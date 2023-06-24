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
        },
        {
            "dt": 1687690800,
            "sunrise": 1687662046,
            "sunset": 1687724205,
            "moonrise": 1687689360,
            "moonset": 1687649460,
            "moon_phase": 0.22,
            "summary": "Expect a day of partly cloudy with clear spells",
            "temp": {
                "day": 291.08,
                "min": 290.57,
                "max": 292.27,
                "night": 292.2,
                "eve": 292.17,
                "morn": 290.67
            },
            "feels_like": {
                "day": 291.17,
                "night": 292.43,
                "eve": 292.43,
                "morn": 290.8
            },
            "pressure": 1018,
            "humidity": 86,
            "dew_point": 288.64,
            "wind_speed": 7.12,
            "wind_deg": 145,
            "wind_gust": 10.73,
            "weather": [
                {
                    "id": 801,
                    "main": "Clouds",
                    "description": "few clouds",
                    "icon": "02d"
                }
            ],
            "clouds": 14,
            "pop": 0,
            "uvi": 7.33
        },
        {
            "dt": 1687777200,
            "sunrise": 1687748472,
            "sunset": 1687810602,
            "moonrise": 1687780260,
            "moonset": 1687736340,
            "moon_phase": 0.25,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 289.3,
                "min": 288.83,
                "max": 292.28,
                "night": 288.88,
                "eve": 288.88,
                "morn": 289.25
            },
            "feels_like": {
                "day": 289.09,
                "night": 288.39,
                "eve": 288.41,
                "morn": 289.34
            },
            "pressure": 1015,
            "humidity": 81,
            "dew_point": 286.1,
            "wind_speed": 10.87,
            "wind_deg": 300,
            "wind_gust": 12.5,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 40,
            "pop": 0.93,
            "rain": 2.31,
            "uvi": 6.27
        },
        {
            "dt": 1687863600,
            "sunrise": 1687834902,
            "sunset": 1687896996,
            "moonrise": 1687871220,
            "moonset": 1687823160,
            "moon_phase": 0.28,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 289.08,
                "min": 288.8,
                "max": 289.29,
                "night": 288.9,
                "eve": 288.8,
                "morn": 289.28
            },
            "feels_like": {
                "day": 288.77,
                "night": 288.57,
                "eve": 288.41,
                "morn": 288.75
            },
            "pressure": 1017,
            "humidity": 78,
            "dew_point": 285.27,
            "wind_speed": 8.07,
            "wind_deg": 276,
            "wind_gust": 9.78,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 1,
            "pop": 0.49,
            "rain": 0.12,
            "uvi": 6.43
        },
        {
            "dt": 1687950000,
            "sunrise": 1687921335,
            "sunset": 1687983386,
            "moonrise": 1687962480,
            "moonset": 1687910040,
            "moon_phase": 0.32,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 289.83,
                "min": 288.36,
                "max": 290.15,
                "night": 289.65,
                "eve": 289.57,
                "morn": 290.15
            },
            "feels_like": {
                "day": 289.98,
                "night": 289.76,
                "eve": 289.7,
                "morn": 290.31
            },
            "pressure": 1012,
            "humidity": 93,
            "dew_point": 288.76,
            "wind_speed": 8.09,
            "wind_deg": 236,
            "wind_gust": 9.52,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 96,
            "pop": 0.93,
            "rain": 2.65,
            "uvi": 6.17
        },
        {
            "dt": 1688036400,
            "sunrise": 1688007772,
            "sunset": 1688069772,
            "moonrise": 1688054040,
            "moonset": 1687996980,
            "moon_phase": 0.35,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 289.74,
                "min": 288.99,
                "max": 290.67,
                "night": 289.28,
                "eve": 288.99,
                "morn": 290.67
            },
            "feels_like": {
                "day": 289.67,
                "night": 289.01,
                "eve": 288.74,
                "morn": 290.75
            },
            "pressure": 1008,
            "humidity": 85,
            "dew_point": 287.24,
            "wind_speed": 9.05,
            "wind_deg": 207,
            "wind_gust": 12.28,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 100,
            "pop": 1,
            "rain": 5.37,
            "uvi": 7
        },
        {
            "dt": 1688122800,
            "sunrise": 1688094211,
            "sunset": 1688156155,
            "moonrise": 1688145840,
            "moonset": 1688084220,
            "moon_phase": 0.39,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 288.69,
                "min": 288.53,
                "max": 289.82,
                "night": 289.28,
                "eve": 288.77,
                "morn": 289.35
            },
            "feels_like": {
                "day": 288.36,
                "night": 288.72,
                "eve": 288.24,
                "morn": 288.93
            },
            "pressure": 1006,
            "humidity": 79,
            "dew_point": 285.12,
            "wind_speed": 11,
            "wind_deg": 245,
            "wind_gust": 12.02,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 66,
            "pop": 0.78,
            "rain": 1.53,
            "uvi": 7
        },
        {
            "dt": 1688209200,
            "sunrise": 1688180654,
            "sunset": 1688242534,
            "moonrise": 1688237700,
            "moonset": 1688171820,
            "moon_phase": 0.42,
            "summary": "Expect a day of partly cloudy with rain",
            "temp": {
                "day": 289.17,
                "min": 289,
                "max": 290.18,
                "night": 289.38,
                "eve": 289,
                "morn": 289.3
            },
            "feels_like": {
                "day": 288.97,
                "night": 289.15,
                "eve": 288.6,
                "morn": 289.16
            },
            "pressure": 999,
            "humidity": 82,
            "dew_point": 286.04,
            "wind_speed": 10.73,
            "wind_deg": 194,
            "wind_gust": 12.27,
            "weather": [
                {
                    "id": 500,
                    "main": "Rain",
                    "description": "light rain",
                    "icon": "10d"
                }
            ],
            "clouds": 77,
            "pop": 1,
            "rain": 3.87,
            "uvi": 7
        }
    ]
}
        expectedArray = [{'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687604400, 'temperature': 290.45, 'windspeed': 5.98, 'wind_deg': 200, 'precipitation_chance': 0},
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687690800, 'temperature': 291.27, 'windspeed': 6.61, 'wind_deg': 139, 'precipitation_chance': 0}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687777200, 'temperature': 289.3, 'windspeed': 10.74, 'wind_deg': 288, 'precipitation_chance': 0.79}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687863600, 'temperature': 289.14, 'windspeed': 8.09, 'wind_deg': 245, 'precipitation_chance': 0.23}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1687950000, 'temperature': 289.81, 'windspeed': 8.19, 'wind_deg': 238, 'precipitation_chance': 1}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1688036400, 'temperature': 288.52, 'windspeed': 7.32, 'wind_deg': 327, 'precipitation_chance': 0.93}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1688122800, 'temperature': 288.93, 'windspeed': 11.48, 'wind_deg': 244, 'precipitation_chance': 0.98}, 
                   {'latitude': 54.5973, 'longitude': 5.9301, 'timestamp': 1688209200, 'temperature': 289.26, 'windspeed': 9.15, 'wind_deg': 210, 'precipitation_chance': 0.99}]
        actualArray = []
        actualArray = writeToArray(response,actualArray)
        print(actualArray)
        print(expectedArray)
        testing.assert_array_equal(expectedArray,actualArray)
        
if __name__ == '__main__':
    unittest.main()