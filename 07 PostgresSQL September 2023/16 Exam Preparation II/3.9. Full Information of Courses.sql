SELECT
	a.name AS address,
	CASE
		WHEN EXTRACT(HOUR FROM co.start) BETWEEN 6 AND 20 THEN 'Day'
		ELSE 'Night'
	END AS day_time,
	co.bill,
	cl.full_name,
	c.make,
	c.model,
	ca.name
FROM
	courses AS co
JOIN
	clients AS cl
	ON
	cl.id = co.client_id
JOIN
	cars AS c
	ON
	c.id = co.car_id
JOIN
	addresses AS a
	ON
	a.id = co.from_address_id
JOIN
	categories AS ca
	ON
	ca.id = c.category_id
ORDER BY
	co.id
;