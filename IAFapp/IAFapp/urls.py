from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from IAFBenflex import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', include('IAFBenflex.urls')),
]
