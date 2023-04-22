from django.contrib import admin
from django.urls import path

from django import views
from . import views

#Urls for users and pages
urlpatterns = [
    path('home/', views.landingPages, name='home'),
    path('signIn/', views.user_login, name='signIn'),
    path('logout/', views.signout, name='logout'),
    #path('home/', views.landingPages, name='home'),
]
