#8/09/2026

import numpy as np

#0 - Dimensional Array
arr = np.array(40)
print(arr)

#1 - Dimensional Array
dimension_1d = np.array([1 , 2, 3, 4, 5]);
print(dimension_1d)

#2 - Dimensional Array
dimension_2d = np.array([[1 ,2, 3], [4, 5, 6]])
print(dimension_2d)

#numpy Indexing
#Access Element from an Array.

dimension_1d = np.array([1 , 2, 3, 4, 5]);
print("Second Element : ",dimension_1d[1])

#Array Operation
dimension_1d = np.array([1 , 2, 3, 4, 5]);
print("SUM : ", dimension_1d[1] + dimension_1d[3])

#Accesing element from 2 dimensional Array
arr = np.array([[10 , 20, 30],[40, 50, 60]])
print(arr)
print("Access : ", arr[0,1])  #This will print 20

print("Sum : ", arr[0,1] + arr[1 , 1])

#Slicing Arrays

#One Dimensional Array Slicing
array = np.array([1, 2, 3, 4, 5, 6, 7])
slice = array[0 : 2]
print(slice)

#if we didnt gave start index it will itself start from begining
print(array[ : 5])

#same with the end index
print(array[4 : ])

#Negative Indexing
# i want to print 4 ,5 from array
print(array[-4 : -2])

#2 - Dimensional Array
array2 = np.array([[10, 20, 30],[40, 50, 60],[70, 80, 90]])

#print 20 , 30
print(array2[0, 1 : 3])

#9/09/2026

#Numpy Array Shape
#it returns with row and column of the 2 dimensional array

array = np.array([[10 ,20 , 30], [30 , 69, 89], [38, 90, 78]])
print(array.shape)

#Iteration Throug 1d Array
arr = np.array([1, 2, 3, 4, 5])

for x in arr :
    print(x)

arr = np.array([[1, 3, 8],[1, 7, 8]])
for x in arr :
    print(x)

#Numpy Join
#To join to Array

arr1 = np.array([1 , 2, 3])
arr2 = np.array([4, 5, 6])

arr = np.concatenate((arr1, arr2))
print(arr)

#Numpy Sort
arr = np.array([3, 8, 9, 5])

print(np.sort(arr))

arr = np.array(["Ammu" , "Kannan", "Anirudh" , "Komali"])
print(np.sort(arr))