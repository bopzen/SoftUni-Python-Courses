SELECT
	v.name AS volunteers,
	v.phone_number,
	SUBSTRING(TRIM(REPLACE(address, 'Sofia', '')),3)
FROM
	volunteers AS v
JOIN
	volunteers_departments AS vd
	ON 
	vd.id = v.department_id
WHERE
	vd.department_name = 'Education program assistant'
	AND
	address LIKE '%Sofia%'
ORDER BY
	v.name
;