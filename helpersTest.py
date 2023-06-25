import json
import unittest
from numpy import testing

from helpers import validateResponse, writeToArray
class TestHelpers(unittest.TestCase):
    def runTest(self):
        response = {
        "lat": 54.5973,
        "lon": 5.9301,
        "timezone": "Europe/Berlin",
        "timezone_offset": 7200,
        "daily": [
        {
            "dt": 1687604400,
            "sunrise": 1687575623,
            "sunset": 1687637803,
            "moonrise": 1687598520,
            "moonset": 1687562580,
            "moon_phase": 0.19,
            "summary": "Expect a day of partly cloudy with clear spells",
            "temp": {
                "day": 290.45,
                "min": 289.62,
                "max": 290.87,
                "night": 290.6,
                "eve": 290.76,
                "morn": 290.4
            },
            "feels_like": {
                "day": 290.64,
                "night": 290.75,
                "eve": 290.95,
                "morn": 290.27
            },
            "pressure": 1023,
            "humidity": 92,
            "dew_point": 289.11,
            "wind_speed": 5.98,
            "wind_deg": 200,
            "wind_gust": 7.66,
            "weather": [
                {
                    "id": 803,
                    "main": "Clouds",
                    "description": "broken clouds",
                    "icon": "04d"
                }
            ],
            "clouds": 83,
            "pop": 0,
            "uvi": 6.91
        }
    ]
        }
        
        expectedArray = [{'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687604400, 'temperature': 290.45, 'windspeed': 5.98, 'wind_deg': 200, 'precipitation_chance': 0}]
        actualArray = []
        actualArray = writeToArray(response,actualArray)
        testing.assert_array_equal(expectedArray[0],actualArray[0])

        
if __name__ == '__main__':
    unittest.main()