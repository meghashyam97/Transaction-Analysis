import MySQLdb
import pandas as pd
db = MySQLdb.connect("localhost","root","angry","new_schema" )

cursor = db.cursor()
sql="""drop table if exists prod1;"""
cursor.execute(sql);
sql="""create table prod1(prod_id int,frequency int);"""
cursor.execute(sql)
sql="""INSERT INTO prod1 SELECT prod_id, COUNT(cust_id)AS frequency FROM new_schema.cust2 GROUP BY prod_id ORDER BY prod_id;"""
cursor.execute(sql)
sql="""select * from prod1;"""
cursor.execute(sql)


data = cursor.fetchall()
print (data)
df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Product ID', 1: 'Frequency'}, inplace=True);
df = df.sort_values(['Product ID'], ascending=[1]);
print(df.head(1536))


#from bokeh.sampledata.autompg import autompg as df
from bokeh.charts import Scatter, output_file, show,save
from bokeh.models import HoverTool

scatter = Scatter(df, x='Product ID', y='Frequency',tools='hover',legend=False)
hover = scatter.select(dict(type=HoverTool))
hover.tooltips = [("Product ID", "$x{int}"),("Frequency", "$y{int}")]
print(df.head())
output_file('prodscatter.html')
save(scatter)


