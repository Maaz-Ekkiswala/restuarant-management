from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.orders.models import Sessions, Order
from apps.orders.serializers import SessionSerializer, OrderSerializer
from restaurant_management.core.permissions import RestaurantPermission


# Create your views here.
class SessionViewSet(viewsets.ModelViewSet):
    serializer_class = SessionSerializer
    permission_classes = (IsAuthenticated, RestaurantPermission)

    def get_queryset(self):
        return Sessions.objects.filter(restaurant_id=self.kwargs.get('restaurant_id'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "restaurant_id": self.kwargs.get('restaurant_id'),
                "user": self.request.user.id
            }
        )
        return context


class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated, RestaurantPermission)

    def get_queryset(self):
        return Order.objects.filter(restaurant_id=self.kwargs.get('restaurant_id'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "restaurant_id": self.kwargs.get('restaurant_id'),
            }
        )
        return context