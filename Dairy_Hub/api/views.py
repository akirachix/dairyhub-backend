
from django.shortcuts import render
from rest_framework import viewsets
from Payment.models import Payment
from .serializers import PaymentSerializer
from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer

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

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
     queryset=Payment.objects.all()
     serializer_class=PaymentSerializer
