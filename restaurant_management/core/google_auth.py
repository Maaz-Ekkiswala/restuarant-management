from rest_framework.serializers import ValidationError
from google.auth.transport import requests
from google.oauth2 import id_token

from restaurant_management import settings


class GoogleAuthProvider:
    def __init__(self, token):
        self.token = token

    def validate_token(self):
        response = id_token.verify_oauth2_token(
            self.token, requests.Request(),
            audience=[settings.GOOGLE_CLIENT_ID]
        )
        response['google_token'] = self.token
        if not response['email'] or not response['email_verified']:
            raise ValidationError("User not verified")
        return response

    def get_decoded_data(self):
        try:
            user_info = self.validate_token()
        except Exception as ex:
            error = {"message": f"Google token invalid or '{ex}'"}
            raise ValidationError(error)
        else:
            return user_info