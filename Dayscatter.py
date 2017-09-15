import MySQLdb
import pandas as pd
db = MySQLdb.connect("localhost","root","angry","new_schema" )

cursor = db.cursor()
cursor.execute("SELECT epoch_time,count(epoch_time) as Frequency FROM new_schema.cust2 group by epoch_time order by count(epoch_time);")
data = cursor.fetchall()
#print (data)
df = pd.DataFrame( [[ij for ij in i] for i in data] )
df.rename(columns={0: 'Date', 1: 'Frequency'}, inplace=True);
df = df.sort_values(['Frequency'], ascending=[1]);

print(df.head(78))


from bokeh.charts import Scatter, output_file, show,save
from bokeh.models import HoverTool

scatter = Scatter(df, x='Date', y='Frequency',tools='hover',legend=False)
hover = scatter.select(dict(type=HoverTool))
hover.tooltips = [("Date", "$x{int}"),("Frequency", "$y{int}")]
#print(df.head())
output_file('Dayscatter.html')
save(scatter)


