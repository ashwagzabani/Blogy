from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', views.logIn, name='logIn'),
    path('signup/', views.signup, name='signup'),
]

