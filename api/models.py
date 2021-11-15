from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.

class User(AbstractUser):
    status = models.IntegerField(default=1)
    pass


class Post(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    title           = models.CharField(max_length=30, null=False)
    content         = models.TextField(null=False)
    read_count      = models.IntegerField(default=0)
    cmt_count       = models.IntegerField(default=0)
    like_count      = models.IntegerField(default=0)
    status          = models.IntegerField(default=1)
    created_date    = models.DateTimeField(default=timezone.now)
    modified_date   = models.DateTimeField(default=timezone.now)

class PostComment(models.Model):
    user            = models.ForeignKey(User, on_delete=models.CASCADE)
    post            = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent_comment  = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    content         = models.TextField(null=False)
    status          = models.IntegerField(default=1)
    is_anonymous    = models.BooleanField(default=False)
    created_date    = models.DateTimeField(default=timezone.now)
    modified_date   = models.DateTimeField(default=timezone.now)

class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.IntegerField(default=1)

