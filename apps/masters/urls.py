from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.masters import views

master_router = DefaultRouter()

master_router.register("countries", views.CountryViewSet, basename="country")
master_router.register("cities", views.CityViewSet, basename="city")

urlpatterns = [
    path("", include(master_router.urls))
]