from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import serializers

from apps.restaurants.models import Restaurant
from apps.users.constants import Role
from apps.users.models import UserProfile, UserRole


class RestaurantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Restaurant
        fields = (
            "id", "name", "city_id", "country_id", "code_postal", "email_or_phone", "speciality",
            "highlight", "opening_time", "closing_time", "status", "code_wifi"
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        validate_data = super().validate(attrs)
        username = self.context['email_or_phone']
        if username:
            try:
                if get_user_model().objects.get(username=username):
                    raise serializers.ValidationError(
                        {"error": "Username with this username already exists."})
            except ObjectDoesNotExist:
                pass
        return validate_data

    def create(self, validated_data):
        with transaction.atomic():
            restaurant_instance = Restaurant.objects.create(
                **validated_data
            )
            user_instance = get_user_model().objects.create_user(
                username=self.context.get('email_or_phone'),
                password=self.context.get('password')
            )
            user_profile = UserProfile.objects.create(
                user=user_instance,
                email_or_phone=self.context.get('email_or_phone'),
            )
            user_role = UserRole.objects.create(
                user=user_instance,
                role=Role.MANAGER,
                restaurant=restaurant_instance
            )
        return restaurant_instance
