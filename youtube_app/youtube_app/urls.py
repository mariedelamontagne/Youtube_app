from django.contrib import admin
from django.urls import path, include
from . import views  # Import your views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('youtube_app.urls')),
]
