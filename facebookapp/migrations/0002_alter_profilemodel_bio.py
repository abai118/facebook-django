# Generated by Django 4.0.6 on 2022-07-17 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facebookapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profilemodel',
            name='bio',
            field=models.CharField(max_length=200),
        ),
    ]
