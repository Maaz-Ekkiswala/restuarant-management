from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from apps.menus.models import Category, Menu
from apps.menus.serializers import CategorySerializer, MenuSerializer, MenuCategorySerializer
from restaurant_management.core.permissions import RestaurantPermission


# Create your views here.
class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, RestaurantPermission)

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
    permission_classes = (IsAuthenticated, RestaurantPermission)

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


class MenuCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = MenuCategorySerializer
    permission_classes = (IsAuthenticated, RestaurantPermission)

    def get_queryset(self):
        return Menu.objects.filter(
            restaurant_id=self.kwargs.get('restaurant_id'),
            category_id=self.kwargs.get('category_id')
        )

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update(
            {
                "restaurant_id": self.kwargs.get('restaurant_id'),
                "category_id": self.kwargs.get('category_id')
            }
        )
        return context