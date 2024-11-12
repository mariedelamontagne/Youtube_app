from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # This is the homepage, accessible via http://127.0.0.1:8000/
    path('register/', views.register, name='register'),  # Existing URL for registration
    path('videos/', views.video_list, name='video_list'),  # Replace with the correct video list view
    path('videos/<int:video_id>/comment/', views.post_comment, name='post_comment'),  # Replace with correct comment posting view
]

from django.contrib.auth.decorators import login_required
from .models import YouTubeVideo, Comment
from django.shortcuts import render, redirect
from .forms import CommentForm

@login_required
def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'video_list.html', {'videos': videos})

@login_required
def post_comment(request, video_id):
    video = YouTubeVideo.objects.get(id=video_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.video = video
            form.save()
            return redirect('video_list')
    else:
        form = CommentForm()
    return render(request, 'post_comment.html', {'form': form, 'video': video})

def home(request):
    return render(request, 'home.html')