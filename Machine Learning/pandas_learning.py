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