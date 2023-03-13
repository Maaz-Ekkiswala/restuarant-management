from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.db import transaction
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.users.constants import Role
from apps.users.models import UserProfile, UserRole
from restaurant_management.core.serializers import BaseSerializer


class UserRoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserRole
        fields = ('user_id', "role", "restaurant_id")
        read_only_fields = ('restaurant_id',)


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True)
    user_role = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = get_user_model()
        fields = ('id', 'username', 'first_name', 'last_name', "user_role")
        read_only_fields = ("id",)

    def get_user_role(self, instance):
        user_role = UserRole.objects.filter(user_id=instance.id)
        return UserRoleSerializer(instance=user_role, many=True).data


class SignUpSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    email_or_phone = serializers.ReadOnlyField()

    class Meta:
        model = UserProfile
        fields = (
          "id",  'user', 'address', "email_or_phone"
        )
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def validate(self, attrs):
        validate_data = super().validate(attrs)
        username = self.context['username']
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
            user_instance = get_user_model().objects.create_user(
                username=self.context.get('username'),
                first_name=self.context.get('first_name'),
                last_name=self.context.get('last_name'),
                password=self.context.get('password')
            )
            user_profile = UserProfile.objects.create(
                user=user_instance,
                email_or_phone=self.context.get('username'),
                **validated_data
            )
            user_role = UserRole.objects.create(
                user=user_instance,
                role=Role.CUSTOMER
            )
        return user_profile


