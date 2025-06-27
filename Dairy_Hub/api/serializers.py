
from rest_framework import serializers

from products.models import Product

from orderItems.models import OrderItem
from rest_framework import serializers
from users.models import User
from rest_framework import serializers
from Payment.models import Payment

class ProductSerializer(serializers.ModelSerializer):
       class Meta:
              model=Product
              fields= "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
       class Meta:
              model=OrderItem
              fields= "__all__"


class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
       class Meta:
              model=Payment
              fields= "__all__"
