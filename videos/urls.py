from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('landingpage/', views.home_view, name='landingpage'),
    #path('', views.home_view, name='home'),
    path('video_list/', views.video_list, name='video_list'),
   # path('post_comment/<int:video_id>/', views.post_comment, name='post_comment'),
]


    