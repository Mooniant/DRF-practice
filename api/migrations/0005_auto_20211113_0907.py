# Generated by Django 3.2.9 on 2021-11-13 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20211113_0906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='postcomment',
            name='content',
            field=models.TextField(),
        ),
    ]
