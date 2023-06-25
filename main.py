import datetime
import json
import xml
import xmltodict
import pprint
import mysql.connector
import requests
import csv

from helpers import readInCSVFile, validateDatabaseConnection, validateResponse, writeToArray
from PredictionTable import createTableString, insertTableString

#This is to show what data imported via csv would have to undergo to get written into our db
records = []
readInCSVFile(records)

#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
response = requests.get(api_url)
jsonForecastDict = validateResponse(response)

writeToArray(jsonForecastDict, records)

#push records to the db 
connection = mysql.connector.connect(host='localhost', user='root',passwd='root', database = 'weatherdb')
validateDatabaseConnection(connection)
myCursor = connection.cursor()
myCursor.execute(createTableString)
try:
   #executemany designed to take arrays, not an array of hashes. that would require special formatting
   myCursor.executemany(insertTableString,records)
   connection.commit()
except:
   connection.rollback()