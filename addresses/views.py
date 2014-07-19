from rest_framework import viewsets
from addresses.models import Province, City
from addresses.serializers import ProvinceSerializer, CitySerializer


class ProvinceViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer


class CityViewSet(viewsets.ModelViewSet):
    """
    API endpoint
    """
    queryset = City.objects.all()
    serializer_class = CitySerializer
