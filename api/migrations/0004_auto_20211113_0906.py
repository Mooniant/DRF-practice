# Generated by Django 3.2.9 on 2021-11-13 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_comment_postcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(default=None, max_length=30),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(default=None),
        ),
    ]
