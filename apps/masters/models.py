from django.db import models

from restaurant_management.core.models import Base


# Create your models here.
class Country(Base):
    name = models.CharField(max_length=20, unique=True)
    country_code = models.CharField(max_length=5, unique=True)

    class Meta:
        unique_together = ("name", "country_code")


class City(Base):
    country_id = models.ForeignKey(to=Country, on_delete=models.CASCADE, related_name="country_cities")
    name = models.CharField(max_length=20, unique=True)

