from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('videos.urls')),
    path('videos/<int:video_id>/comment/', views.post_comment, name='post_comment')
]
