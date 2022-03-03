from django.shortcuts import render
from rest_framework import generics, status
from .serializers import ProductItemSerializer
from .models import ProductItem
# Create your views here.

class ProductItemView(generics.ListAPIView):
    model = ProductItem
    serializer_class = ProductItemSerializer