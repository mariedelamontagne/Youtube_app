# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo, Comment
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'login.html')

def register_view(request):
    return render(request, 'register.html')

def home_view(request):
    return render(request, 'videos/home.html')

def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'videos/video_list.html')