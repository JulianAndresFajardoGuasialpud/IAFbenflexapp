from django.utils import timezone
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

# from .serializers.serializers import UserSerializers

# Users django
from django.contrib.auth.models import User

# import from Users table
# from IAFBenflex.models import Users

# imports for user autenticated
from django.contrib.auth import login, logout, authenticate

# Import forms
from .forms import TaskForm

# Import Task to model
from .models import Task


# Create your views here.

""" !Views for user django model database and task crud  """

# View landing page


@api_view(['GET'])
def landingPages(request):
    if request.method == 'GET':
        return render(request, 'home.html')


# View to tasks completed
def completed_task(request):
    task = Task.objects.filter(
        user=request.user, datecompleted__isnull=False).order_by('-datecompleted')
    return render(request, "index.html", {'tasks': task})


# View tasks not completed (task pending of users)

@api_view(['GET'])
def index(request):
    if request.method == 'GET':
        task = Task.objects.filter(
            user=request.user, datecompleted__isnull=True)
        return render(request, "index.html", {'tasks': task})

# View login django user


@api_view(['GET', 'POST'])
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


# View for logout django user and redirect homepage


def signout(request):
    logout(request)
    return redirect('home')


""" !Views for user django model database and task crud  """


""" Functions to tasks """
# View to create task


@api_view(['GET', 'POST'])
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

# View to list task


@api_view(['GET'])
def list_task(request, list_id):
    if request.method == 'GET':
        details = get_object_or_404(Task, pk=list_id)
        detailTask = TaskForm(request.GET, instance=details)
        return render(request, 'index', {'details': detailTask})

# View to update tasks


@api_view(['POST'])
def update_task(request, task_id):
    try:
        if request.method == 'POST':
            updateTask = get_object_or_404(Task, pk=task_id)
            formTask = TaskForm(request.POST, instance=updateTask)
            formTask.save()
            return redirect('index')
    except ValueError:
        return render(request, 'updateTask.html', {'update': updateTask, 'form': formTask, 'errors': 'Error updating task'})


# view to edit user
@api_view(['GET', 'PUT'])
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


# View to delete users table_2
def delete_user(request, user_id):
    if request.method == 'DELETE':
        users = User.objects.delete_user()
