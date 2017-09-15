import pandas as pd


df=pd.read_csv("J:/J/College/SE Project/Apriori/res2.csv", dtype={'prod_id': object});
#df.groupby('cust_id', sort=False)['prod_id'].apply(' '.join)
print(df.head())

result1 = [df['cust_id'][0]]  
result2 = [df['prod_id'][0]]

# Use zip() to iterate over the two columns of df simultaneously,
# making sure to skip the first row which is already added
for a, b in zip(df['cust_id'][2:], df['prod_id'][2:]):
    if a == result1[-1]:        # If a matches the last value in result2,
        result2[-1] += " " + b  # add b to the last value of result1
    else:  # Otherwise add a new row with the values
        result1.append(a)
        result2.append(b)

# Create a new dataframe using these result lists
df = pd.DataFrame({'cust_id': result1, 'prod_id': result2})
print(df.head(10))
header = ["prod_id"]
df.to_csv('output.csv', columns = header,header=False,index=False)




              
