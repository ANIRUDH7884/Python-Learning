#list 
mylist = ["Bannana" , "Apple", "Organge", 2 ]
print(list)

myList = ["Bannana" , "Apple", "Organge", "Bannana" , "Apple", "Organge"]
print(myList)
print(myList[3])

#to find length We using len()
print(len(myList))

#To find the Data Type of List
print(type(myList))
print(type(list))

#List Constructor
#Another Method by using list() 

#method 1 
thelist = ["Bannana" , "Apple", "Organge"]
print(thelist)

#method 2
thislist = list(("Bannana" , "Apple", "Organge" ))
print(thislist)

#Two Type of Indexing

#positive 
ListIndexing = [ "Anirudh" , "Komali" , "Ammu", "Anni"]
print(ListIndexing[2])

#Negative Indexing
print(ListIndexing[-1])

#multiple element indexing
print(ListIndexing[0:3])
print(ListIndexing[1 : ])
print(ListIndexing[ : 2])
print(ListIndexing[-3 : -1])

myList = ["Bannana" , "Apple", "Organge", "kiwi" , "pineapple", "citrus"]
print(mylist[-4 : -1])

#Access List Items
#in

myList = ["Bannana" , "Apple", "Organge", "kiwi" , "pineapple", "citrus"]
if "Bannana" in myList :
    print("Bannana is in the List")
else : 
    "Its not in the List"

#List Items are Changeable or Mutabale
myList = ["Bannana" , "Apple", "Organge", "kiwi" , "pineapple", "citrus"]
myList[0 : 4] = ["Supporta", "Strawberry"]
myList[1] = "Avacado"
print(myList)

#List Methods

#Append() - To add an element at the last of the list
goatList = ["Messi" , "Leo", "lionel"]
goatList.append("Lionel Andreas Messi")
print(goatList)

#insert() - to insert an elemnet using Index Number by interchanging the position of the lement inside the list
goatList = ["Messi" , "Leo", "lionel"]
goatList.insert(1, "La Pulga")
print(goatList)
 
#extend() - want to append a list by using another list and merging into 1 list
mobileList  = ["Samsung" , "Apple" , "Vivo"]
newPhones = ["Oneplus" , "Xiaomi" , "Oppo"]
mobileList.extend(newPhones)
print(mobileList)

#Remove an elemnet
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
mobiles.remove("samsung")
mobiles.remove("Oneplus")
print(mobiles)

#POP - reMOVE SPECIFIES INDEX
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
mobiles.pop(1)

#Remove the last element
mobiles.pop()
print(mobiles)

#delete - keyword (del)
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
del mobiles[2]
print(mobiles)

#delete entire list
del mobiles

#Clear() - removes the elements in the list Only items  in the list not the list
thisList = ["ramu" , "somu"]
thisList.clear()
print(thisList)

#sort() 
sortingList =  ["c" , "a" , "d" , "b"]
sortingList.sort()
print(sortingList)

#copy() - 
copyList = ["anirudh" , "ammu"]
myList = copyList.copy()
print(myList)

#count() - to find the count of an item in a list
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
counts = mobiles.count("Oneplus")
print(counts)

#Index() - to recogonise the position
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
indexes = mobiles.index("Iphone")
print(indexes)

#reverse() - to reverse the order of the list
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo" , "Oneplus"]
mobiles.reverse()
print(mobiles)

#sum() - to get the sum of a numbered list
#min()
#max()


#eXCERSISE

#Create a list of 5 mobile brands and print it.
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo"]
print(mobiles)

#Create a list of 5 employee salaries.
employers_salary = ["15000" , "30000" , "5700" , "67900" , "45609"]
print(employers_salary)

#List of Numbers and its Length
Numbers = [10 , 30 , 40 , 50 , 60]
print(len(Numbers))

#Append an Element to the end of a List
sampleList = ["Car" , "Bike" , "Auto"]
sampleList.append("Scooter")
print(sampleList)

#insert an element at a sepcific position
sampleList = ["Car" , "Bike" , "Auto"]
sampleList.insert(1, "Scooter")
print(sampleList)

#Remove the first occurrence of an element in a list
sampleList = ["Car" , "Bike" , "Auto"]
sampleList.remove("Car")
print(sampleList)

#sum of all elements in a list
Numbers = [10 , 30 , 40 , 50 , 60]
Total = sum(Numbers)
print(Total)

#Acces the Third Element of a List
sampleList = ["Car" , "Bike" , "Auto", "Scooter"]
print(sampleList[3])

#print the last element of a list
sampleList = ["Car" , "Bike" , "Auto", "Scooter", "Truck"]
print(sampleList[4])

#Extract a Subset of elements from a list using slicing
sampleList = ["Car" , "Bike" , "Auto", "Scooter", "Truck"]
sliced = sampleList[1 : 4]
print(sliced)

#Reverse A list using slicing
sampleList = ["Car" , "Bike" , "Auto", "Scooter", "Truck"]
reversedList = sampleList[ : : -1]
print(reversedList)

#sort a list of numbers in ascending order
Numbers = [10 , 30 , 40 , 50 , 60]
Numbers.sort()
print(Numbers)

#sort a list of numbers in ascending order
sampleList = ["Car" , "Bike" , "Auto", "Scooter", "Truck"]
sampleList.sort()
print(sampleList)

#Find the minimum and maximum
Numbers = [10 , 30 , 40 , 50 , 60]
print(min(Numbers))
print(max(Numbers))

#count the Occurence of a specific element in a list
sampleList = ["Car" , "Bike" , "Auto", "Scooter", "Truck" , "Car" , "Car"]
counts = sampleList.count("Car")
print(counts)

