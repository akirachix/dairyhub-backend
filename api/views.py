from django.shortcuts import render

from django.utils import timezone
import datetime
from rest_framework import viewsets
from Orders.models import Order
from .serializers import OrderSerializer
from Payment.models import Payment
from .serializers import PaymentSerializer
from users.models import User
from .serializers import UserSerializer
from rest_framework import viewsets


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .daraja import DarajaAPI
from .serializers import STKPushSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
 
from products.models import Product
from orderItems.models import OrderItem
from .serializers import ProductSerializer
from .serializers import OrderItemSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token

from django.contrib.auth import authenticate
from users.permission import IsFarmer, IsSupplier,IsFarmerOrSupplier 
from .serializers import RegisterSerializer, LoginSerializer
from users.models import User  
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny



class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key, 'user_type': user.type}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(phone_number=phone_number)
            except User.DoesNotExist:
                return Response({'error': 'Invalid phone number or password.'}, status=status.HTTP_401_UNAUTHORIZED)

            if user.check_password(password):
                token, _ = Token.objects.get_or_create(user=user)
                return Response({'token': token.key, 'user_type': user.type}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'Invalid phone number or password.'}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFarmerOrSupplier]

    def get_queryset(self):
        return Order.objects.filter(farmer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsSupplier]

    def get_queryset(self):
        return Product.objects.filter(supplier=self.request.user)

    def perform_create(self, serializer):
        serializer.save(supplier=self.request.user)


class OrderItemViewSet(viewsets.ModelViewSet):
    serializer_class = OrderItemSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFarmerOrSupplier]

    def get_queryset(self):
        return OrderItem.objects.filter(order__farmer=self.request.user)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return User.objects.all()


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsFarmer]

    def get_queryset(self):
        return Payment.objects.filter(farmer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(farmer=self.request.user)



class STKPushView(APIView):
    def post(self, request):
        serializer = STKPushSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            daraja = DarajaAPI()
            response = daraja.stk_push(
                phone_number=data['phone_number'],
                amount=data['amount'],
                account_reference=data['account_reference'],
                transaction_desc=data['transaction_desc']
            )

            checkout_request_id = response.get('CheckoutRequestID', None)

            
            order_id = data.get('order_id') 

            if checkout_request_id:
                payment = Payment.objects.create(
                    phone_number=data['phone_number'],
                    amount=data['amount'],
                    account_reference=data['account_reference'],
                    transaction_desc=data['transaction_desc'],
                    mpesa_checkout_id=checkout_request_id,
                    quantity=1,
                    payment_method="MPESA",
                    order_id=[order_id] if order_id else None,
                    amount_paid=data['amount'],
                )
                if User:
                    if User.role == 'farmer':
                        payment.farmer = User
                    payment.save()

            return Response(response)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['POST'])
def daraja_callback(request): 
    callback_data = request.data
    print("Daraja Callback Data:", callback_data)

    try:
        stk_callback = callback_data['Body']['stkCallback']
        checkout_request_id = stk_callback['CheckoutRequestID']
        result_code = stk_callback['ResultCode']
        result_desc = stk_callback['ResultDesc']
        payment = Payment.objects.get(mpesa_checkout_id=checkout_request_id)

        payment.result_code = str(result_code)
        payment.result_description = result_desc

        if result_code == 0:
            items = stk_callback.get('CallbackMetadata', {}).get('Item', [])
            item_dict = {item['Name']: item['Value'] for item in items}

            payment.mpesa_receipt_number = item_dict.get('MpesaReceiptNumber')
            trans_date_str = str(item_dict.get('TransactionDate'))
            trans_date = datetime.datetime.strptime(trans_date_str, '%Y%m%d%H%M%S')
            payment.transaction_date = timezone.make_aware(trans_date, timezone.get_current_timezone())

            payment.amount_from_callback = item_dict.get('Amount')
            payment.phone_number_from_callback = item_dict.get('PhoneNumber')
            payment.payment_status = 'Completed'
        else:
            payment.payment_status = 'Failed'

        payment.save()

    except Payment.DoesNotExist:
        print(f"Payment with CheckoutRequestID {checkout_request_id} not found.")
    except Exception as e:
        print(f"Error processing Daraja callback: {e}")
    return Response({"ResultCode": 0, "ResultDesc": "Accepted"})






