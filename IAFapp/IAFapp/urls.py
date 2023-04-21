from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from IAFBenflex import views

#Urls for gestion administration user (Crud - usuarios)
urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('create_user/', views.create_user, name='register'),
    path('edit_user/', views.edit_user, name='edit'),
    path('delete_user/', views.delete_user, name='delete'),
    path('', include('IAFBenflex.urls')),
]
