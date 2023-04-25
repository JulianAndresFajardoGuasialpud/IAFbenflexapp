from django.contrib import admin
from django.urls import path

from django import views
from . import views

# Urls for users and pages
urlpatterns = [
    path('home/', views.landingPages, name='home'),
    path('signIn/', views.user_login, name='signIn'),
    path('create_user/', views.create_user, name='register'),
    path('edit_user/', views.edit_user, name='edit'),
    path('logout/', views.signout, name='logout'),
    path('delete_user/', views.delete_user, name='delete'),
]
