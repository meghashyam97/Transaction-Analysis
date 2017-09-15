DROP TABLE IF EXISTS res2;
create table res2 
(
	prod_id int,
    frequency int 
    
);
select cust_id,prod_id from new_schema.cust2 group by cust_id,prod_id;