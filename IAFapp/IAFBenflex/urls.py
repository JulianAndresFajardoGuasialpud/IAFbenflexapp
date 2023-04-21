from django.contrib import admin
from django.urls import path

from django import views
from . import views

#Urls for users and pages
urlpatterns = [
    path('index/', views.index, name='index'),
    path('user_login/', views.user_login, name='signIn'),
    path('logout/', views.signout, name='logout'),
    path('home/', views.landingPages, name='home'),
]
