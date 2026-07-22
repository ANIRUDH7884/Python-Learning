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

#copy()
copyList = ["anirudh" , "ammu"]
myList = copyList.copy()
print(myList)

#eXCERSISE

#Create a list of 5 mobile brands and print it.
mobiles = ["samsung" , "Iphone" , "Oneplus", "Vivo" , "Oppo"]
print(mobiles)

#Create a list of 5 employee salaries.
employers_salary = ["15000" , "30000" , "5700" , "67900" , "45609"]
print(employers_salary)

