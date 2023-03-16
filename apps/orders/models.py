from datetime import datetime, timedelta

from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

from apps.menus.models import Menu
from apps.orders.constants import SessionStatus, OrderStatus
from apps.restaurants.models import Restaurant
from restaurant_management import settings
from restaurant_management.core.models import Base


def later_hours():
    return datetime.utcnow() + timezone.timedelta(hours=settings.DEFAULT_SESSION_END_HOURS)


# Create your models here.
class Sessions(Base):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now_add=True)
    end_at = models.DateTimeField(default=later_hours, editable=True)
    table_number = models.IntegerField(verbose_name="session_table")
    user = models.ForeignKey(to=get_user_model(), on_delete=models.CASCADE)
    status = models.CharField(
        choices=SessionStatus.choices(), verbose_name="session status", max_length=30,
        default=SessionStatus.ACTIVE
    )

    class Meta:
        db_table = "session"

    @staticmethod
    def is_valid_end_at(started_at, end_at):
        return False if started_at.time() > end_at.time() else True


class Order(Base):
    restaurant = models.ForeignKey(to=Restaurant, on_delete=models.CASCADE)
    option_chosen = models.BooleanField(verbose_name="option_chosen")
    options = models.JSONField(verbose_name="order_option")
    table_number = models.IntegerField(verbose_name="table number")
    menu = models.ForeignKey(to=Menu, on_delete=models.CASCADE)
    session = models.ForeignKey(to=Sessions, on_delete=models.CASCADE)
    status = models.CharField(
        choices=OrderStatus.choices(), verbose_name="order status", max_length=30,
        default=OrderStatus.OPEN
    )

    class Meta:
        db_table = "order"
