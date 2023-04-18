from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    return render(request, "index.html")

# Views list users

def user_list(request):
    users = Users.objects.all()

# View to created user


def user_create(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm()
    return render(request, 'user_create.html', {'form': form})

# view to edit user


def user_edit(request, user_id):
    user = get.object_or_404(User, pk=user_id)
    if request.method == 'PUT':
        form = UserForm(request.PUT, isinstance=user)
        if form.is_valid():
            form.save()
            return redirect('user_list')
    else:
        form = UserForm(isinstance=user)
    return render(request, 'user_edit.html', {'form': form, 'user': user})
