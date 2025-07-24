from rest_framework import permissions
class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.type == 'Supplier'
        )
class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.type == 'farmer'
        )
from rest_framework import permissions

class IsFarmerOrSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        user = request.user
        return (
            user and
            user.is_authenticated and
            (user.type == 'farmer' or user.type == 'Supplier')  
        )
