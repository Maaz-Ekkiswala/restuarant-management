import requests
from django.core.exceptions import ValidationError


class FaceBookAuthProvider:
    def __init__(self, token):
        self.token = token

    def validate_token(self):
        with requests.get(
                url="https://graph.facebook.com/me",
                params=dict(
                    fields=",".join(["id", "first_name", "last_name", "email"]),
                    access_token=self.token
                )
        ) as response:
            return response.json()

    def get_user_info(self):
        try:
            user_info = self.validate_token()
        except Exception as ex:
            error = {"message": f"Facebook token invalid or '{ex}'"}
            raise ValidationError(error)
        else:
            return user_info