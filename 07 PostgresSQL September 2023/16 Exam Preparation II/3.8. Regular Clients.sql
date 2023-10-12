SELECT
	cl.full_name,
	COUNT(car_id) AS count_of_cars,
	SUM(co.bill) AS total_sum
FROM
	clients AS cl
JOIN
	courses AS co
	ON
	co.client_id = cl.id
WHERE
	cl.full_name LIKE '_a%'
GROUP BY
	cl.full_name
HAVING
	COUNT(car_id) > 1
ORDER BY
	cl.full_name
;