import pandas as pd

data = pd.read_csv('women_clothing_ecommerce_sales.csv')

#To print the data
data

#data.head()  - to get a quick Overview of the data in the first
print(data.head())
print(data.head(15))

#data.tail() - to get the last 5 rows of the data
print(data.tail())

#data.shape - to know the no of colums and rows
print(data.shape)

#data.size - to know the size of data
print(data.size)

#data.info - to get the full information of the data like data type count and everything
print(data.info())

#data.describe() - it gives the full description of the data o integer values
print(data.describe()) 

#data.describe(include = "O") - It Give the full description including the charachters 
print(data.describe(include= "O"))

print(data.describe(include="all"))

print(data['size'])

print(data.color)

#Locator

print(data.loc[0:10, 'order_id':'size']) #indexed locating by specifying the required index

print(data.loc[:, 'order_id':'size']) #not specifying the index so returns all orders

print(data.loc[0:14, ['order_id', 'size']])

#iloc ---> select data using position or index number

print(data.iloc[:,0:5])

print(data.iloc[500:, 2 :: 3])

#data copy to make any changes so its doesnt affect the orginal Data
df= data.copy()
print("Copy : ", df)

#to drop any Column

new_ds = df.drop(columns=['size'])
print(new_ds.head())
