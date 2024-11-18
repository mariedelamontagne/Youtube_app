from django.contrib import admin
from .models import YouTubeVideo
from .models import Video

# Register your models here.
admin.site.register(YouTubeVideo)

class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'description', 'created_at')
