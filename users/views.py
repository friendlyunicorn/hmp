from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from products.models import *


def profile(request, pk):
    all_products = Product.objects.filter(salesman=pk)
    shown_products = Product.objects.filter(salesman=pk, is_publish=True)
    user = Profile.objects.get(user=pk)
    data = {
        'all_products': all_products,
        'user': user,
        'shown_products': shown_products,
    }
    if request.user.pk == pk: # you'r profile
        hidden_products = Product.objects.filter(salesman=request.user.pk, is_publish=False)
        data['hidden_products'] = hidden_products
        return render(request, 'users/my_profile.html', data)
    else:
        return render(request, 'users/profile.html', data)
    

def user_login(request):
    data = {
        'user': request.user
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


def set_salesman(request):
    pk = request.user.pk
    user = Profile.objects.get(user=pk)
    user.is_salesman = True
    user.save()
    return redirect('profile', pk=pk)


def show_item(request, pk):
    user = request.user.pk
    item = Product.objects.get(pk=pk)
    item.is_publish = True
    item.save()
    return redirect('profile', pk=user)


def hide_item(request, pk):
    user = request.user.pk
    item = Product.objects.get(pk=pk)
    item.is_publish = False
    item.save()
    return redirect('profile', pk=user)