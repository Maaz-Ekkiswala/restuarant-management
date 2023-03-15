from rest_framework.exceptions import ValidationError

from apps.menus.models import Menu
from apps.orders.models import Order, Sessions
from apps.users.serializers import UserSerializer
from restaurant_management.core.serializers import BaseSerializer


class SessionSerializer(BaseSerializer):
    user = UserSerializer(required=False)

    class Meta:
        model = Sessions
        fields = (
            "id", "table_number", "started_at", "end_at", "status", "user", "restaurant_id"
        )
        read_only_fields = ("id", "started_at", "user", "restaurant_id")

    def create(self, validated_data):
        session = Sessions.objects.create(
            restaurant_id=self.context.get('restaurant_id'),
            user_id=self.context.get("user"),
            **validated_data
        )
        return session

    def update(self, instance, validated_data):
        if Sessions.is_valid_end_at(
                end_at=validated_data.get('end_at'), started_at=instance.started_at
        ):
            session = super().update(instance, validated_data)
            return session
        else:
            raise ValidationError({"message": "Time for end_at is not valid"})


class OrderSerializer(BaseSerializer):

    class Meta:
        model = Order
        fields = (
            "id", "restaurant", "option_chosen", "options", "table_number", "menu_id",
            "session_id", "status"
        )
        read_only_fields = ("id", "restaurant")

    def create(self, validated_data):
        menu = Menu.objects.get(id=self.initial_data.get('menu_id'))
        if menu and Menu.is_valid_options(menu=menu, options=validated_data.get('options')):
            order = Order.objects.create(
                restaurant_id=self.context.get('restaurant_id'),
                menu_id=self.initial_data.get('menu_id'),
                session_id=self.initial_data.get('session_id'),
                **validated_data
            )
            return order
        else:
            raise ValidationError({"message": "Options are not valid"})
