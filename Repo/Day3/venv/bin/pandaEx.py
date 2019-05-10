import pandas as pd

df1 = pd.read_csv ('dbdata.csv')
df2 = df1.head(5)
#print(df2)
df3 = df1.tail(5)
#print(df3)
df4 = df1['id']
#print(df4)
df5 = df1['id'].describe()
#print(df5)
df6 = df1.describe()
#print(df6)
df7 = df1['id'].mean()
print(df7)