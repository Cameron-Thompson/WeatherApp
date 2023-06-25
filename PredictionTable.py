createTableString = """CREATE TABLE IF NOT EXISTS daily_prediction(daily_predictionId INT NOT NULL PRIMARY KEY, 
                latitude FLOAT NOT NULL, longitude FLOAT NOT NULL, time_of_Prediction TIMESTAMP NOT NULL,
                temperature FLOAT NOT NULL, wind_speed FLOAT NOT NULL, wind_direction FLOAT NOT NULL,
                precipitation_chance FLOAT NOT NULL)"""

insertTableString = """INSERT INTO daily_prediction (latitude, longitude, time_of_prediction,
temperature, wind_speed, wind_direction, precipitation_chance) VALUES (%s, %s, %s, %s, %s, %s, %s)"""