"""Defines URL patterns for users"""

from django.urls import path, include
from . import views

app_name = 'users'
urlpatterns = [
    # --------------------------------------------INCLUDE DEFAULT AUTH URLS---------------------------------------------
    path('', include('django.contrib.auth.urls')),
    # ------------------------------------------------REGISTER NEW USER-------------------------------------------------
    path('register/', views.register_new_user, name='register'),
    # ------------------------------------------------------LOGIN-------------------------------------------------------

]