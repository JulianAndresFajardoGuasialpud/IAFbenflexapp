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
    path('update_and_list/<int:task_id>/', views.update_and_list, name='update_and_list'),
    path('complete_task/<int:task_id>/complete', views.complete_task, name='complete_task'),
    path('delete_task/<int:task_id>/delete', views.delete_task, name='delete_task'),
    path('', include('IAFBenflex.urls')),
]
