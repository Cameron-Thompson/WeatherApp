import requests 
import json
import xml
import mysql
from helpers import validateResponse, writeToDictionary

forecastDict = ''

#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
response = requests.get(api_url)
forecastDict = validateResponse(response)


records = []
writeToDictionary(forecastDict, records)

#push records to the db 


