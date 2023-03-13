from django.shortcuts import render
from rest_framework import viewsets, mixins

from apps.restaurants.serializers import RestaurantSerializer


# Create your views here.
class RestaurantSignUpViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = RestaurantSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        email_or_phone = self.request.data.get('email_or_phone')
        password = self.request.data.get('password')
        context.update({
            "email_or_phone": email_or_phone,
            "password": password,
        })
        return context