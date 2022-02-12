from django.urls import path
from .views import *


urlpatterns = [
    path('<int:pk>', profile, name='profile'),
    path('login/', user_login, name='user_login'),
    path('register/', user_register, name='user_register'),
    path('logout/', user_logout, name='user_logout'),
    path('set-salesman/', set_salesman, name="set_salesman"),
    path('show-item/<int:pk>',  show_item, name="show_item"),
    path('hide-item/<int:pk>', hide_item, name="hide_item"),
    path('settings/', profile_settings, name='profile_settings'),
    path('shop-settings/', shop_settings, name='shop_settings'),
    path('item-delete/<int:pk>', item_delete, name='item_delete'),
    path('item-add/', add_item, name='add_item'),
    path('item-edit/<int:pk>', edit_item, name='edit_item'),
]
