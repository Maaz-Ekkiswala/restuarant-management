import json

from django.test import TestCase
from rest_framework import status

from restaurant_management.core.test_client import RestaurantManagementTestCase


# Create your tests here.
class UserTestCases(RestaurantManagementTestCase):

    def test_get_user(self):
        response = self.authorized_user_client.get(
            path=f"/api/v1/users/{self.user.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_user_with_invalid_url(self):
        response = self.authorized_user_client.get(
            path=f"/api/v1/users{self.user.id}"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_user_with_unauthorized_client(self):
        response = self.unauthorized_user_client.get(
            path=f"/api/v1/users/{self.user.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_user(self):
        data = {
            "first_name": "Resto",
            "last_name": "test"
        }
        response = self.authorized_restaurant_client.put(
            path=f"/api/v1/users/{self.restaurant_user.id}/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.json()['first_name'], "Resto")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_user_with_another_client(self):
        data = {
            "first_name": "Resto",
            "last_name": "test"
        }
        response = self.authorized_user_client.put(
            path=f"/api/v1/users/{self.restaurant_user.id}/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_with_invalid_id(self):
        data = {
            "first_name": "Resto",
            "last_name": "test"
        }
        response = self.authorized_restaurant_client.put(
            path=f"/api/v1/users/5/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_user_with_invalid_id(self):
        response = self.authorized_restaurant_client.delete(
            path=f"/api/v1/users/5/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_user(self):
        response = self.authorized_user_client.delete(
            path=f"/api/v1/users/{self.user.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)