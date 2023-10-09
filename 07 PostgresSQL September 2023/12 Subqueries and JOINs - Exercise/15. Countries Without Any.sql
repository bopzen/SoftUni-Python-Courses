SELECT
	COUNT(m.country_name) AS countries_without_mountains
FROM
	(
		SELECT
			country_name
		FROM
			countries AS c
		LEFT JOIN
			mountains_countries AS mc
			ON
			c.country_code = mc.country_code
		WHERE
			mc.mountain_id IS NULL
	) AS m
;