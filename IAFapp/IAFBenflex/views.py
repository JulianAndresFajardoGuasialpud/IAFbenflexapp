from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers.serializers import UserSerializers

# Users django
from django.contrib.auth.models import User

# Users from table IAFBenflex
from IAFBenflex.models import Users

# imports
from django.contrib.auth import login
# Create your views here.

# View landing page


def index(request):
    return render(request, "index.html")

# View login


def user_login(request):
    return render(request, "login.html")

# Views list users


@api_view(['GET'])
def user_list(request):
    users = User.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)

# View to created user


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
                serializer = UserSerializers({users}, many=False)
                if serializer.is_valid():
                    return Response(serializer.data, 'User created succesfully')
                else:
                    return render(request, 'register.html',
                                  {'form': UserCreationForm, 'errors': 'User already exists'})
        return render(request, 'register.html',
                      {'form': UserCreationForm, 'errors': 'passwod do not mach'})                     
""" @api_view(['GET', 'POST'])
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
                serializer = UserSerializers({users}, many=False)
                if serializer.is_valid():
                    return Response(serializer.data, 'User created succesfully')
                else:
                    return render(request, 'register.html',
                                  {'form': UserCreationForm, 'errors': 'User already exists'})
        return render(request, 'register.html',
                      {'form': UserCreationForm, 'errors': 'passwod do not mach'}) """
# view to edit user


@api_view(['PUT'])
def edit_user(request, user_id):
    user = Users.get.object_or_404(Users, pk=user_id)
    if request.method == 'PUT':
        user = Users.objects.edit_user(
            request.PUT['username'], isinstance=user)
        if user.is_valid():
            user.save()
            return Response('user_list')
    else:
        return Response('the user do not edit')
