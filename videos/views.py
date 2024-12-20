# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .models import YouTubeVideo, Comment
from .forms import VideoForm
from .forms import CommentForm

class MyLoginView(LoginView):
    template_name = 'login.html'  # Your login template
    redirect_authenticated_user = True  # Redirect logged-in users

def login_view(request):
    return render(request, 'videos/login.html')

def get_success_url(self):
        return reverse_lazy('video_list')  
 
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "videos/signup.html"

def signup_view(request):
    return render(request, 'videos/signup.html')

def home_view(request):
    return render(request, 'videos/home.html')

@login_required
def video_list(request):
    videos = YouTubeVideo.objects.all()
    return render(request, 'videos/video_list.html', {"videos" : videos})

class VideoListView (ListView):
    model = YouTubeVideo
    template_name = 'videos/video_list.html'  
    context_object_name = 'videos'
    
def video_detail(request, pk):
    video = get_object_or_404(YouTubeVideo, pk=pk)
    comments = video.comments.all()  # Retrieve all comments for the video
    form = CommentForm(request.POST or None)  # Handle GET and POST requests for the comment form

    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.video = video  # Associate the comment with the video
        new_comment.save()  # Save the comment

        return redirect('video_detail', pk=video.pk)  # Redirect to the same page

    return render(request, 'videos/video_detail.html', {
        'video': video,
        'comments': comments,
        'form': form,
    })

@login_required
def add_comment(request):
    pass

@login_required  
def add_video(request):
    if request.method == 'POST':
        form = VideoForm(request.POST)
        if form.is_valid():
            video = form.save(commit=False)
            print("Saving video:", video.title, video.url, video.description)  # Debug data
            video.save()
            print("Video saved successfully!")
            return redirect('video_list')
        else:
            print("Form is invalid:", form.errors)  # Debug errors
    else:
        form = VideoForm()

    return render(request, 'add_video.html', {'form': form})

def table_view(request):
    videos = YouTubeVideo.objects.all()  # Fetch all YouTube videos
    return render(request, 'table_view.html', {'videos': videos})