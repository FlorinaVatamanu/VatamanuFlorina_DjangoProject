from pprint import pprint
from rest_framework.generics import ListAPIView
from proiectSI.models import Weather
from .serializers import WeatherSerializers
from .date import getData,adauga_date_vreme
#am incercat niste metode cu import pickle, dar  nu am reusit

class WeatherListView(ListAPIView):
    queryset = Weather.objects.all()
    #queryset = adauga_date_vreme()
    serializer_class = WeatherSerializers
    pprint(getData())














