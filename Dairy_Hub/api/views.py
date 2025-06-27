from django.shortcuts import render
from rest_framework import viewsets
from Payment.models import Payment
from .serializers import PaymentSerializer

# Create your views here.
from rest_framework import viewsets
from users.models import User
from .serializers import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PaymentViewSet(viewsets.ModelViewSet):
     queryset=Payment.objects.all()
     serializer_class=PaymentSerializer

