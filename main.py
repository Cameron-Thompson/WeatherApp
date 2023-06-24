import requests 
import json
import xml
import mysql

forecastDict = ''

#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
response = requests.get(api_url)

try:
   if (response.headers.get('Content-Type').startswith('application/json')):
        forecastDict = response.json()
   else:
        raise Exception(TypeError('unsupported format, please use JSON only')) 
except TypeError as te:
     print("Error: " + te)


for x in forecastDict['daily']:
     print("printing x")
     print (x)

     tempDict = {
          "latitude": forecastDict['lat'],
          "longitude": forecastDict['lon'],
          "timestamp": x['dt'],
          "temperature": x['temp']['day'],
          "windspeed": x['wind_speed'],
          "wind_deg": x['wind_deg'],
          "precipitation_chance": x['pop'],
     }
     print(tempDict)

