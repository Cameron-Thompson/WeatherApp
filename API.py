#get the overall daily predictions for the next days, exclude current , minutely and hourly from the response

def requestWeatherData():
    api_url = "https://api.openweathermap.org/data/3.0/onecall?lat=54.5973&lon=5.9301&exclude=minutely,hourly,current&appid=cf6e18bcfba8040fd3d0bef6a12975af"
    response = requests.get(api_url)
    jsonForecastDict = validateResponse(response)
    return jsonForecastDict