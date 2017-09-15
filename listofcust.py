import MySQLdb
import pandas as pd
import sys
db = MySQLdb.connect("localhost","root","angry","new_schema" )
cursor=db.cursor()
cursor.execute("select cust_id,quantity from new_schema.cust2 where prod_id=21975 ;");
data=cursor.fetchall()
print(data)


df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Customer ID', 1: 'Quantity'}, inplace=True);
df = df.sort_values(['Customer ID'], ascending=[1]);
#df['new'] = 0
df=df.groupby("Customer ID").sum()
print(df.head(10))



from bokeh.charts import Bar, output_file,save
from bokeh.models import HoverTool



bar=Bar(df,'Customer ID',values='Quantity',title="test chart",responsive=True,tools='hover',legend=False)
hover = bar.select(dict(type=HoverTool))
hover.tooltips = [("Customer ID", "$x"),("Quantity", "$y")]
output_file('listofcust.html')
save(bar)
