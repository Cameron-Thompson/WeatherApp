def writeToArray(forecastDict, records):
    for dailyRecord in forecastDict['daily']:
         tempDict = {
          #write a temporary dictionary and then append to an array
          "latitude": forecastDict['lat'],
          "longitude": forecastDict['lon'],
          "timestamp": dailyRecord['dt'],
          "temperature": dailyRecord['temp']['day'],
          "windspeed": dailyRecord['wind_speed'],
          "wind_deg": dailyRecord['wind_deg'],
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
