SELECT
	country_code,
	mountain_range,
	peak_name,
	elevation
FROM
	mountains AS m
JOIN
	peaks AS p
	ON
	m.id = p.mountain_id
JOIN
	mountains_countries AS mc
	ON
	m.id = mc.mountain_id
WHERE
	p.elevation > 2835
	and mc.country_code LIKE 'BG'
ORDER BY
	elevation DESC
;