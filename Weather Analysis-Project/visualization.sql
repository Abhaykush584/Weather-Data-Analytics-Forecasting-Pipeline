 -- Visualization of weather analysis using sql

 SELECT * FROM weather_analysis LIMIT 10 ;



 --1. Todays weather . 
 SELECT * FROM weather_analysis WHERE date_only = '2025-4-15' ;




 --2. Hottest week day in a month.
 SELECT day_of_week , day_of_month , max(temperature_2m)  as max_temperature_recorded FROM weather_analysis GROUP BY day_of_month , day_of_week ORDER BY max_temperature_recorded DESC;




 --3. Coolest week day in a month.
 SELECT day_of_week , date_only , min(temperature_2m) as 
 min_temperature_recorder FROM weather_analysis GROUP BY date_only , day_of_week ORDER BY date_only ASC;



--4. Days having maximum chance of raining.
SELECT DISTINCT(date_only) as date , day_of_week, is_raining 
FROM weather_analysis  
WHERE 
is_raining = 'Yes' AND 
date_only BETWEEN '2025-04-13' AND '2025-04-30'

ORDER BY date_only ASC;



--5.Is there any chance of raining today?
SELECT DISTINCT date_only as date_ , time_only as time_ FROM weather_analysis 
where is_raining = 'Yes' and date_only='2025-4-21'

ORDER BY time_only;



--6. lowest temperature recorded.
SELECT date_only , min(temperature_2m) as 
 min_temperature_recorder FROM weather_analysis 
 GROUP BY date_only
 ORDER BY min_temperature_recorder ASC
 LIMIT 1;



--7. highest temperature recorded.
SELECT date_only , max(temperature_2m) as 
 max_temperature_recorder FROM weather_analysis 
 GROUP BY date_only
 ORDER BY max_temperature_recorder DESC
 LIMIT 1;

SELECT COUNT(*) FROM weather_analysis;









