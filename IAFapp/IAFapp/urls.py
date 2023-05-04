from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from IAFBenflex import views

# Urls for gestion administration user (Crud - usuarios)
urlpatterns = [
    path('index/', views.index, name='index'),
    path('home/', views.landingPages, name='home'),
    path('admin/', admin.site.urls, name='admin'),
    path('create_task/', views.create_task, name='create_task'),
    path('list_task/<int:task_id>/', views.list_task, name='list_task'),
    path('update_task/<int:task_id>/', views.update_task, name='update_task'),
    path('complete_task/<int:task_id>/complete', views.completed_task, name='complete_task'),
    path('delete_task/<int:task_id>/delete', views.delete_user, name='delete_task'),
    path('', include('IAFBenflex.urls')),
]
