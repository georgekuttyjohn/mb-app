# Generated by Django 2.2.2 on 2019-06-10 10:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
