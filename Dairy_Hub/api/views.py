from django.shortcuts import render


from rest_framework import viewsets
from Orders.models import Order
from .serializers import OrderSerializer
from Payment.models import Payment
from .serializers import PaymentSerializer
from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from products.models import Product
from orderItems.models import OrderItem
from .serializers import ProductSerializer
from .serializers import OrderItemSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class=OrderSerializer
    



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

