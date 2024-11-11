# youtube_app/models.py

from django.db import models

class YouTubeVideo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200)
    url = models.URLField()

    def __str__(self):
        return self.title


class Comment(models.Model):
    video = models.ForeignKey(YouTubeVideo, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return f"Comment on {self.video.title}"
