from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from . import views
from .views import SignUpView
from django.contrib.auth.views import LoginView
#from .views import add_video
#from .views import video_detail

urlpatterns = [
    path('login/', LoginView.as_view(template_name='videos/login.html'), name='login'),
    path('signup/', SignUpView.as_view(), name="signup"),
    path('landingpage/', views.home_view, name='landingpage'),
    path('video_list/', views.video_list, name='video_list'),
    path('add_video/', views.add_video, name='add_video'),
    path('video/<int:pk>/', views.video_detail, name='video_detail'),
]


    