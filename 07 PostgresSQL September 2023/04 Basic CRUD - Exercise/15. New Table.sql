CREATE TABLE IF NOT EXISTS
	company_chart
AS
SELECT
	CONCAT_WS(' ', first_name, last_name) as "Full Name",
	job_title AS "Job Title",
	department_id as "Department ID",
	manager_id as "Manager ID"
FROM
	employees;