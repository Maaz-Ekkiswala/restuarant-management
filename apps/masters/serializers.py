from rest_framework import serializers

from apps.masters.models import Country, City


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ("id", "name", "country")
        read_only_fields = ("id",)


class CountrySerializer(serializers.ModelSerializer):
    country_cities = CitySerializer(many=True, read_only=True)

    class Meta:
        model = Country
        fields = ("id", "name", "country_code", "country_cities")
        read_only_fields = ("id", "country_cities")

    def validate(self, attrs):
        name = attrs.get('name')
        country_code = attrs.get('country_code')
        if not name[0].isupper() and not country_code.startswith("+"):
            attrs['name'] = name.capitalize()
            attrs['country_code'] = "+" + country_code
        validate_data = super().validate(attrs)
        return validate_data
