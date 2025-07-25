from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import OrderViewSet
from django.urls import path ,include
from .views import RegisterUserView, LoginUserView
from rest_framework.authtoken.views import obtain_auth_token
from .views import PaymentViewSet, STKPushView, daraja_callback

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

from .views import OrderItemViewSet
from .views import UserViewSet
from .views import PaymentViewSet

router=DefaultRouter()
router.register(r"Orders" ,OrderViewSet,basename="Orders")
router.register(r"products",ProductViewSet,basename="products")
router.register(r"orderItems",OrderItemViewSet,basename="orderItems")
router.register(r"users", UserViewSet, basename = "users")
router.register(r"payment",PaymentViewSet,basename="payment")

urlpatterns=[
  path("api/",include(router.urls)),
  path('daraja/stk-push/', STKPushView.as_view(), name='daraja-stk-push'),
  path('daraja/callback/', daraja_callback, name='daraja-callback'),
  path('api/register/', RegisterUserView.as_view(), name='register'),
  path('api/login/', LoginUserView.as_view(), name='login'),
  path('api/api-token-auth/', obtain_auth_token, name='api_token_auth')
]


    





