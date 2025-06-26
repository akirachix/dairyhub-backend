from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from Orders.models import Order
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    queryset= Order.objects.all()
    serializer_class=OrderSerializer
    