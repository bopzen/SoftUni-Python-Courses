CREATE TABLE search_results(
	id SERIAL PRIMARY KEY,
	address_name VARCHAR(50),
	full_name VARCHAR(100),
	level_of_bill VARCHAR(20),
	make VARCHAR(30),
    condition CHAR(1),
    category_name VARCHAR(50)
);


CREATE OR REPLACE PROCEDURE sp_courses_by_address(
	IN address_name VARCHAR(100)
)
AS
$$
BEGIN
	TRUNCATE search_results;
	
	INSERT INTO
		search_results(
			address_name, 
			full_name, 
			level_of_bill, 
			make, 
			condition, 
			category_name
		)
	SELECT 
		a.name,
		cl.full_name,
		CASE
			WHEN co.bill <= 20 THEN 'Low'
			WHEN co.bill <= 30 THEN 'Medium'
			ELSE 'High'
		END,
		c.make,
		c.condition,
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
		categories AS ca
		ON
		ca.id = c.category_id
	JOIN
		addresses AS a
		ON
		a.id = co.from_address_id
	WHERE
		a.name = address_name
	ORDER BY
		c.make,
		cl.full_name;
		
END;
$$
LANGUAGE plpgsql;