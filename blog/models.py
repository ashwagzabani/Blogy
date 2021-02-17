from django.db import models
from django.contrib.auth.models import User


class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.CharField(max_length=255)
    about_me = models.CharField(max_length=255)
    position = models.CharField(max_length=100)
