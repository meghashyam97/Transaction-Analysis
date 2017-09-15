DROP TABLE IF EXISTS query1 ;
CREATE TABLE query1
(
	id int,
    frequency int,
    monetary_value int,
    maxdate int,
    mindate int
    
);

INSERT INTO query1
SELECT cust_id AS id, COUNT(cust_id)-1 AS frequency,SUM(total_price) AS monetary_value,MAX(epoch_time) as maxdate,MIN(epoch_time) as mindate
	from new_schema.cust2

  GROUP BY id 
  ORDER BY id;
  select * from query1;
  select id,frequency,(maxdate-mindate)/86400 as recency,((1323388800+31556926)-maxdate)/86400 as T,monetary_value
 from new_schema.query1;

  DROP TABLE query1;