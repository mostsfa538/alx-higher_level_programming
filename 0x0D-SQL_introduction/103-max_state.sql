-- displays the max temperature of each state (ordered by State name)
SELECT state, MAX(value) AS value FROM temperatures GROUP BY state ORDER BY state ASC 
