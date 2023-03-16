from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.menus import views

category_router = DefaultRouter()

category_router.register("categories", views.CategoryViewSet, basename="categories")
category_router.register("menus", views.MenuViewSet, basename="menus")

menu_router = DefaultRouter()
menu_router.register("", views.MenuCategoryViewSet, basename="menu_category")

urlpatterns = [
        path('', include(category_router.urls)),
        path("categories/<int:category_id>/menus/", include(menu_router.urls)),

]
