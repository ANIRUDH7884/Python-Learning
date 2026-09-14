#pandas Library using to clean the messy data / analyze the data
#comonly used for Data analysis 
#pandas - Python Data Analysis / Panel Data

import pandas as pd

#series - A pandas Series is like a Column in a Table

a = [1, 2, 3]

myVar = pd.Series(a)

print(myVar)

#label - Changing the name of Index
arr = ["Anirudh", "Ammu", "Kannan", "komali"]

array = pd.Series(arr , index = ["Name" , "name", "name", "name"])

print(array)
print(array["name"])

#DataFrame - ITS A 2D DATA STRUCTURE

data = {
    "Calories" : [420 , 560, 789],
    "Duration" : [50 , 40, 50]
 }

df = pd.DataFrame(data)
print(df)

#Locate Row
print(df.loc[0])
print(df.loc[[0 , 1,2]])

df = pd.DataFrame(data , index = ["day1", "day2", "Day3"])
print(df)
print(df.loc["day2"])