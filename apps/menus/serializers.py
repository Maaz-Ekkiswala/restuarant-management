from apps.menus.models import Category, Menu
from restaurant_management.core.serializers import BaseSerializer


class CategorySerializer(BaseSerializer):

    class Meta:
        model = Category
        fields = ("id", "name", "restaurant_id")
        read_only_field = ("id", "restaurant_id")

    def create(self, validated_data):
        category = Category.objects.create(
            restaurant_id=self.context.get('restaurant_id'),
            **validated_data
        )
        return category


class MenuSerializer(BaseSerializer):

    class Meta:
        model = Menu
        fields = (
            "id", "name", "restaurant_id", "highlight", "category",
            "picture_address", "price", "available", "rating", "options"
        )
        read_only_fields = ("id", "restaurant_id")

    def create(self, validated_data):
        menu = Menu.objects.create(
            restaurant_id=self.context.get('restaurant_id'),
            **validated_data
        )
        return menu