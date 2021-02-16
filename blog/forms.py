from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from .models import user
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(label="User Name", max_length=64)
    password = forms.CharField(widget=forms.PasswordInput())


class SignUpForm(UserCreationForm, ModelForm):

    class Meta:
        model = User
        model = models.user
        # to hid some fields in form >> use exclude
        exclude = ('profile_picture', 'about_me', 'position',)
        fields = ['first_name', 'last_name', 'username',
                  'email', 'password1', 'password2']
