from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    user_description = models.CharField(max_length=200, null=True)
    user_avatar = models.ImageField(null=True, blank=True)
    user_uploaded_recipes = models.IntegerField() # Increment by 1 on upload
