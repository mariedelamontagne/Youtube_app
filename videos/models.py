from django.db import models
from django.contrib.auth.models import User

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    date_uploaded = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='video_comments')
    # other fields

