from django.shortcuts import render
from users.models import Profile
from products.models import *


def main_index(request):
    if request.user.is_anonymous:
        user = None
    else:
        # print(request.user.pk)
        # user = None
        user = Profile.objects.get(user=request.user.pk)

    data = {
        'user': user
    }
    return render(request, 'main/index.html', data)


def salesmans(request):
    users = Profile.objects.filter(is_salesman=True)
    data = {
        'salesmans': users
    }
    return render(request, 'main/salesmans.html', data)


def all_products(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'products/products.html', data)