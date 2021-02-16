from django.db import models
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django import forms


class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    profile_picture = models.CharField(max_length=255, default=None)
    about_me = models.CharField(max_length=255, default=None)
    position = models.CharField(max_length=100, default=None)
