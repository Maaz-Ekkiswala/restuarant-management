from rest_framework import viewsets, mixins

from apps.masters.models import Country, City
from apps.masters.serializers import CountrySerializer, CitySerializer


# Create your views here.
class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer

    def get_queryset(self):
        return Country.objects.all()


class CityViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.UpdateModelMixin):
    serializer_class = CitySerializer

    def get_queryset(self):
        return City.objects.all()