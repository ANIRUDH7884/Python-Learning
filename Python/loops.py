#For Loop
mobiles = ["Samsung s25" , "iphone 16", "oneplus 13", "Vivo x200", "Oppo find x8"]
for items in mobiles :
    print(items)

#Tuple
watches = ("Casio", "Titan", "Seiko")
for items in watches :
    print(items)

#sets
company = {"Kreo" , "Acer", "zebronics"}
for items in company :
    print(items)

#Dictionary
info = {
    "Name" : "Anirudh",
    "course" : "Data Science",
    "Place" : "Kochi"
}

for x in info.items() :
    print(x)

word = "Bananna"
for x in word :
    print(x)

#Break Statements
iterative1 = ["Task 1" , "Task 2", "Task 3"]
for task in iterative1 :
    print(task)
    if task == "Task 2" :
        print("Task 2 is the Last Task")
        break

#continue
fruits = ["Manago" , "Apple", "Kiwi"]
for x in fruits :
    if x == "Apple" :
        continue
    print(x)

#range
for x in range(10):
    print(x)

for num in range(10 , 200 ,10):
    print(num)
else:
    print("Finished")

#while loop
i = 1
while i < 7 :
    print(i)
    i += 1

#break in while loop
i = 1
while i <= 7 :
    print(i)
    if (i == 3) :
        break
    i += 1

#continue in Whiel loop
i = 0
while i <= 6 :
    i += 1
    if i == 3:
        continue
    print(i)

#else in while loop
i = 0
while i <= 6 :
    i += 1
    if i == 3:
        continue
    print(i)
else:
    print(i, 'finished')

#For loop Excersises -------------------------------------->
mobiles = [
    "Samsung S25",
    "iPhone 16",
    "OnePlus 13",
    "Pixel 10",
    "Nothing Phone 3"
]

for mobile in mobiles :
    print("Available Device" , mobile)

#  6. Exercise 2 — Employee salary filter

# You're developing a payroll system.

salaries = [
    15000,
    32000,
    18000,
    45000,
    28000,
    55000
]

for salary in salaries :
    if salary > 30000 :
        print("Highest Salary : ",salary)

# Print only salaries ₹30,000 or above.

stocks = [5, 0, 12, 0, 3, 8]
for stock in stocks :
    if stock == 0 :
        print("Out Of Stock")
    else:
        print("Available")

# Exercise 1 🟢

# Print employee IDs from:

for Id in range(101 , 106) :
    print("Employee ID : ",Id)

# Exercise 2 🟡 — EMI Payments

# A customer pays:

# emi = 2500

# every month for 6 months.

# Generate:

# Month 1 : 2500
# Month 2 : 5000
# Month 3 : 7500
# Month 4 : 10000
# Month 5 : 12500
# Month 6 : 15000

# Meaning this is the total amount paid by that month.

emi = 2500

for month in range(1 , 7) :
    total_emi = emi * month
    print(month,"month", "=", total_emi,"💲")

# Exercise 3 🔥 — Even Numbers

for evenNumbers in range(2 , 22, 2) :
    print(evenNumbers)

salaries = [18000, 25000, 32000, 21000, 40000]
total = 0

for salary in salaries :
    total = total + salary

print(total)

salaries = [18000, 35000, 22000, 45000, 31000, 19000]

total = 0
count = 0

for salary in salaries :
    total = total + salary
    if salary > 30000 :
      count = count + 1    
print("Total Salary is : ", total )
print("Total Count", count)



# Now let's make the logic harder 🧠

# Imagine an e-commerce system:

# orders = [1200, 5500, 800, 7200, 3000, 9500, 1500]

# Management wants three pieces of information:

# Total Revenue : ?
# High Value Orders : ?
# Low Value Orders : ?

# Rules:

# High Value: order is >= 5000
# Low Value: order is < 5000

# You need three variables:

# total_revenue = 0
# high_orders = 0
# low_orders = 0

# Then process every order using one for loop.

# You will need:

# for
# if
# else
# accumulator
# two counters

# Don't calculate anything manually.

# Expected result:

# Total Revenue : 28700
# High Value Orders : 3
# Low Value Orders : 4


orders = [1200, 5500, 800, 7200, 3000, 9500, 1500]

total_revenue = 0
highest_order = 0
lowest_odrer = 0

for order in orders :
    total_revenue = total_revenue + order

    if order >= 5000 :
        highest_order = highest_order + 1
    else:
        lowest_odrer = lowest_odrer + 1

print("Total Revenew :", total_revenue)
print("Highest Order :", highest_order)
print("Lowest Order :", lowest_odrer)

numbers = [20, 55, 30, 80, 45]
highest_number = numbers[0]

for number in numbers :
    if number > highest_number :
        highest_number = number
print(highest_number)

#Lowest Number
numbers = [20, 55, 30, 80, 45, 10, 65]
lowest_number = numbers[0]

for number in numbers :
    if number < lowest_number:
        lowest_number = number
print("Lowest Number :", lowest_number)

salaries = [18000, 45000, 27000, 62000, 31000, 55000]

lowest = salaries[0]
highest = salaries[0]
total = 0
count = 0

for salary in salaries :
    total = salary + total
    count = count + 1
    average = total / count

    if salary > highest :
        highest = salary
    if salary < lowest :
        lowest = salary

print("Total Salary of Employees :", total )
print("Total Number Of Employees :", count)
print("Highest Salary :", highest)
print("Lowest Salary :", lowest)
print("Average Salary :", average)

#---------------------------------------------------------------------->

#While Loop
