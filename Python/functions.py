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
