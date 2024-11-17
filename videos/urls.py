from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('home/', views.home_view, name='home'),
    path('video_list/', views.video_list, name='video_list'),
]


    