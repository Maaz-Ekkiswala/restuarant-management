import logging

from django.contrib.auth import get_user_model
from rest_framework import mixins, viewsets, status
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.constants import Role
from apps.users.models import UserProfile, UserRole
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
        token = self.request.stream.headers.get("Authorization").split(" ", 1)
        if request.data.get("username") and request.data.get("password"):
            serializer = self.get_serializer(data=request.data)
            try:
                serializer.is_valid(raise_exception=True)
                response = dict(**serializer.validated_data)
                user = serializer.user
                response['user'] = UserSerializer(instance=user).data
                return Response(response, status=status.HTTP_200_OK)
            except TokenError as e:
                raise InvalidToken(e.args[0])
            except AuthenticationFailed as ex:
                logger.error(
                    "Login Failed for user: %s. %s", request.data.get('username'), str(ex)
                )
                return Response(
                    {"message": "Login Failed."},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        elif request.data.get('login_type') == "google":
            if not token:
                return Response(
                    {"message": "The token should be passed in headers to authenticate with google"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            google_auth = GoogleAuthProvider(token=token[-1])
            user_data = google_auth.get_decoded_data()
            user_instance = get_user_model().objects.filter(
                username=user_data.get('email')
            ).first()
            user_payload = {
                "first_name": user_data.get('given_name'),
                "last_name": user_data.get('family_name')
            }
        elif request.data.get('login_type') == "facebook":
            if not token:
                return Response(
                    {"message": "The token should be passed in headers to authenticate with facebook"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            facebook_auth = FaceBookAuthProvider(token=token[-1])
            user_data = facebook_auth.get_user_info()
            user_instance = get_user_model().objects.filter(
                username=user_data.get('email')
            ).first()
            user_payload = {
                "first_name": user_data.get('first_name'),
                "last_name": user_data.get('last_name')
            }
        if not user_instance.exists():
            # user_instance = get_user_model().objects.create(
            #     username=user_data.get('email'),
            #     ** user_payload
            # )
            user_profile_instance = UserProfile.objects.create(
                user=user_instance,
                email_or_phone=user_instance.username
            )
            user_role = UserRole.objects.create(
                user=user_instance,
                role=Role.CUSTOMER
            )
        return Response(
                None
        )