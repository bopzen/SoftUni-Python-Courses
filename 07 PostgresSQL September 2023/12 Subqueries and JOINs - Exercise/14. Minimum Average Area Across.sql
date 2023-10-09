SELECT
	MIN(avg.average) AS minimum_average_area
FROM
	(
		SELECT
			continent_code,
			AVG(area_in_sq_km) AS average
		FROM
			countries
		GROUP BY
			continent_code
	) AS avg
;