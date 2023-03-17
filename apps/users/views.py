import json
import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.response import Response

from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.serializers import SignUpSerializer, UserSerializer
from restaurant_management.core.facebook_auth import FaceBookAuthProvider
from restaurant_management.core.google_auth import GoogleAuthProvider

logger = logging.getLogger(__name__)


# Create your views here.
class SignUpViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin):
    serializer_class = SignUpSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        username = self.request.data.get('username')
        first_name = self.request.data.get('first_name')
        lastname = self.request.data.get('last_name')
        password = self.request.data.get('password')
        context.update({
            "username": username,
            "first_name": first_name,
            "last_name": lastname,
            "password": password,
        })
        return context


class LoginViewSet(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        response = None
        if username and password:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            response = dict(**serializer.validated_data)
            user = serializer.user
            response['user'] = UserSerializer(instance=user).data

        login_type = request.data.get('login_type')
        if login_type == "google":
            token = self.get_token_from_header(request)
            google_auth = GoogleAuthProvider(token=token)
            user_google_data = google_auth.get_decoded_data()
            user_instance, created = get_user_model().objects.get_or_create(
                username=user_google_data.get('email'),
                defaults={
                    "first_name": user_google_data.get('given_name'),
                    "last_name": user_google_data.get('family_name')
                }
            )
            response = RefreshToken.for_user(user_instance)
            response = {
                "access": str(response.access_token),
                "refresh": str(response),
                "user": UserSerializer(instance=user_instance).data
            }

        elif login_type == "facebook":
            token = self.get_token_from_header(request)
            facebook_auth = FaceBookAuthProvider(token=token)
            user_data = facebook_auth.get_user_info()
            user_instance, created = get_user_model().objects.get_or_create(
                username=user_data.get('email'),
                defaults={
                    "first_name": user_data.get('first_name'),
                    "last_name": user_data.get('last_name')
                }
            )
            response = RefreshToken.for_user(user_instance)
            response = {
                "access": str(response.access_token),
                "refresh": str(response),
                "user": UserSerializer(instance=user_instance).data
            }

        return Response(response, status=status.HTTP_200_OK)

    def get_token_from_header(self, request):
        token = request.headers.get("Authorization", "").split(" ", 1)
        if not token:
            return Response(
                {"message": "Token should be passed in headers to authenticate social login"},
                status=status.HTTP_400_BAD_REQUEST
            )
        if len(token) == 2:
            return token[1]
        return None


class UserViewSet(
    viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return get_user_model().objects.filter(pk=self.request.user.id)

    def perform_destroy(self, instance):
        instance.is_active = False
        instance.save()
