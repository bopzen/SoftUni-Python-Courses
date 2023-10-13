SELECT
	c.id,
	CONCAT(c.first_name, ' ', c.last_name) AS creator_name,
	email
FROM
	creators AS c
LEFT JOIN
	creators_board_games
	ON
	c.id = creators_board_games.creator_id
WHERE
	creator_id IS NULL
ORDER BY
	creator_name
;