#Employee Joining System
employees = [ "Anirudh", "Ammu", "Rahul"]
employees.append("Arjun")
print(employees)

#Employee Resignation System
employees = [ "Anirudh", "Ammu", "Rahul", "Arjun"]
employees.remove("Rahul")
print(employees)

#Mobile Store Inventory
mobiles = [ "Samsung","iPhone","OnePlus", "OnePlus", "Vivo"]
counts = mobiles.count("Oneplus")
print("Total Count of Oneplus : " , counts)

#Student Ranking
marks = [ 75, 90, 45, 88, 99, 67 ]
print(max(marks))
print(min(marks))

#Company Payroll
salaries = [
    15000,
    20000,
    35000,
    18000,
    22000
]
total = sum(salaries)
highest = max(salaries)
lowest = min(salaries)

print("Total salary for employees This month :" , total)
print("Highest Salary :" , highest)
print("Lowest Salary :" , lowest)

#E-Commerce Product Sorting
prices = [
    3000,
    500,
    1500,
    7000,
    2500
]

prices.sort()
print(prices)

# Customer Search
customers = [
    "Anirudh",
    "Ammu",
    "Rahul",
    "Arjun"
]

if "Ammu" in customers :
    print("Customer Found")
else :
    print("Customer Not Found")

#Dashboard Preview
employees = [
    "Anirudh",
    "Ammu",
    "Rahul",
    "Arjun",
    "Vishnu",
    "Akhil"
]
print(employees[ : 3])

#Latest Chat Messages
messages = [
    "Hello",
    "How are you?",
    "Good Morning",
    "See you"
]
messages.reverse()
print(messages)

#Company Team Merge
developers = [
    "Anirudh",
    "Rahul"
]

testers = [
    "Ammu",
    "Arjun"
]

developers.extend(testers)
print(developers)

#bonus : 
employees = [
    "Anirudh",
    "Ammu",
    "Rahul"
]

# Arjun joins.
# Rahul resigns.
# Find how many employees are there now.
# Print employee list in reverse order.

employees.append("Arjun")
employees.remove("Rahul")
print(len(employees))
employees.reverse()
print(employees)

#Tupple
thisTupple = ("Apple" , "Orange" , "mango")
print(thisTupple)

thisTupple = ("Apple" , "Orange" , "mango" , "Apple")
print(thisTupple)
print(len(thisTupple))

thistupple = ("apple" ,)
print(type(thistupple))

thistupple = ("apple")
print(type(thistupple))

#tuple constructor
thistuple = tuple(("hello" , "hi" , "hey"))
print(thistuple)
print(type(thistuple))

#Accessing elements
print(thistuple[2])
print(thistuple[-1])

#Accessing Multiple elements
print(thistuple[0:2])

#without starting index
print(thistuple[ : 2])

#without end Index
print(thistuple[0 : ])

#negative indexing
print(thistuple[-3 : -1])

thistuple = tuple(("hello" , "hi" , "hey"))

if "hello" in thistuple :
    print("hello Welcome")
else:
    print("didnt found!")

#Update Tuple
mainTuple = ("swiss" , "corso", "Casio" , "titan")

#want to add a new element at th position of casio
listing = list(mainTuple)
listing.insert(2, "Seiko")
listing.append("Armour")
print(listing)

tupling = tuple(listing)
print(tupling)

#Task 1 append watermelon
a=("apple" , "banana", "cherry", "Orange")

listing = list(a)
listing.append("Watermelon")

tupling = tuple(listing)
print(tupling)

#task 2 to remove the cherry
a=("apple" , "banana", "cherry", "Orange")

listing = list(a)
listing.remove("cherry")

tupling = tuple(listing)
print(tupling)

#sets
thisSets = {'apple' , 'orange', 'mango',}
print(thisSets)

duplicateSets = {'apple' , 'orange', 'mango', 'apple'}
print(duplicateSets)

setsCheck = {True , False , 1 , 0}
print(setsCheck)
print(len(setsCheck))
print(type(setsCheck))

sets_1 = set(('albin' , 'eric' , 'joan'))
sets_1.add("Gavi")
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
sets_2 = {'Gk' , 'Lmf' , 'rmf'}
sets_1.update(sets_2)
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
sets_1.remove('albin')
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
# sets_1.remove('noun')
sets_1.discard("noun")
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
random = sets_1.pop()
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
sets_1.clear()
print(sets_1)

sets_1 = set(('albin' , 'eric' , 'joan'))
del sets_1


set1 = {'messi' , 'alvarez' , 'montiel'}
set2 = {'miami' , 'atletico' , 'lyon'}
# set3 = set1.union(set2)
set3 = set1 | set2 
print(set3)

set1 = {'messi' , 'alvarez' , 'miami'}
set2 = {'miami' , 'atletico' , 'lyon'}
# set3 = set1.intersection(set2)
set3 = set1 & set2
print(set3)

#Tuple Excersise

# Task 1
employee = (
    101,
    "Anirudh",
    "Developer",
    25000
)

print(employee[0])
print(employee[1])
print(employee[3])

# Exercise 2: Product Details
product = (
    "iPhone 17",
    150000,
    "Apple"
)

print(product[0])
print(product[1])
print(product[2])

#Exercise 3: GPS Tracking System
location = (
    8.8932,
    76.6141
)

print(location[0])
print(location[1])

#Exercise 4: Company Server
server = (
    "192.168.1.1",
    8080
)

print(server[0])
print(server[1])

#Exercise 5: Movie Information
movie = (
    "Interstellar",
    2014,
    8.7
)

print(movie[0])
print(movie[1])
print(movie[2])

#SET EXERCISES
