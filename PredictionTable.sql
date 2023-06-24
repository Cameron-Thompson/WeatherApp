-- Create a new table called 'dailyPrediction' in schema 'weather'
-- Drop the table if it already exists
IF OBJECT_ID('weather.daily_prediction', 'U') IS NOT NULL
DROP TABLE weather.dailyPrediction
GO
-- Create the table in the specified schema
CREATE TABLE daily_prediction
(
    daily_predictionId INT NOT NULL PRIMARY KEY, -- primary key column
    latitude [FLOAT] NOT NULL,
    longitude [FLOAT] NOT NULL,
    time_of_Prediction [TIMESTAMP] NOT NULL,
    temperature [FLOAT] NOT NULL,
    wind_speed [FLOAT] NOT NULL,
    wind_direction [FLOAT] NOT NULL,
    preciptiation_chance [FLOAT] NOT NULL
    -- specify more columns here
);
GO