SELECT
	c.id,
	c.make,
	c.mileage,
	COUNT(cou.id) AS count_of_courses,
	ROUND(AVG(bill), 2)
FROM
	cars AS c
LEFT JOIN
	courses AS cou
	ON
	cou.car_id = c.id
GROUP BY
	c.id, c.make,c.mileage
HAVING
	COUNT(cou.id) <> 2
ORDER BY
	count_of_courses DESC,
	c.id
;