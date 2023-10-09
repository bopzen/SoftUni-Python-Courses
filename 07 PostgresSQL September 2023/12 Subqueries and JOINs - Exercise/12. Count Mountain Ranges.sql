SELECT
	country_code,
	COUNT(DISTINCT mountain_range) AS mountain_range_count
FROM
	mountains_countries
JOIN
	mountains AS m
	ON
	m.id = mountains_countries.mountain_id
WHERE
	country_code in ('US', 'RU', 'BG')
GROUP BY
	country_code
;