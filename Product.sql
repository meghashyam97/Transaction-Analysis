#this is for basic scatter plot


select cust_id,count(cust_id) as frequency  from new_schema.cust2 where prod_id=21975;
select sum(quantity) from new_schema.cust2 where prod_id=15034;
select prod_id,quantity from new_schema.cust2 where prod_id=21975 and in_sale=1 ;#group by cust_id order by cust_id;