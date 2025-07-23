from rest_framework import serializers
from Orders.models import Order
from rest_framework import serializers
from users.models import User
from rest_framework import serializers
from Payment.models import Payment
from products.models import Product
from orderItems.models import OrderItem


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=Order
        fields="__all__"

    

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



class STKPushSerializer(serializers.Serializer):
  phone_number = serializers.CharField()
  amount = serializers.DecimalField(max_digits=10, decimal_places=2)
  account_reference = serializers.CharField()
  transaction_desc = serializers.CharField()
