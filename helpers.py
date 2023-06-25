import datetime

def writeToArray(forecastDict, records):
    for dailyRecord in forecastDict['daily']:
         tempDict = {
          #write a temporary dictionary and then append to an array
          "latitude": forecastDict['lat'],
          "longitude": forecastDict['lon'],
          "time_of_Prediction": datetime.datetime.fromtimestamp(dailyRecord['dt']),
          "temperature": dailyRecord['temp']['day'],
          "wind_speed": dailyRecord['wind_speed'],
          "wind_direction": dailyRecord['wind_deg'],
          "precipitation_chance": dailyRecord['pop'],
     }
         records.append(tempDict)
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