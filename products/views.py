from django.shortcuts import render, get_object_or_404
from .models import *


def all_products(request):
    products = Product.objects.all()
    data = {
        'products': products
    }
    return render(request, 'products/products.html', data)


def item_info(request, pk):
    item = get_object_or_404(Product, pk=pk)
    items = Product.objects.all()
    itemsr = items.reverse()
    data = {
        'item': item
    }
    if item.pk != items[0] and item.pk != itemsr[0]:
        while True:
            next = get_object_or_404(Product, pk=pk+1)
            if next != None:
                break
        while True:
            back = get_object_or_404(Product, pk=pk-1)
            if back != None:
                break
        data['next'] = next
        data['back'] = back
    elif item.pk == itemsr[0]:
        while True:
            back = get_object_or_404(Product, pk=pk-1)
            if back != None:
                break
        data['back'] = back
    elif item.pk == items[0]:
        while True:
            next = get_object_or_404(Product, pk=pk+1)
            if next != None:
                break
        data['next'] = next
    return render(request, 'products/iteminfo.html', data)