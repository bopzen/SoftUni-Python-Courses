CREATE OR REPLACE PROCEDURE sp_animals_with_owners_or_not(
	IN animal_name VARCHAR(30),
	OUT name VARCHAR(30)
)
AS
$$
BEGIN
	SELECT INTO name
		o.name
	FROM
		owners AS o
	JOIN
		animals AS a
		ON
		a.owner_id = o.id
	WHERE
		a.name = animal_name;
	IF name IS NULL THEN
		name = 'For adoption';
	END IF;
	RETURN;
END;
$$
LANGUAGE plpgsql;