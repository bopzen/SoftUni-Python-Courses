SELECT
	LEFT(first_name, 2) AS initials,
	COUNT('initials') AS user_count
FROM
	users
GROUP by 
	initials
ORDER BY
	user_count DESC,
	initials ASC
;