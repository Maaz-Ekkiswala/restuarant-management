from rest_framework.permissions import BasePermission

from apps.users.models import UserRole


class RestaurantPermission(BasePermission):
    def has_permission(self, request, view):
        user_roles = UserRole.objects.filter(user=request.user).values_list('role', flat=True)
        return True if "manager" in user_roles else False


class CustomerPermission(BasePermission):
    def has_permission(self, request, view):
        user_roles = UserRole.objects.filter(user=request.user).values_list('role', flat=True)
        return True if "customer" in user_roles else False
