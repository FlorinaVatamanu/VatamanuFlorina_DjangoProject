from rest_framework import serializers
from .models import Weather

class WeatherSerializers(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ('windSpeed','airTemperature','pressure','currentSpeed',
                'humidity','iceCover','precipitation','seaLevel','swellDirection',
                'swellHeight','swellPeriod','secondarySwellPeriod','secondarySwellDirection',
                'secondarySwellHeight','visibility','waterTemperature','waveDirection',
                 'waveHeight','wavePeriod','windWaveDirection','windWaveHeight')
