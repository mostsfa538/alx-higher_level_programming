-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending) TOP 3
SELECT TOP 3 city, AVG(value) AS avg_temp
FROM temperatures
WHERE month IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC;
