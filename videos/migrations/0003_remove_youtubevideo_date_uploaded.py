# Generated by Django 5.1.3 on 2024-11-17 16:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0002_youtubevideo_remove_comment_video_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='youtubevideo',
            name='date_uploaded',
        ),
    ]
