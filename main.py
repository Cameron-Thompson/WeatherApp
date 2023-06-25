from mysqlx import Error
import requests 
import json
import xml
import mysql.connector 
from helpers import validateResponse, writeToArray


forecastDict = ''

#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response
api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
response = requests.get(api_url)
forecastDict = validateResponse(response)


records = []
writeToArray(forecastDict, records)
print (records)

#push records to the db 

connection = mysql.connector.connect(host='localhost',
                                         user='root',passwd='root')
if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

