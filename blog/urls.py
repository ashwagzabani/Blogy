from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('logIn/', auth_views.LoginView.as_view(template_name='logIn.html'), name='logIn'),
    path('signup/', views.signup, name='signup'),
    path('user/posts/', views.userPostsList, name='userPostsList'),
]
