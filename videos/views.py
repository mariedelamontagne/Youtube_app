# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

def login_view(request):
    return render(request, 'videos/login.html')

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "videos/signup.html"

def signup_view(request):
    return render(request, 'videos/signup.html')

def home_view(request):
    return render(request, 'videos/home.html')

def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'videos/video_list.html', {"videos" : videos})

class VideoListView (ListView):
    model = YouTubeVideo
    template_name = 'videos/video_list.html'  
    context_object_name = 'videos'
    
def add_video(request):
    pass

def add_comment(request):
    pass

def video_detail(request):
    pass