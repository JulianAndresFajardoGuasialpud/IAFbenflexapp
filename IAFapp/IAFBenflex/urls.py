from django.contrib import admin
from django.urls import path

from django import views
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('users/', views.user_login, name='login'),
    path('create_user/', views.create_user, name='register'),
    path('edit_user/', views.edit_user, name='edit'),
    path('delete_user', views.delete_user, name='delete'),
    path('logout_user', views.logout_user, name='logout'),
]