from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('accounts/signup/', views.register_view, name='register'),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("", TemplateView.as_view(template_name="home.html"), name="home"),
    path('landingpage/', views.home_view, name='landingpage'),
    #path('', views.home_view, name='home'),
    path('video_list/', views.video_list, name='video_list'),
    #path('post_comment/<int:video_id>/', views.post_comment, name='post_comment'),
    
]


    