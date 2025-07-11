from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from.views import OrderViewSet
from django.urls import path ,include

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
    path("",include(router.urls)),
    ]






