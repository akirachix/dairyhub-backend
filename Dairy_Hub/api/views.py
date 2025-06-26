from django.shortcuts import render

from rest_framework import viewsets
from Payment.models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
     queryset=Payment.objects.all()
     serializer_class=PaymentSerializer

# Create your views here.
