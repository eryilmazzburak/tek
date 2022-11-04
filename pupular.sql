-- What are the most popular pickup locations?
SELECT
count(pickup_location_id), pickup_location_id
FROM
  `teknasyon.one.two`
group by pickup_location_id
order by 1 desc;


-- What are the most popular dropoff locations?
SELECT
count(dropoff_location_id), dropoff_location_id
FROM
  `teknasyon.one.two`
group by dropoff_location_id
order by 1 desc;


--What are the most popular routes?
SELECT
count(*), pickup_location_id, dropoff_location_id
FROM
  `teknasyon.one.two`
group by pickup_location_id, dropoff_location_id
order by 1 desc;