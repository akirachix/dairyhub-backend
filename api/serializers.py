from rest_framework import serializers
from Orders.models import Order
from rest_framework import serializers
from users.models import User
from rest_framework import serializers
from Payment.models import Payment
from products.models import Product
from orderItems.models import OrderItem
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from users.models import User


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




class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=8,
        style={'input_type': 'password'},
        error_messages={
            'min_length': 'Password must be at least 8 characters long.'
        }
    )
    phone_number = serializers.CharField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Phone number already registered.")]
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all(), message="Email already registered.")]
    )

    class Meta:
        model = User
        fields = ['name', 'phone_number', 'email', 'password', 'type']

    def validate_type(self, value):
        allowed_types = [choice[0] for choice in User.USER_TYPE_CHOICES]
        if value not in allowed_types:
            raise serializers.ValidationError("Invalid user type.")
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)  # securely hash the password
        user.save()
        return user

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
