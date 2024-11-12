# youtube_app/videos/views.py

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import YouTubeVideo, Comment
from django.contrib.auth.decorators import login_required

def video_list(request):
    return HttpResponse("This is the video list page.")

def video_detail(request, video_id):
    return HttpResponse(f"This is the detail page for video {video_id}.")

def home(request):
    return render(request, 'home.html')

def register(request):
    return HttpResponse("Registration page")

def post_comment(request, video_id):
    # Fetch the video by ID or show a 404 error if not found
    video = get_object_or_404(YouTubeVideo, id=video_id)

    if request.method == 'POST':
        content = request.POST.get('content')  # Get the content of the comment from the form
        # Create the comment and associate it with the logged-in user and the video
        Comment.objects.create(video=video, content=content)

        # Redirect to the video's detail page or video list after posting the comment
        return redirect('video_list')  # Change this if you want to redirect somewhere else

    return render(request, 'post_comment.html', {'video': video})