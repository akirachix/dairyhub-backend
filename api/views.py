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






