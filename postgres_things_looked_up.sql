-- Postgres
----------------------------------------------
-- queries
---- aggregations, group by
-------- group by timestamp on days
	SELECT date_trunc('day', timestamp_column), count(*) FROM table_name WHERE column = 'condition' GROUP BY 1 ORDER BY 1;

-------- select the columns names for a table
	SELECT column_name
	FROM information_schema.columns
	WHERE table_schema = 'public'
	AND table_name = 'laminator_foam_defect_removal_records';