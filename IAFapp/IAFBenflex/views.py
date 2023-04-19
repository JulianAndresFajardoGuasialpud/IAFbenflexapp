from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from IAFBenflex.models import Users

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers.serializers import UserSerializers
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
    users = Users.objects.all()
    serializer = UserSerializers(users, many=True)
    return Response(serializer.data)

# View to created user

def create_user(request):
    if request.method == 'GET':
        return render(request, 'register.html', {'form': UserCreationForm})
    else:
        if request.POST.get['password'] == request.POST.get['password_confirm']:
            try:
                data = Users.objects.create_user(username=request.POST['username'],
                                                email=request.POST['email'],
                                                is_active=request.POST[''],
                                                is_staff=request.POST[''],
                                                is_superuser=request.POST[''],
                                                password=request.POST['password'],
                                                password_confirm=request.POST['password_confirm'],
                                                created_at=request.POST[''],
                                                update_at=request.POST[''],
                                                )
                data.save()
                return Response('user create')
            except:
                if data.exist():
                    return Response('username already exist')
# view to edit user


def edit_user(request, user_id):
    user = Users.get.object_or_404(Users, pk=user_id)
    if request.method == 'PUT':
        user = Users.objects.edit_user(request.PUT['username'], isinstance=user)
        if user.is_valid():
            user.save()
            return Response('user_list')
    else:
        return Response('the user do not edit')