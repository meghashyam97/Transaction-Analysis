import MySQLdb
import pandas as pd
import sys
db = MySQLdb.connect("localhost","root","angry","new_schema" )

cursor = db.cursor()
string=str(sys.argv[1]);
cursor.execute("select prod_id,count(prod_id) from new_schema.cust2 where epoch_time=%s group by prod_id;"%(string))
data = cursor.fetchall()
#print (data)
df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Prod id', 1: 'Frequency'}, inplace=True);
df = df.sort_values(['Frequency'], ascending=[1]);

print(df.head(78))


from bokeh.charts import Bar, output_file,save
from bokeh.models import HoverTool



bar=Bar(df,'Prod id',values='Frequency',responsive=True,tools='hover',legend=False)
hover = bar.select(dict(type=HoverTool))
hover.tooltips = [("Prod id", "$x"),("Frequency", "$y")]
output_file('Listproducts.html')
save(bar)



