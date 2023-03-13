from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.restaurants import views

restaurant_router = DefaultRouter()

restaurant_router.register("signup", views.RestaurantSignUpViewSet, basename="signup")

urlpatterns = [
        path('', include(restaurant_router.urls)),
        path('login/', views.RestaurantLoginViewSet.as_view(), name='token_obtain_pair'),
        # path("refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
]