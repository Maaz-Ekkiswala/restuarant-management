from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from apps.restaurants.constants import RestaurantStatus
from apps.restaurants.models import Restaurant
from apps.users.constants import Role
from apps.users.models import UserRole, UserProfile

TEST_USER_EMAIL = "xxx@xxx.com"
TEST_USER_PASSWORD = "1234567890"
TEST_USER_FIRST_NAME = "Test"
TEST_USER_LAST_NAME = "User"


TEST_RESTAURANT_NAME = "test_restaurant"
TEST_RESTAURANT_CODE_POSTAL = "380000"
TEST_RESTAURANT_EMAIL_OR_PHONE = "restaurant@no.com"
TEST_RESTAURANT_SPECIALITY = "test_speciality"
TEST_RESTAURANT_HIGHLIGHT = True
TEST_RESTAURANT_OPENING_TIME = datetime.now()
TEST_RESTAURANT_CLOSING_TIME = datetime.now() + timedelta(hours=8)
TEST_RESTAURANT_STATUS = RestaurantStatus.OPEN
TEST_RESTAURANT_CODE_WIFI = "TEST@00"
TEST_RESTAURANT_PASSWORD = "test@123"


class RestaurantManagementTestCase(APITestCase):
    fixtures = ["country.json", "city.json"]

    @classmethod
    def setUpTestData(cls):
        super(RestaurantManagementTestCase, cls).setUpTestData()
        get_user_model().objects.create_user(
            username=TEST_USER_EMAIL,
            password=TEST_USER_PASSWORD,
            first_name=TEST_USER_FIRST_NAME,
            last_name=TEST_USER_LAST_NAME,
            is_active=True,
        )

        Restaurant.objects.create(
            name=TEST_RESTAURANT_NAME,
            city_id=2,
            country_id=1,
            code_postal=TEST_RESTAURANT_CODE_POSTAL,
            email_or_phone=TEST_RESTAURANT_EMAIL_OR_PHONE,
            speciality=TEST_RESTAURANT_SPECIALITY,
            highlight=TEST_RESTAURANT_HIGHLIGHT,
            opening_time=TEST_RESTAURANT_OPENING_TIME,
            closing_time=TEST_RESTAURANT_CLOSING_TIME,
            status=TEST_RESTAURANT_STATUS,
            code_wifi=TEST_RESTAURANT_CODE_WIFI
        )

        get_user_model().objects.create_user(
            username=TEST_RESTAURANT_EMAIL_OR_PHONE,
            password=TEST_RESTAURANT_PASSWORD
        )

    def setUp(self) -> None:
        super(RestaurantManagementTestCase, self).setUp()
        self.user = get_user_model().objects.filter(username=TEST_USER_EMAIL).first()
        UserRole.objects.create(user_id=self.user.id, role=Role.CUSTOMER)
        UserProfile.objects.create(user=self.user, email_or_phone=TEST_USER_EMAIL)
        self.restaurant = Restaurant.objects.filter(name=TEST_RESTAURANT_NAME).first()
        self.restaurant_user = get_user_model().objects.filter(
            username=TEST_RESTAURANT_EMAIL_OR_PHONE
        ).first()
        UserRole.objects.create(
            user_id=self.restaurant_user.id, role=Role.MANAGER, restaurant=self.restaurant
        )
        UserProfile.objects.create(
            user=self.restaurant_user, email_or_phone=TEST_RESTAURANT_EMAIL_OR_PHONE
        )
        user_token = RefreshToken.for_user(self.user)
        restaurant_user_token = RefreshToken.for_user(self.restaurant_user)
        user_access_key = str(user_token.access_token)
        restaurant_user_access_key = str(restaurant_user_token.access_token)
        self.authorized_user_client = APIClient(
            self.user, HTTP_AUTHORIZATION="Bearer " + user_access_key,
            content_type="application/json"
        )
        self.unauthorized_user_client = APIClient(
            self.user
        )
        self.authorized_restaurant_client = APIClient(
            self.restaurant_user, HTTP_AUTHORIZATION="Bearer " + restaurant_user_access_key,
            content_type="application/json"
        )
        self.unauthorized_restaurant_client = APIClient(
            self.restaurant_user
        )

