# Weather-Data-Analytics-Forecasting-Pipeline Project

🖼️Weather Data Analysis and Alert System
Project Overview
This project fetches hourly weather data from the Open-Meteo API, stores it in a PostgreSQL database, calculates daily moving averages, generates weather alerts via email, and performs weather data analysis using SQL. Additionally, it includes instructions to create an interactive weather dashboard using Power BI.

## ✏️Features

>Fetch hourly weather data (temperature, humidity, precipitation) for a specified location.
>Store data in PostgreSQL (weather_update table).
>Calculate 7-day moving averages of temperature, humidity, and precipitation.
>Store moving averages in a separate table (moving_average).
>Send email alerts for extreme weather conditions (e.g., heatwaves).
>Scheduled data fetching every minute (can be adjusted).
>SQL queries for weather analysis including hottest/coolest days, rainfall chances, and temperature extremes.
>Interactive Power BI dashboard based on the weather and moving average data.

Setup Instructions
Prerequisites
Python 3.8+

PostgreSQL installed and running locally or remotely

Power BI Desktop installed (for dashboard visualization)

Gmail account with App Password for sending emails via SMTP

Python Libraries Required
bash
Copy
Edit
pip install requests pandas sqlalchemy schedule psycopg2-binary

### Step 1: Database Setup
Create a PostgreSQL database named weather_data.

Create tables with the following structure:

sql
Copy
Edit
CREATE TABLE weather_update (
    time TIMESTAMP PRIMARY KEY,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    precipitation FLOAT
);

CREATE TABLE moving_average (
    date DATE PRIMARY KEY,
    temperature_2m FLOAT,
    relative_humidity_2m FLOAT,
    precipitation FLOAT,
    moving_avg_temp FLOAT,
    moving_avg_humidity FLOAT,
    moving_avg_precipitation FLOAT
);
### Step 2: Fetch and Insert Weather Data
The fetch_weather() function pulls data from Open-Meteo API.

The insert_data() function inserts hourly data into weather_update and computes/stores daily moving averages into moving_average.

The schedule library runs insert_data() every minute (customize interval as needed).

### Step 3: Weather Alert Email
send_weather_alert() sends emails for extreme conditions.

Customize alert logic (e.g., temperature > threshold) and call this function to notify users.

Use Gmail SMTP with an app password.

### Step 4: SQL Weather Analysis Queries
Run these queries in PostgreSQL to gain insights:

Today's Weather:

sql
Copy
Edit
SELECT * FROM weather_analysis WHERE date_only = CURRENT_DATE;
Hottest Weekday in Month:

sql
Copy
Edit
SELECT day_of_week, day_of_month, MAX(temperature_2m) AS max_temperature
FROM weather_analysis
GROUP BY day_of_month, day_of_week
ORDER BY max_temperature DESC;
Coolest Weekday in Month:

sql
Copy
Edit
SELECT day_of_week, date_only, MIN(temperature_2m) AS min_temperature
FROM weather_analysis
GROUP BY date_only, day_of_week
ORDER BY date_only ASC;
Days with Maximum Chance of Raining:

sql
Copy
Edit
SELECT DISTINCT date_only, day_of_week, is_raining
FROM weather_analysis
WHERE is_raining = 'Yes' AND date_only BETWEEN '2025-04-13' AND '2025-04-30'
ORDER BY date_only ASC;
Chance of Raining Today:

sql
Copy
Edit
SELECT DISTINCT date_only, time_only
FROM weather_analysis
WHERE is_raining = 'Yes' AND date_only = CURRENT_DATE
ORDER BY time_only;
Lowest Temperature Recorded:

sql
Copy
Edit
SELECT date_only, MIN(temperature_2m) AS min_temperature
FROM weather_analysis
GROUP BY date_only
ORDER BY min_temperature ASC
LIMIT 1;
Highest Temperature Recorded:

sql
Copy
Edit
SELECT date_only, MAX(temperature_2m) AS max_temperature
FROM weather_analysis
GROUP BY date_only
ORDER BY max_temperature DESC
LIMIT 1;



### Step 5: Power BI Dashboard Creation
Import data from PostgreSQL tables weather_update and moving_average.

Create visuals for:

Hourly temperature, humidity, precipitation trends.

7-day moving averages line charts.

Weather alerts and extreme event markers.

Rainfall days and temperature extremes.

Use filters/slicers by date and location.

Schedule dashboard refresh to sync with database updates.

![Weather Analysis Dashboard](https://github.com/Abhaykush584/Projects-Dashboards/blob/main/dashboard%20ss/Screenshot%202025-06-05%20102009.png)
![Weather Analysis Dashboard](https://github.com/Abhaykush584/Projects-Dashboards/blob/main/dashboard%20ss/Screenshot%202025-06-05%20095134.png)
![Weather Analysis Dashboard](https://github.com/Abhaykush584/Projects-Dashboards/blob/main/dashboard%20ss/Screenshot%202025-06-05%20095143.png)
![Weather Analysis Dashboard](https://github.com/Abhaykush584/Projects-Dashboards/blob/main/dashboard%20ss/Screenshot%202025-06-05%20102021.png)
![Weather Analysis Dashboard](https://github.com/Abhaykush584/Projects-Dashboards/blob/main/dashboard%20ss/Screenshot%202025-06-05%20095159.png)
