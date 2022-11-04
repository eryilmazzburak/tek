select 
CASE WHEN hour IN (0, 1, 2, 3, 4, 5) THEN 'Night'
WHEN hour IN (6, 7, 8, 9, 10, 11) THEN 'Morning'
WHEN hour IN (12, 13, 14, 15, 16, 17) THEN 'Noon'
WHEN hour IN (18, 19, 20, 21, 22, 23) THEN 'Evening'
ELSE 'false' END AS hour
from
(SELECT
dropoff_datetime,
EXTRACT(HOUR FROM DATETIME(dropoff_datetime)) as hour
FROM
  `bigquery-public-data.new_york_taxi_trips.tlc_green_trips_2014`
where data_file_year = 2014
and data_file_month = 3
and pickup_datetime > '2014-03-01'
and dropoff_datetime < '2014-03-08' limit 3) teknasyon;