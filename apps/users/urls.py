from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users import views

router = DefaultRouter()

router.register("signup", views.SignUpViewSet, basename="signup")


urlpatterns = [
        path('', include(router.urls)),
        path('login/', views.LoginViewSet.as_view(), name='token_obtain_pair'),
        path("refresh_token/", TokenRefreshView.as_view(), name="token_refresh"),
]