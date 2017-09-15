DROP TABLE IF EXISTS query2;
CREATE TABLE query2
(
	prod_id int,
    frequency int
);
CREATE TABLE temp1
(
	cust_id int 
);
INSERT INTO temp1
SELECT DISTINCT cust_id from new_schema.cust2;
SELECT * FROM temp1;
/*SELECT DISTINCT prod_id from new_schema.cust2 WHERE cust_id=12347;
SELECT count(DISTINCT prod_id) from new_schema.cust2 WHERE cust_id=12347 group by prod_id;*/
INSERT INTO query2
SELECT DISTINCT prod_id,COUNT(case when cust_id=12346 then prod_id end) AS Frequency from new_schema.cust2 
group by prod_id 
HAVING COUNT(case when cust_id=12346 then prod_id end)>0;
SELECT * from query2;
DROP TABLE temp1;
DROP TABLE query2;
/*we will plot histogram with this table to show most and least frequenly bought products by that customer
We have to pass the customer number as an argument to the script from the ui
for now i have used concrete value and only a part of the whole csv file
Table temp1 will be used to make scatter plot of different customers*/
