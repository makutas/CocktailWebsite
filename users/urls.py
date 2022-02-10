from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'users'
urlpatterns = [
    # --------------------------------------------INCLUDE DEFAULT AUTH URLS---------------------------------------------
    path(r'', include('django.contrib.auth.urls')),
    # ------------------------------------------------REGISTER NEW USER-------------------------------------------------
    path(r'register/', views.register_new_user, name='register'),
    # -----------------------------------------------------LOGIN--------------------------------------------------------
    path(r'login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # -----------------------------------------------------LOGOUT-------------------------------------------------------
    path(r'logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    # TODO - baigti tvarkyti URLS (registration??? i templates)
]
