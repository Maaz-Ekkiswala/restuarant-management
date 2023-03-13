from apps.masters.models import City, Country
from apps.restaurants.constants import RestaurantStatus
from restaurant_management.core.models import Base
from django.db import models


# Create your models here.
class Restaurant(Base):
    name = models.CharField(max_length=50, verbose_name="restaurant_name")
    city_id = models.ForeignKey(to=City, on_delete=models.CASCADE, related_name="restuarant_city")
    country_id = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name="restaurant_country")
    code_postal = models.CharField(null=True, max_length=8)
    email_or_phone = models.CharField(max_length=100, null=True, unique=True)
    speciality = models.CharField(max_length=50, null=True)
    highlight = models.BooleanField(verbose_name="restaurant highlight")
    opening_time = models.TimeField(null=True)
    closing_time = models.TimeField(null=True)
    status = models.CharField(max_length=6, choices=RestaurantStatus.choices())
    code_wifi = models.CharField(null=True, max_length=30)