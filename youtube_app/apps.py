from django.apps import AppConfig


class VideosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'videos'
    
# youtube_app/apps.py

from django.apps import AppConfig

class YoutubeAppConfig(AppConfig):
    name = 'youtube_app'
