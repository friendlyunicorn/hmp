from django.urls import path
from .views import *


urlpatterns = [
    path('', all_products, name='all_products'),
    path('item-info-<int:pk>', item_info, name='item_info')
]
