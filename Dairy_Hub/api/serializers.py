

from rest_framework import serializers
from users.models import User
from rest_framework import serializers
from Payment.models import Payment

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = "__all__"


class PaymentSerializer(serializers.ModelSerializer):
       class Meta:
              model=Payment
              fields= "__all__"

