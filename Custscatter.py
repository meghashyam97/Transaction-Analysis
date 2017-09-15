import MySQLdb
import pandas as pd
db = MySQLdb.connect("localhost","root","angry","new_schema" )

cursor = db.cursor()
cursor.execute("DROP TABLE IF EXISTS query1")
sql="""CREATE TABLE query1
(
	cust_id int,
    frequency int
);"""
cursor.execute(sql)
sql="""INSERT INTO query1
SELECT cust_id, COUNT(cust_id)AS Frequency 
  FROM new_schema.cust2

  GROUP BY cust_id 
  ORDER BY cust_id;"""
cursor.execute(sql)
cursor.execute("select * from query1")
data = cursor.fetchall()
print (data)
df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Customer ID', 1: 'Frequency'}, inplace=True);
df = df.sort_values(['Customer ID'], ascending=[1]);
print(df.head(78))


#from bokeh.sampledata.autompg import autompg as df
from bokeh.charts import Scatter, output_file, show,save
from bokeh.models import HoverTool

scatter = Scatter(df, x='Customer ID', y='Frequency',tools='hover',legend=False)
hover = scatter.select(dict(type=HoverTool))
hover.tooltips = [("Customer ID", "$x{int}"),("Frequency", "$y{int}")]
print(df.head())
output_file('Custscatter.html')
save(scatter)




