
-- 1. Verify the daily analytics records
SELECT COUNT(*) AS total_records,
       MIN(pickup_day) AS first_date,
       MAX(pickup_day) AS last_date
FROM daily_taxi_analytics;

-- 2. Find the busiest day
SELECT pickup_day, total_trips, total_fare
FROM daily_taxi_analytics
ORDER BY total_trips DESC
LIMIT 1;

-- 3. Find the quietest day
SELECT pickup_day, total_trips, total_fare
FROM daily_taxi_analytics
ORDER BY total_trips ASC
LIMIT 1;

-- 4. Find the top five busiest days
SELECT pickup_day, total_trips, total_fare
FROM daily_taxi_analytics
ORDER BY total_trips DESC
LIMIT 5;

-- 5. Calculate January totals and daily average
SELECT
    ROUND(AVG(total_trips), 2) AS average_daily_trips,
    SUM(total_trips) AS total_january_trips,
    ROUND(SUM(total_fare), 2) AS total_january_base_fares
FROM daily_taxi_analytics;
