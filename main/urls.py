from django.urls import path
from .views import *


urlpatterns = [
    path('', main_index, name='main_index'),
    path('salesmans/', salesmans, name='salesmans'),
    path('products/', all_products, name='all_products'),
]
