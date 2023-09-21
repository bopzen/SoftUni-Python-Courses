SELECT
	id, 
	CONCAT(number, ' ', street) as "Address",
	city_id
FROM addresses
WHERE id >= 20;