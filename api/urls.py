from django.urls import path
from .views import ProductItemView

urlpatterns = [
    path('api', ProductItemView.as_view()), 
]