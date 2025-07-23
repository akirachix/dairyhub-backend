from rest_framework import permissions
class IsSupplier(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.type == 'supplier'
        )
class IsFarmer(permissions.BasePermission):
    def has_permission(self, request, view):
        return (
            request.user and
            request.user.is_authenticated and
            request.user.type == 'farmer'
        )
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            obj.user == request.user or
            request.method in permissions.SAFE_METHODS
        )