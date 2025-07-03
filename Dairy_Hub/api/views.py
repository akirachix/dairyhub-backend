from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Orders.models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class=OrderSerializer
    

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

