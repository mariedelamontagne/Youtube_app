from django.contrib import admin
from django.urls import path, include
from . import views  

urlpatterns = [
    path('', views.home, name='home'),  # Homepage route
    path('register/', views.register, name='register'),  # Registration route
    path('videos/', views.video_list, name='video_list'),  # Video list route
    path('videos/<int:video_id>/comment/', views.post_comment, name='post_comment'),
]
