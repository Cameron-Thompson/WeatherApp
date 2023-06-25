createTableString = """CREATE TABLE IF NOT EXISTS daily_prediction(daily_predictionId INT NOT NULL  AUTO_INCREMENT, 
                latitude FLOAT NOT NULL, longitude FLOAT NOT NULL, time_of_Prediction DATETIME NOT NULL,
                temperature FLOAT NOT NULL, wind_speed FLOAT NOT NULL, wind_direction FLOAT NOT NULL,
                precipitation_chance FLOAT NOT NULL, PRIMARY KEY (daily_predictionId))"""
#%s acts as a placeholder, executemany replaces these with the value in that element in the array
#This works because arrays are always the same order
insertTableString = """INSERT INTO daily_prediction (latitude, longitude, time_of_prediction,
temperature, wind_speed, wind_direction, precipitation_chance) VALUES (%s, %s, %s, %s, %s, %s, %s)"""