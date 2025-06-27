
from django.urls import path ,include

from rest_framework.routers import DefaultRouter

from .views import ProductViewSet

from .views import OrderItemViewSet
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet

from django.urls import path ,include
from rest_framework.routers import DefaultRouter
from .views import PaymentViewSet

router=DefaultRouter()

router.register(r"products",ProductViewSet,basename="products")
urlpatterns=[path("",include(router.urls)),]

router.register(r"orderItems",OrderItemViewSet,basename="orderItems")
urlpatterns=[path("",include(router.urls)),]




router = DefaultRouter()
router.register(r"users", UserViewSet, basename = "users")
urlpatterns = [
    path("",include(router.urls)),

]

router=DefaultRouter()
router.register(r"payment",PaymentViewSet,basename="payment")
urlpatterns=[path("",include(router.urls)),]
