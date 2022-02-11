from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def profile(request, pk):
    user = Profile.objects.get(user=pk)
    data = {
        'user': user
    }
    return render(request, 'users/profile.html', data)
    

def user_login(request):
    data = {

    }
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main_index')
        else:
            messages.info(request, "Username or password is incorrect")
            return render(request, 'users/login.html', data)
    return render(request, 'users/login.html', data)


def user_register(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST.get('username')
            password = request.POST.get('password1')

            profile = Profile()
            profile.user = User.objects.get(username=username)
            profile.name = username
            profile.save()

            user = authenticate(request, username=username, password=password)
            login(request, user)
            return redirect('main_index')

    data = {
        'form': form
    }
    return render(request, 'users/registration.html', data)


def user_logout(request):
    logout(request)
    return redirect('user_login')