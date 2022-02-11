from django.urls import path
from .views import *


urlpatterns = [
    path('', main_index, name='main_index'),
]
