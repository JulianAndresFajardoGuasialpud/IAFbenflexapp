from django.contrib import admin
from django.urls import path

from django import views
from . import views

# routes for users django
urlpatterns = [
    path('signIn/', views.user_login, name='signIn'),
    path('create_user/', views.create_user, name='register'),
    path('logout/', views.signout, name='logout'),
]
