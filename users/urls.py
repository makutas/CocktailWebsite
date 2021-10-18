"""Defines URL patterns for users"""

from django.urls import path, include
from .views import *

app_name = 'users'
urlpatterns = [
    # INCLUDE DEFAULT AUTH URLS
    path('', include('django.contrib.auth.urls')),
    # REGISTRATION PAGE
    # path('register/', views.register, name='register'),
]