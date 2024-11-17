from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views
from .views import SignUpView

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('landingpage/', views.home_view, name='landingpage'),
    path('video_list/', views.video_list, name='video_list'),
    path('post_comment/<int:video_id>/', views.add_comment, name='add_comment'),
    path('post_video/<int:video_id>/', views.add_video, name='add_video'),
]


    