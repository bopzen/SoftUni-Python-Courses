UPDATE
	countries
SET country_name = 'Burma'
WHERE
	country_name = 'Myanmar'
;

INSERT INTO
	monasteries(monastery_name, country_code)
VALUES
	('Hanga Abbey', (
		SELECT
			country_code
		FROM
			countries
		WHERE
			country_name LIKE 'Tanzania'
	)),
	('Myin-Tin-Daik', (
		SELECT
			country_code
		FROM
			countries
		WHERE
			country_name LIKE 'Myanmar'	
	))
;


SELECT
	continent_name,
	country_name,
	COUNT(monastery_name) AS monasteries_count
FROM
	countries AS c
JOIN
	continents AS con
	USING (continent_code)
LEFT JOIN
	monasteries AS m
	USING (country_code)
WHERE
	NOT c.three_rivers
GROUP BY
	continent_name,
	country_name
ORDER BY
	monasteries_count DESC,
	c.country_name
;