# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo, Comment
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

def login_view(request):
    return render(request, 'videos/video_list.html')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to home or another page after login
            return redirect('home')  # Or any other view name
    else:
        form = UserCreationForm()

    return render(request, 'videos/login.html', {'form': form})

def home_view(request):
    return render(request, 'videos/home.html')

def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'videos/video_list.html', {"videos" : videos})

class VideoListView (ListView):
    model = YouTubeVideo
    template_name = 'videos/video_list.html'  
    context_object_name = 'videos'
    