import MySQLdb
import pandas as pd
import sys
db = MySQLdb.connect("localhost","root","angry","new_schema" )
cursor=db.cursor()
sql="""drop table if exists query2"""
cursor.execute(sql)
sql="""CREATE TABLE query2
(
	prod_id int,
        frequency int
);"""
cursor.execute(sql)
st=str(sys.argv[1])
#st=str(12347)
cursor.execute("INSERT INTO query2 SELECT DISTINCT prod_id,COUNT(case when cust_id=%s then prod_id end) AS Frequency from new_schema.cust2 group by prod_id HAVING COUNT(case when cust_id=%s then prod_id end)>0;",(st,st))
sql="""SELECT * from query2;"""
cursor.execute(sql)
data=cursor.fetchall()
print(data)


df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Product ID', 1: 'Frequency'}, inplace=True);
df = df.sort_values(['Product ID'], ascending=[1]);
#df['new'] = 0 
print(df.head(10))



from bokeh.charts import Bar, output_file,save
from bokeh.models import HoverTool



bar=Bar(df,'Product ID',values='Frequency',title="test chart",responsive=True,tools='hover',legend=False)
hover = bar.select(dict(type=HoverTool))
hover.tooltips = [("Product ID", "$x"),("Frequency", "$y")]
output_file('relproduct.html')
save(bar)
