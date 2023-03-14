from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.menus import views

category_router = DefaultRouter()

category_router.register("categories", views.CategoryViewSet, basename="categories")
category_router.register("menus", views.MenuViewSet, basename="menus")

urlpatterns = [
        path('', include(category_router.urls)),
]
