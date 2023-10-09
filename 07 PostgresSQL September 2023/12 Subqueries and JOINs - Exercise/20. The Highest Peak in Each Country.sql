WITH all_peaks AS
(
	SELECT
		c.country_name,
		p.peak_name,
		p.elevation,
		m.mountain_range,
		ROW_NUMBER() OVER (PARTITION BY c.country_name ORDER BY p.elevation DESC) AS row_number
	FROM
		countries AS c
	LEFT JOIN
		mountains_countries AS mc
		ON
		c.country_code = mc.country_code
	LEFT JOIN
		mountains AS m
		ON
		mc.mountain_id = m.id
	LEFT JOIN
		peaks AS p
		ON
		p.mountain_id = m.id
)

SELECT
	country_name,
	COALESCE(peak_name, '(no highest peak)') AS highest_peak_name,
	COALESCE(elevation, 0) AS highest_peak_elevation,
	CASE
		WHEN peak_name IS NULL THEN '(no mountain)'
		ELSE mountain_range
	END AS mountain
FROM
	all_peaks
WHERE
	row_number = 1
ORDER BY
	country_name,
	peak_name
;