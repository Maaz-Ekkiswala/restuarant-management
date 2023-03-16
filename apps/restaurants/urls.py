from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.restaurants import views

restaurant_router = DefaultRouter()

restaurant_router.register("signup", views.RestaurantSignUpViewSet, basename="signup")
restaurant_router.register("", views.RestaurantViewSet, basename="restaurant")

urlpatterns = [
        path('restaurant-login/', views.RestaurantLoginViewSet.as_view(), name='token_obtain_pair'),
        path("restaurant-refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
        path('', include(restaurant_router.urls)),
]