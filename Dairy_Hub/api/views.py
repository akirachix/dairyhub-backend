
from django.shortcuts import render

from rest_framework import viewsets

from products.models import Product

from orderItems.models import OrderItem

from .serializers import ProductSerializer

from .serializers import OrderItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
     queryset=Product.objects.all()
     serializer_class=ProductSerializer


class OrderItemViewSet(viewsets.ModelViewSet):
     queryset=OrderItem.objects.all()
     serializer_class=OrderItemSerializer

