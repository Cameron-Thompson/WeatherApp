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
