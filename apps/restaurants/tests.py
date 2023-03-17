import json
from datetime import datetime, timedelta

from rest_framework import status

from restaurant_management.core.test_client import RestaurantManagementTestCase


# Create your tests here.
class RestaurantTestCases(RestaurantManagementTestCase):

    def test_get_restaurant(self):
        response = self.authorized_restaurant_client.get(
            path=f"/api/v1/restaurants/{self.restaurant.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_restaurant_with_invalid_url(self):
        response = self.authorized_restaurant_client.get(
            path=f"/api/v1/restaurants{self.restaurant.id}"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_restaurant_with_unauthorized_client(self):
        response = self.unauthorized_restaurant_client.get(
            path=f"/api/v1/restaurants/{self.restaurant.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_restaurant(self):
        data = {
            "name": "Resto",
            "city_id": 3,
            "code_postal": "35200",
            "country_id": 2,
            "code_wifi": "pt@123",
            "opening_time": str(datetime.now().time()),
            "closing_time": str((datetime.now() + timedelta(hours=8)).time()),
            "speciality": "restaurant_speciality",
            "highlight": True,
            "status": "open"
        }
        response = self.authorized_restaurant_client.put(
            path=f"/api/v1/restaurants/{self.restaurant.id}/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.json()['name'], "Resto")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_restaurant_with_invalid_id(self):
        data = {
            "name": "Resto",
            "city_id": 3,
            "code_postal": "35200",
            "country_id": 2,
            "code_wifi": "pt@123",
            "opening_time": str(datetime.now().time()),
            "closing_time": str((datetime.now() + timedelta(hours=8)).time()),
            "speciality": "restaurant_speciality",
            "highlight": True,
            "status": "open"
        }
        response = self.authorized_restaurant_client.put(
            path=f"/api/v1/restaurants/10/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_restaurant_with_unauthorized_user(self):
        data = {
            "name": "Resto",
            "city_id": 3,
            "code_postal": "35200",
            "country_id": 2,
            "code_wifi": "pt@123",
            "opening_time": str(datetime.now().time()),
            "closing_time": str((datetime.now() + timedelta(hours=8)).time()),
            "speciality": "restaurant_speciality",
            "highlight": True,
            "status": "open"
        }
        response = self.unauthorized_restaurant_client.put(
            path=f"/api/v1/restaurants/{self.restaurant.id}/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_restaurant_with_invalid_data(self):
        data = {
            "city_id": 3,
            "code_postal": "35200",
            "country_id": 2,
            "code_wifi": "pt@123",
            "speciality": "restaurant_speciality",
            "highlight": True,
            "status": "open"
        }
        response = self.authorized_restaurant_client.put(
            path=f"/api/v1/restaurants/{self.restaurant.id}/",
            data=json.dumps(data), content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_restaurant_with_unauthorized_client(self):
        response = self.unauthorized_restaurant_client.delete(
            path=f"/api/v1/restaurants/{self.restaurant.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_restaurant_with_invalid_id(self):
        response = self.authorized_restaurant_client.delete(
            path=f"/api/v1/restaurants/5/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_restaurant(self):
        response = self.authorized_restaurant_client.delete(
            path=f"/api/v1/restaurants/{self.restaurant.id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

