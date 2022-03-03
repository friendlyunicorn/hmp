from rest_framework import serializers
from .models import *


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ('id', 'title')