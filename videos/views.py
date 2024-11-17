# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo, Comment
from django.contrib.auth.decorators import login_required

def login_view(request):
    return render(request, 'videos/login.html')

def register_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # Redirect to home or another page after login
            return redirect('home')  # Or any other view name
    else:
        form = AuthenticationForm()

    return render(request, 'videos/login.html', {'form': form})

def home_view(request):
    return render(request, 'videos/home.html')

def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'videos/video_list.html')