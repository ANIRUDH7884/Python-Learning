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