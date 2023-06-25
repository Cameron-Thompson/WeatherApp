import datetime

def writeToArray(forecastDict, records):
    for dailyRecord in forecastDict['daily']:
         tempArr = [
          #write a temporary array and then append to an array
          forecastDict['lat'],
          forecastDict['lon'],
          convertTimestamp(dailyRecord['dt']),
          dailyRecord['temp']['day'],
          dailyRecord['wind_speed'],
          dailyRecord['wind_deg'],
          dailyRecord['pop'],
         ]
         records.append(tempArr)
    print(records[0])
    return records


def validateResponse(response):
    try:
       if (response.headers.get('Content-Type').startswith('application/json')):
            forecastDict = response.json()
       else:
            raise Exception(TypeError('unsupported format, please use JSON only')) 
    except TypeError as te:
         print("Error: " + te)
    return forecastDict



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


def convertTimestamp(timestamp):
     print(timestamp)
     dateTime = datetime.datetime.fromtimestamp(timestamp)
     print(dateTime)
     return dateTime