from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('index/', views.index, name='landingPage'),
    path('users/', views.user_login, name='login'),
    path('create_user/', views.create_user, name='register'),
    path('edit_user/', views.edit_user, name='edit'),
]