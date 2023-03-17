import json

from django.test import TestCase
from rest_framework import status

from restaurant_management.core.test_client import RestaurantManagementTestCase


# Create your tests here.
class MasterTestCases(RestaurantManagementTestCase):

    def test_create_country(self):
        data = {
            "name": "London",
            "country_code": "+90"
        }
        response = self.unauthorized_user_client.post(
            data=json.dumps(data), content_type="application/json",
            path="/api/v1/masters/countries/"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_country_with_invalid_data(self):
        data = {
            "country_code": "+90"
        }
        response = self.unauthorized_user_client.post(
            data=json.dumps(data), content_type="application/json",
            path="/api/v1/masters/countries/"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_country_with_invalid_url(self):
        data = {
            "name": "London",
            "country_code": "+90"
        }
        response = self.unauthorized_user_client.post(
            data=json.dumps(data), content_type="application/json",
            path="/api/v1/masters/"
        )
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_get_country(self):
        response = self.unauthorized_user_client.get(
            path="/api/v1/masters/countries/3/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        return response.json()['id']

    def test_get_country_with_invalid_id(self):
        response = self.unauthorized_user_client.get(
            path="/api/v1/masters/countries/10/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_country_list(self):
        response = self.unauthorized_user_client.get(
            path="/api/v1/masters/countries/"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_country_list_with_invalid_url(self):
        response = self.unauthorized_user_client.get(
            path="/api/v1/masters/countries"
        )
        self.assertEqual(response.status_code, status.HTTP_301_MOVED_PERMANENTLY)

    def test_update_country(self):
        data = {
            "name": "NewYork",
            "country_code": "+90"
        }
        response = self.unauthorized_user_client.put(
            path="/api/v1/masters/countries/3/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_country_with_same_name(self):
        data = {
            "name": "India",
            "country_code": "+90"
        }
        response = self.unauthorized_user_client.put(
            path="/api/v1/masters/countries/3/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_country_with_same_code(self):
        data = {
            "name": "NewYork",
            "country_code": "+91"
        }
        response = self.unauthorized_user_client.put(
            path="/api/v1/masters/countries/3/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_delete_country_with_invalid_id(self):
        response = self.unauthorized_user_client.delete(
            path=f"/api/v1/masters/countries/10/"
        )
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_delete_country(self):
        country_id = self.test_get_country()
        response = self.unauthorized_user_client.delete(
            path=f"/api/v1/masters/countries/{country_id}/"
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_create_city(self):
        data = {
            "name": "Venice",
            "country": 2
        }
        response = self.unauthorized_user_client.post(
            path="/api/v1/masters/cities/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_cities_with_invalid_data(self):
        data = {
            "country": 2
        }
        response = self.unauthorized_user_client.post(
            path="/api/v1/masters/cities/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_cities_with_invalid_id(self):
        data = {
            "name": "Kenya",
            "country": 10
        }
        response = self.unauthorized_user_client.post(
            path="/api/v1/masters/cities/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_update_city(self):
        data = {
            "name": "Kenya",
            "country": 2
        }
        response = self.unauthorized_user_client.put(
            path="/api/v1/masters/cities/4/", data=json.dumps(data),
            content_type="application/json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)