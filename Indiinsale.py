import MySQLdb
import pandas as pd
import sys
db = MySQLdb.connect("localhost","root","angry","new_schema" )
cursor=db.cursor()
st=str(sys.argv[1])
#st=str(21975);
#print(st)
cursor.execute("select sum(quantity) from new_schema.cust2 where prod_id=%s and in_sale=1 ;"%(st));
(data,)=cursor.fetchone();
print(data)

