DROP TABLE IF EXISTS query1;
CREATE TABLE query1
(
	cust_id int,
    frequency int
);

INSERT INTO query1
SELECT cust_id, COUNT(cust_id)AS Frequency 
  FROM new_schema.cust2

  GROUP BY cust_id 
  ORDER BY cust_id;
  select * from query1;
