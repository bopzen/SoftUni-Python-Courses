SELECT
	bg.name,
	bg.rating,
	c."name" AS category_name
FROM
	board_games AS bg
JOIN
	categories AS c
	ON
	c.id = bg.category_id
JOIN
	players_ranges AS pr
	ON
	pr.id = bg.players_range_id
WHERE
	(rating > 7 AND bg.name ILIKE '%a%')
	OR 
	(rating > 7.5 AND pr.min_players >=2 AND pr.max_players <= 5)
ORDER BY
	bg.name,
	bg.rating DESC
LIMIT 5
;