from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', profile, name='main_index'),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
]
