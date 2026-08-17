#Function()

def helloFunction():
    print("hello From a Function")
helloFunction()

def myName():
    print("Im Anirudh")
myName()

temp = 72 
celsius = (temp - 32) * 5 / 9
print(celsius)

def farenheit_to_celsius(farenheit) :
    celsius = (farenheit - 32 ) * 5 / 9
    return celsius

print(farenheit_to_celsius(72))
print(farenheit_to_celsius(36))

def sum_of_numbers(a , b) :
    sum = a + b
    return sum
print(sum_of_numbers(4,5))

#default value of parameter

def wish_Function(name = "friend") :
    return("hello", name)

print(wish_Function("Anirudh"))
print(wish_Function())

#exersices

def greeting () :
    print("Welcome")
greeting()

#task2
def greet(name):
    print("Welcome", name)

greet("Anirudh")

# task3

def sum(a , b) :

    total = a + b
    print("Total",total)

sum(19,17)

# 👉 Function to find square of a number

def square_num(number):

    square = number * number 
    return square

result = square_num(10)
print("Square - ",result)

# Function to check: even or odd

def number_check(number):
    if number % 2 == 0 :
        print("This is an Even Number")
    elif number % 2 == 1:
        print("This is an odd Number")

number_check(10)


#Average of 3 Number

def average_num (a,b,c) :
    average  = (a + b + c) /3
    return average

print("Average : ",average_num(10,20,30))

# Function Calling Function

def square(number) :
    return number *number

def cube(number):
    return number * number * number

def run(number):
    square_num = square(number)
    cube_num = cube(number)

    print("Square : ", square_num)
    print("Qube :", cube_num)

run(6)

#function for total and average
numbers = [10, 20, 30, 40]

def calculate_total(numbers):
    total = 0

    for number in numbers :
        total += number

    return total

def calculate_average(numbers):
    total = calculate_total(numbers)
    average = total / len(numbers)

    return average

print("Sum of Numbers :", calculate_total(numbers))
print("Average of Numbers :", calculate_average(numbers))

#Function to find the maximum 

numbers = [20, 50, 10, 90, 45, 80]

def calculate_highest(numbers):

    highest = numbers[0]

    for number in numbers:
        if number > highest:
            highest = number 

    return highest

print("Highest Number : ", calculate_highest(numbers))

#function to find the Lowest

numbers = [20, 50, 10, 90, 45, 80]

def calculate_lowest(numbers):

    lowest = numbers[0]
    for number in numbers:
        if number < lowest:
            lowest = number

    return lowest

print("Lowest Number :", calculate_lowest(numbers))

#Even & Odd Counter

numbers = [12, 7, 9, 20, 33, 42, 8, 15]


def odd_even_count(numbers):

 even_count = 0
 odd_count = 0

 for number in numbers:
    if number % 2 == 0:
        even_count = even_count + 1
    else:
        odd_count = odd_count + 1

 return even_count,odd_count

even,odd = odd_even_count(numbers)
total = even + odd

print("Even Count :", even)
print("Odd Count :", odd)
print("Total : ", total)

#function to count above a limit

numbers = [10, 50, 30, 80, 20, 90, 45, 15]

def count_greater(numbers , limit):

    count = 0

    for number in numbers:
        if number > limit:
            count = count + 1

    return count

result = count_greater(numbers , 80)

print('Numbers Greater than 80 :',result) 

#function to count numbers in Range

numbers = [10, 25, 40, 55, 70, 85, 100]

def count_between(numbers , minimum,maximum):

    count = 0

    for number in numbers:
        if number >= minimum and number <= maximum:
            count = count + 1

    return count

result = count_between(numbers,30,80)
print("The numbers in between 30 and 80", result)

# Task 6 — Salary Analyzer 💼

#Tasks
# Total Salary
# Highest Salary
# Lowest Salary
# Number of employers earning more than 30000


salaries = [18000, 25000, 32000, 45000, 21000, 55000]

def calculate_total(salaries):

    total = 0

    for salary in salaries:
        total = salary + total

    return total

def calculate_highest(salaries):

    highest = salaries[0]

    for salary in salaries:
        if salary > highest:
            highest = salary

    return highest

def calculate_lowest(salaries):

    lowest = salaries[0]

    for salary in salaries:
        if salary < lowest:
            lowest = salary

    return lowest

def calculate_higher_count(salaries,limit):

    count = 0

    for salary in salaries:
        if salary > limit:
            count += 1

    return count

result = calculate_higher_count(salaries,30000)


def salary_reports(salaries):

    print("Total Salary : ", calculate_total(salaries))
    print("Highest Salary : ", calculate_highest(salaries))
    print("Lowest Salary : ", calculate_lowest(salaries))
    print("Employers Have more than 30000 :", result)

salary_reports(salaries)
