CREATE VIEW continent_currency_usage
AS
SELECT
	con.continent_code,
	cur.currency_code,
	cur.currency_usage
	
FROM
	continents AS con
JOIN
	(
		SELECT
			continent_code,
			COUNT(currency_code) AS currency_usage,
			currency_code,
			DENSE_RANK() OVER (PARTITION BY continent_code ORDER BY COUNT(currency_code) DESC) AS "rank"
		FROM
			countries
		GROUP BY 
			continent_code,
			currency_code
		HAVING
			COUNT(currency_code) > 1
	) AS cur
	USING (continent_code)
WHERE
	cur.rank = 1
ORDER BY
	cur.currency_usage DESC
;