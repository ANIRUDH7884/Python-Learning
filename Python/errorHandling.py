# ValueError        → wrong input (abc instead of number)
# ZeroDivisionError → divide by 0
# IndexError        → wrong index
# KeyError          → wrong dictionary key

try :
    square = int(input("Enter the number : "))
    print(square * square)

except:

    print("something went error")

# 🎯 Your task
# Modify your code to:

# ✔ Take number
# ✔ Divide 100 by that number
# ✔ Handle:

# wrong input
# division by zero

try:

    number = int(input("Enter a Number"))
    result = 100 / number
    print("Answer : ", result)

except ValueError:
    print("Enter A Valid Number")

except ZeroDivisionError:
    print("The Number Cant be divided By 0")


# while True:
#  try:

#     number = int(input("Enter a Number"))
#     result = 100 / number
#     print("Answer : ", result)

#  except ValueError:
#     print("Enter A Valid Number")

#  except ZeroDivisionError:
#     print("The Number Cant be divided By 0")


while True:
 
 try:
      Number = int(input("Enter a Number : "))
      result = 100 / Number
      print("Answer : ", result)

 except ValueError:

     print("Invalid Input! Please Enter A Number")

 except ZeroDivisionError:

     print("Cannot divided by 0")
