SELECT
	COUNT(c.country_name) AS countries_without_rivers
FROM 
	countries AS c
LEFT JOIN
	countries_rivers AS cr
		ON
	cr.country_code = c.country_code
WHERE
	river_id IS NULL
;