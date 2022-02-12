from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from products.models import *
from django.core.files.storage import FileSystemStorage


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


def profile_settings(request):
    user = Profile.objects.get(user=request.user.pk)
    data = {
        'user': user
    }
    if request.method == 'POST':
        username = request.POST.get('username')
        status = request.POST.get('status')
        avatar = request.POST.get('user_photo')
        if avatar:
            user.user_image = avatar
            user.save()
        if username:
            user = Profile.objects.get(user=request.user.pk)
            user.status = status
            user2 = User.objects.get(pk=request.user.pk)
            user.name = username
            user2.username = username
            if not user.is_salesman:
                user.is_salesman = request.POST.get('is_salesman')
            user.save()
            user2.save()
            return redirect('profile_settings')
    return render(request, 'users/settings.html', data)


def shop_settings(request):
    user = Profile.objects.get(user=request.user.pk)
    data = {
        'user': user
    }
    if request.method == 'POST':
        background = request.POST.get('background')
        user.shop_background = background
        user.save()
        return redirect('shop_settings')
    return render(request, 'users/shop_settings.html', data)
    

def item_delete(request, pk):
    Product.objects.get(pk=pk).delete()
    return redirect('profile', request.user.pk)


def add_item(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.POST.get('image')
        describe = request.POST.get('describe')
        price = request.POST.get('price')
        is_publish = request.POST.get('is_pub')
        profile = Profile.objects.get(user=request.user.pk)
        if title != "" and describe != "" and price != "0":  
            if is_publish == "on":
                is_publish = True
            else:
                is_publish = False
            Product(
                salesman = profile,
                title = title,
                image = image,
                describe = describe,
                price = price,
                is_publish = is_publish
            ).save()
            return redirect('profile', request.user.pk)
    return render(request, 'products/add.html')


def edit_item(request, pk):
    item = Product.objects.get(pk=pk)
    title = request.POST.get('title')
    image = request.POST.get('image')
    describe = request.POST.get('describe')
    price = request.POST.get('price')
    is_publish = request.POST.get('is_pub')
    data = {
        'item': item
    }
    profile = Profile.objects.get(user=request.user.pk)
    if request.method == 'POST':
        if is_publish == "on":
            is_publish = True
        else:
            is_publish = False
        if title != "" and describe != "" and price != '0':
            item.image = image
            item.title = title
            item.describe = describe
            item.price = price
            item.is_publish = is_publish
            item.save()
        return redirect('profile', profile.pk)
    return render(request, 'products/edit.html', data)