import arrow
import requests
from proiectSI.models import Weather


start = arrow.now().floor('day')

# Get last hour of today
end = arrow.now().ceil('day')
#clasa cu ajutorul careia imi iau datele necesare de pe stormglass, in campurile declarate in model
#request-ul HTTP returneaza un obiect cu toate datele din campurile mentionate
#metoda response = requests.get trimite un GET request la URL-ul specificat

response = requests.get(
    'https://api.stormglass.io/v2/weather/point',
    params={
        'lat': 58.7984,
        'lng': 17.8081,
        'params': ','.join(['windSpeed', 'airTemperature', 'pressure', 'currentSpeed',
                            'humidity', 'iceCover', 'precipitation', 'seaLevel', 'swellDirection',
                            'swellHeight', 'swellPeriod', 'secondarySwellPeriod', 'secondarySwellDirection',
                            'secondarySwellHeight', 'visibility', 'waterTemperature', 'waveDirection',
                            'waveHeight', 'wavePeriod', 'windWaveDirection', 'windWaveHeight']),
        'source': 'sg'
        # 'start': start.to('UTC').timestamp,  # Convert to UTC timestamp
        # 'end': end.to('UTC').timestamp  # Convert to UTC timestamp
    },
    headers={
        'Authorization': 'e490778c-c03d-11eb-80d0-0242ac130002-e4907854-c03d-11eb-80d0-0242ac130002'
    }
)

#datele extrase de pe site vor fi adaugate intr-un fisier json

json_data = response.json()
print(json_data)

def getData():
    return json_data
#cu aceasta metoda adaug datele din fisierul json in baza de date
#parcurg datele din fisierul json
def adauga_date_vreme():
    for data in json_data["hours"]:
        windSpeed = data['windSpeed']['sg'],
        airTemperature = data['airTemperature']['sg'],
        pressure = data['pressure']['sg'],
        currentSpeed = data['currentSpeed']['sg'],
        humidity = data['humidity']['sg'],
       # iceCover = data['iceCover']['sg'],
        precipitation = data['precipitation']['sg'],
        seaLevel = data['seaLevel']['sg'],
        swellDirection = data['swellDirection']['sg'],
        swellHeight = data['swellHeight']['sg'],
        swellPeriod = data['swellPeriod']['sg'],
        secondarySwellPeriod = data['secondarySwellPeriod']['sg'],
        secondarySwellDirection = data['secondarySwellDirection']['sg'],
        secondarySwellHeight = data['secondarySwellHeight']['sg'],
        visibility = data['visibility']['sg'],
        waterTemperature = data['waterTemperature']['sg'],
        waveDirection = data['waveDirection']['sg'],
        waveHeight = data['waveHeight']['sg'],
        wavePeriod = data['wavePeriod']['sg'],
        windWaveDirection = data['windWaveDirection']['sg'],
        windWaveHeight = data['windWaveHeight']['sg']

        weather = Weather(windSpeed,airTemperature,pressure,currentSpeed,
                humidity,precipitation,seaLevel,swellDirection,
                swellHeight,swellPeriod,secondarySwellPeriod,secondarySwellDirection,
                secondarySwellHeight,visibility,waterTemperature,waveDirection,
                waveHeight,wavePeriod,windWaveDirection,windWaveHeight)
        #salvez datele
        weather.save()
        #metoda .all() returneaza un queryset cu toate obiectele din baza de date

        return Weather.objects.all()
