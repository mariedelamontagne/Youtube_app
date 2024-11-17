from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views import View

urlpatterns = [
    path('admin/', admin.site.urls),
    path("accounts/", include("django.contrib.auth.urls")), 
    path('videos/', include('videos.urls')),  
]