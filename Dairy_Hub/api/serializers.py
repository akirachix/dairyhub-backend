from rest_framework import serializers

from products.models import Product

from orderItems.models import OrderItem

class ProductSerializer(serializers.ModelSerializer):
       class Meta:
              model=Product
              fields= "__all__"

class OrderItemSerializer(serializers.ModelSerializer):
       class Meta:
              model=OrderItem
              fields= "__all__"