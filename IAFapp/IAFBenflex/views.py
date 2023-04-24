from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers.serializers import UserSerializers

# Users django
from django.contrib.auth.models import User

# Users from table IAFBenflex
from IAFBenflex.models import Users

# imports
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages

# Import forms
from .forms import TaskForm

# Import Task
from .models import Task

# Create your views here.

# View landing page
def landingPages(request):
    if request.method == 'GET':
        return render(request, 'home.html')

# View index
def index(request):
    return render(request, "index.html")

# View login
def user_login(request):
    if request.method == 'GET':
        return render(request, "signIn.html",
                      {'form_auth': AuthenticationForm}
                      )
    else:
        users = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if users is None:
            return render(request, "signIn.html",
                          {'form_auth': AuthenticationForm,
                           'errors': 'Username or password is incorrecto or dont exists in the database'}
                          )
        else:
            login(request, users)
            return redirect('index')

# View para cerrar sesion de users
def signout(request):
    logout(request)
    return redirect('home')


# View para la lista de usuarios de administacion
@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)

# View to create user
@api_view(['GET', 'POST'])
def create_user(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm})
    else:
        if request.POST['password1'] == request.POST['password2']:

            try:
                users = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'],
                )
                users.save()
                login(request, users)
                return redirect('index')
            except IntegrityError:
                return render(request, 'register.html',
                              {'form': UserCreationForm, 'errors': 'User already exists'})
        return render(request, 'register.html',
                      {'form': UserCreationForm, 'errors': 'passwod do not mach'})

# View create task
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html',
                      {'forms': TaskForm})
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('index')
        except ValueError:
            return render(request, 'create_task.html',
                          {'forms': TaskForm, 'errors': 'please provide valid data'})

# view to edit user
@api_view(['PUT'])
def edit_user(request, user_id):
    user = User.edit_user(request, pk=user_id)
    if request.method == 'PUT':
        users = User.objects.edit_user(
            request.PUT['username'], isinstance=user)
        if users.is_valid():
            users.save()
            return Response('user_list')
    else:
        return Response('the user do not edit')

# View to delete user
def delete_user(request, user_id):
    if request.method == 'DELETE':
        users = User.objects.delete_user()
