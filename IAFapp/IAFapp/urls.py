from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from IAFBenflex import views

# Urls for gestion administration user (Crud - usuarios)
urlpatterns = [
    path('index/', views.index, name='index'),
    path('admin/', admin.site.urls, name='admin'),
    path('create_task/', views.create_task, name='create_task'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('', include('IAFBenflex.urls')),
]
