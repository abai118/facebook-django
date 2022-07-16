# Generated by Django 4.0.6 on 2022-07-16 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0002_post_time'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post',
        ),
        migrations.AddField(
            model_name='post',
            name='postImg',
            field=models.ImageField(default=None, upload_to='media/posts'),
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='image',
            field=models.ImageField(upload_to='media/ProfilePics'),
        ),
    ]
