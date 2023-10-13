CREATE OR REPLACE FUNCTION fn_creator_with_board_games(creator_first_name VARCHAR(30))
RETURNS INT
AS
$$
BEGIN
	RETURN
		(
			SELECT
				COUNT(bg.id)
			FROM
				board_games AS bg
			JOIN
				creators_board_games AS cbg
				ON
				cbg.board_game_id = bg.id
			JOIN
				creators AS c
				ON
				c.id = cbg.creator_id
			WHERE
				c.first_name = creator_first_name
		);
END;
$$
LANGUAGE plpgsql;
	