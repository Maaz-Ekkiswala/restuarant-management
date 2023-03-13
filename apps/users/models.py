from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.db import models

from apps.restaurants.models import Restaurant
from apps.users.constants import Role
from restaurant_management.core.models import Base


# Create your models here.
class UserProfile(Base):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="user_profile")
    address = models.TextField(verbose_name="address", null=True, blank=True)
    email_or_phone = models.CharField(max_length=100)

    USERNAME_FIELD = 'email_or_phone'



class UserRole(Base):
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE, related_name="user_role")
    role = models.CharField(choices=Role.choices(), max_length=10)
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE, null=True, blank=True)