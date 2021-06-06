from django.db import models

#clasa in care mi-am creat modelul pentru prezicerile pentru vreme
#contine campurile esentiale si comportamentul datelor pe care le-am stocat de pe site-ul stormglass,in fisierul json, prin request-uri
#fiecare atribut din model reprezinta un camp in baza de date
class Weather(models.Model):

    windSpeed = models.FloatField(default=0)
    airTemperature = models.FloatField(default=0)
    pressure = models.FloatField(default=0)
    currentSpeed = models.FloatField(default=0)
    humidity = models.FloatField(default=0)
    iceCover = models.FloatField(default=0)
    precipitation = models.FloatField(default=0)
    seaLevel = models.FloatField(default=0)
    swellDirection = models.FloatField(default=0)
    swellHeight = models.FloatField(default=0)
    swellPeriod = models.FloatField(default=0)
    secondarySwellPeriod = models.FloatField(default=0)
    secondarySwellDirection = models.FloatField(default=0)
    secondarySwellHeight = models.FloatField(default=0)
    visibility = models.FloatField(default=0)
    waterTemperature = models.FloatField(default=0)
    waveDirection = models.FloatField(default=0)
    waveHeight = models.FloatField(default=0)
    wavePeriod = models.FloatField(default=0)
    windWaveDirection = models.FloatField(default=0)
    windWaveHeight = models.FloatField(default=0)

