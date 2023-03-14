from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.menus.models import Category, Menu
from apps.menus.serializers import CategorySerializer, MenuSerializer


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Category.objects.filter(restaurant_id=self.kwargs.get('restaurant_id'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "restaurant_id": self.kwargs.get('restaurant_id')
            }
        )
        return context


class MenuViewSet(viewsets.ModelViewSet):
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)


    def get_queryset(self):
        return Menu.objects.filter(restaurant_id=self.kwargs.get('restaurant_id'))

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "restaurant_id": self.kwargs.get('restaurant_id')
            }
        )
        return context