from django.urls import path, include
from . import views

app_name = 'cocktails_app'
urlpatterns = [
    # -----------------------------------------------------INDEX--------------------------------------------------------
    path('', views.index, name='index'),
]