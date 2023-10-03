CREATE TABLE
	manufacturers(
		id SERIAL PRIMARY KEY,
		name VARCHAR(50)
	)
;

CREATE TABLE
	models(
		id INTEGER GENERATED ALWAYS AS IDENTITY(START WITH 1000 INCREMENT BY 1) PRIMARY KEY,
		model_name VARCHAR(50),
		manufacturer_id INT,
		
		CONSTRAINT fk_models_manufacturers
		FOREIGN KEY (manufacturer_id)
		REFERENCES manufacturers(id)
	)
;

CREATE TABLE
	customers(
		id SERIAL PRIMARY KEY,
		name VARCHAR(50),
		date DATE
	)
;

CREATE TABLE
	photos(
		id SERIAL PRIMARY KEY,
		url VARCHAR(100),
		place VARCHAR(50),
		customer_id INT,
		
		CONSTRAINT fk_photos_customers
		FOREIGN KEY (customer_id)
		REFERENCES customers(id)
	)
;

INSERT INTO 
	customers(name, date)
VALUES 
	('Bella', '2022-03-25'),
	('Philip', '2022-07-05')
;


INSERT INTO
	photos(url, place, customer_id)
VALUES
	('bella_1111.com', 'National Theatre', 1),
	('bella_1112.com', 'Largo', 1),
	('bella_1113.com', 'The View Restaurant', 1),
	('philip_1121.com', 'Old Town', 2),
	('philip_1122.com', 'Rowing Canal', 2),
	('philip_1123.com', 'Roman Theater', 2)
;