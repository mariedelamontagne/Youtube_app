from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('videos/', views.video_list, name='video_list'),
    path('videos/<int:video_id>/comment/', views.post_comment, name='post_comment'),
]
