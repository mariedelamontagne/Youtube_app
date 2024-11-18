from django.db import models
from django.contrib.auth.models import User
from django.db import models

class YouTubeVideo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    url = models.URLField()
    pub_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    video = models.ForeignKey('Video', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)  # Optional: Use Django's User model for authentication
    content = models.TextField()


    def __str__(self):
        return f"Comment by {self.author} on {self.video.title}"

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title