MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # Correct order
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # Must come after SessionMiddleware
    'django.contrib.messages.middleware.MessageMiddleware',  # After AuthenticationMiddleware
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # To handle login sessions
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,  # This makes Django look for templates inside app directories
       # "DIRS": [BASE_DIR / "templates"],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


DEBUG = True


# settings.py

INSTALLED_APPS = [
    # Default apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    

    # Your app
    'youtube_app', 
    'videos.apps.VideosConfig',
]

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ROOT_URLCONF = 'youtube_app.urls'  # Point to your main URL configuration

import os
from pathlib import Path

# Define BASE_DIR (root of the project directory)
BASE_DIR = Path(__file__).resolve().parent.parent

# Static file settings
STATIC_URL = '/static/'  # URL prefix for static files

# Optional: Define the location for your static files (for development)
STATICFILES_DIRS = [
    BASE_DIR / 'static',  # Custom static folder at the root level of your project
]

# Optional: Define where static files should be collected in production
STATIC_ROOT = BASE_DIR / 'staticfiles'  # For production deployment

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

SECRET_KEY = "iu6+lujh2)xru+9hhy!rtb$m=^a&mzhs5*1ygbpu+qil7b)^*f"

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Database engine (SQLite)
        'NAME': BASE_DIR / 'db.sqlite3',  # Path to the SQLite database file
    }
}

LOGIN_REDIRECT_URL = '/videos/video_list/'
LOGOUT_REDIRECT_URL = '/videos/landingpage/'