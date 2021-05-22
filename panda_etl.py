import pandas as pd
df = pd.read_csv('sample.csv', delimiter=',') # read_csv  read csv and txt file 
sdf = df.head(5) #small Top 5 row

#sdf = df.tail(5) # Bottom 5 rows
##print (sdf.columns)
#print (sdf['UNITS'][0:4])

#print (sdf.iloc[0:4]) # integer location
#print(sdf.iloc[2,1])  # read specific location
for index,row in sdf.iterrows():
    #print(index,row['STATUS'])
    pass
# for i, row in sdf.iterrows():
#     for j, column in row.iteritems():
#         #print(j,column)
#         pass
#rdf = df.loc[(df['STATUS'] == 'F') & (df['Data_value'] == 80078)]
rdf = df.loc[(df['STATUS'] == 'F') & (df['Data_value'] == 80078)]
print(rdf)
#print(rdf[['STATUS','Data_value']])
df_sorted = df.sort_values(['Data_value','STATUS'],ascending = [0,1])
print(df_sorted)
df['Total'] = df['Data_value'] + df ['Period']
df['tot_series'] = df['Series_reference'] + df['Series_reference']
import re
#df = df.loc[df[]]
#---------------------------------------------------------
dfsales = pd.read_csv('SalesJan2009.csv')
print(dfsales)
print(dfsales.columns)
dfsales.groupby(['Payment_Type']).count()
dfsales = dfsales.groupby(['Payment_Type']).sum()['Price']


#df.to_csv('out.csv',index = False)
#Write a Pandas program to create and display a one-dimensional array-like object containing an array of data using Pandas module
s1 = pd.Series([1,3,2,6,'wewe'])
print(s1)
#2. Write a Pandas program to convert a Panda module Series to Python list and it's type
s = list(s1)
print(s)
#Write a Pandas program to add, subtract, multiple and divide two Pandas Series.
ds1 = pd.Series([2, 4, 6, 8, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
print(ds1 + ds2)
df = pd.DataFrame({'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 800},index = [0,1,2,3,4])
print(df.loc[1,4])




# for df in pd.read_csv('sample.csv', delimiter=',',chunksize=10000):
#     print(df)