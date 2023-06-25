import csv
import datetime

#daily is a subset of the data from the api, it is an array of hashmaps 
#by looping over each element (each hashmap, each day's results in other words)
#We can extract the required data for each day, some data is fixed such as lat and lon 
#so we don't have to drill down into each element of the daily array for these.
def writeToArray(forecastDict, records):
    for dailyRecord in forecastDict['daily']:
         tempArr = [
          #write a temporary array and then append to an array for writing to the db
          forecastDict['lat'],
          forecastDict['lon'],
          convertTimestamp(dailyRecord['dt']),
          dailyRecord['temp']['day'],
          dailyRecord['wind_speed'],
          dailyRecord['wind_deg'],
          dailyRecord['pop'],
         ]
         records.append(tempArr)
    return records

#determine if the response is json 
def validateResponse(response):
    try:
       if (response.headers.get('Content-Type').startswith('application/json')):
            forecastDict = response.json()
       else:
            raise Exception(TypeError('unsupported format, please use JSON only')) 
    except TypeError as te:
         print("Error: " + te)
    return forecastDict


#ensure the database has been connected to sucessfully
def validateDatabaseConnection(connection):
    if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            print("You're connected to database: ", record)
    else:
            print("You are not connected to the database")
            quit()

#convert the timestamp into a datetime 
def convertTimestamp(timestamp):
     dateTime = datetime.datetime.fromtimestamp(timestamp)
     return dateTime

#read in a csvFile
def readInCSVFile(records):
    with open('exampleCSV.csv',mode='r') as CSVFile:
       csvReader = csv.reader(CSVFile)
   #skip the headers
       next(csvReader)
       csvData = next(csvReader)
       records.append(csvData)