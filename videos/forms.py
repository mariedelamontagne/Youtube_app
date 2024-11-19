from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import YouTubeVideo
from .models import Comment

class VideoForm(forms.ModelForm):
    class Meta:
        model = YouTubeVideo
        fields = ['title', 'url', 'description']  # Include fields from your Video model
        widgets = {
            'url': forms.URLInput(attrs={'placeholder': 'Enter YouTube URL'}),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write a comment...'}),
        }
   