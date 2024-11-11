# youtube_app/models.py

from django.db import models
from django.contrib.auth.models import User

class YouTubeVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(YouTubeVideo, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.video.title}"
