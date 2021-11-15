from django.contrib.auth.models import User
from django.contrib.auth        import get_user_model
from django.http                import JsonResponse
from django.shortcuts           import get_object_or_404
from rest_framework             import viewsets, filters, status
from rest_framework             import permissions
from rest_framework.response    import Response
from rest_framework.decorators  import action
from api.serializers            import *
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permissions_classes = [permissions.IsAuthenticated]

    # def get_queryset(self,pk):
    #     return User.objects.filter(pk=pk)

    def retrieve(self, request, pk=None):
        user = get_object_or_404(self.queryset, pk=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permissions_classes = [permissions.IsAuthenticated]
    def get_user(self):
        return get_object_or_404(User.objects.all(), pk=3)

    @action(methods=['post'], detail=False)
    def write(self, request, *args, **kwargs):
        request.data['user'] = self.get_user().id
        # serializer = PostSerializer(data=request.data)
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        post = get_object_or_404(self.queryset, pk=pk)
        cmt_queryset = PostComment.objects.filter(post=post)
        cmt_serializer = PostCommentSerializer(cmt_queryset, many=True)
        post_data = PostSerializer(post).data
        post_data['comments'] = cmt_serializer.data
        return Response(post_data, status=status.HTTP_200_OK)
        # else :
        #     return Response(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        request.data['user'] = self.get_user().id
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(methods=['post'], detail=True)
    def comment(self, request, pk):
        user = self.get_user()
        post = get_object_or_404(self.queryset, pk=pk)
        request.data['user'] = user.id
        request.data['post'] = post.id
        cmt_serializer = PostCommentSerializer(data=request.data)
        if cmt_serializer.is_valid():
            self.perform_create(cmt_serializer)
            return Response(cmt_serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(cmt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    @action(methods=['post'], detail=True)
    def recomment(self, request, *args, **kwargs):
        user = User.objects.get(id=4)
        request.data['user'] = user.id
        request.data['post'] = kwargs['post_id']
        request.data['parent_comment'] = kwargs['parent_comment_id']
        cmt_serializer = PostCommentSerializer(data=request.data)
        if cmt_serializer.is_valid():
            self.perform_create(cmt_serializer)
            return Response(cmt_serializer.data, status=status.HTTP_200_OK)
        else :
            return Response(cmt_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

