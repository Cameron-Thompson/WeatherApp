import database
from API import requestWeatherData
from helpers import (readInCSVFile, writeToArray)

#This is to show what data imported via csv would have to undergo to get written into our db
records = []
readInCSVFile(records)
jsonForecastDict = requestWeatherData()
writeToArray(jsonForecastDict, records)
#push records to the db 
connection, myCursor = database.connectToDB()
database.writeToDB(records, connection, myCursor)