from django.db import models

from apps.restaurants.models import Restaurant
from restaurant_management.core.models import Base


# Create your models here.
class Category(Base):
    name = models.CharField(max_length=50, verbose_name="category name")
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("restaurant", "name")


class Menu(Base):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE)
    picture_address = models.CharField(max_length=200, verbose_name="image_url")
    name = models.CharField(max_length=100, verbose_name="menu_item_name")
    price = models.FloatField(verbose_name="item price")
    available = models.BooleanField(verbose_name="item availability")
    highlight = models.BooleanField(verbose_name="item highlight")
    rating = models.FloatField(verbose_name="item rating")
    options = models.JSONField(verbose_name="items options")

    class Meta:
        unique_together = ("restaurant", "name")