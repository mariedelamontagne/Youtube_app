from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.views import View

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin route
    path('', include('videos.urls')),  # Include your app's URLs
#    path('login/', View.as_view(), name='login'),  # Login view
#    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Logout view
]