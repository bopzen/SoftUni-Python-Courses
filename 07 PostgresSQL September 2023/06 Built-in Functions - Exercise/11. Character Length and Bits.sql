SELECT
	CONCAT(m.mountain_range, ' ', p.peak_name) AS "Mountain Information",
	CHAR_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name)),
	BIT_LENGTH(CONCAT(m.mountain_range, ' ', p.peak_name))
FROM
	mountains AS m,
	peaks AS p
WHERE
	m.id = p.mountain_id
;