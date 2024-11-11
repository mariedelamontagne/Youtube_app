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
    video = models.ForeignKey(YouTubeVideo, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    text = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.video.title}'
