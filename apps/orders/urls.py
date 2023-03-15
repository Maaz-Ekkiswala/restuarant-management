from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.orders import views

order_router = DefaultRouter()

order_router.register("sessions", views.SessionViewSet, basename="sessions")
order_router.register("orders", views.OrderViewSet, basename="orders")

urlpatterns = [
    path('', include(order_router.urls))
]