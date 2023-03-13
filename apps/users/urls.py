from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from apps.users import views

router = DefaultRouter()

router.register("signup", views.SignUpViewSet, basename="signup")
router.register("", views.UserViewSet, basename="users")


urlpatterns = [
        path('user-login/', views.LoginViewSet.as_view(), name='token_obtain_pair'),
        path("user-refresh-token/", TokenRefreshView.as_view(), name="token_refresh"),
        path('', include(router.urls)),
]