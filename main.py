import requests 
import json
import xml
import pymysql

fileType = ''

#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
response = requests.get(api_url)

try:
   if (response.headers.get('content_type').startswith('application/json')):
        fileType = 'JSON'
   else:
        raise Exception(TypeError('unsupported format, please use JSON only')) 
except TypeError as te:
     print("Error: " + te)


def  getLatitude(JSON ) {

}

def getLongitude() {

}


def getUTCTime() {

}


def getTemperature() {

}

def getWindSpeed() {

}

def getWindDirection() {

}

def getPrecipitationChance() {

}