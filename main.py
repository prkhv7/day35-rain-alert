import requests

api_key = '3f2aa04b179e8f7deb9acc5c603a9085'

parameters = {'lat': 50.075539,
              'lon': 14.437800,
              'appid': api_key,
              'exclude': 'current,minutely,daily'
              }

response = requests.get(url='https://api.openweathermap.org/data/2.8/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]
will_rain = False

for hours in weather_slice:
    condition_code = hours['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print('Bring an umbrella.')
