#logical operator
is_Admin = "Available"
admin_Status = "online"

#Logical And

if is_Admin == "Available" and  admin_Status == "online" :
    print("You can Access")

else:
    print("You cant Access")

#Logical Or

if is_Admin == "Available" or admin_Status == "online" :
    print("You can Access")

else:
    print("You cant Access!")

#Logical Not

if is_Admin == "Available" and not admin_Status == "online" :
    print("You can Access")

else:
    print("You cant Access")

# Arithemetic Operators
#calculate Employee Monthly income based on daily wages

daily_wage = 675
total_working_days = 22

monthly_income = daily_wage * total_working_days
print(monthly_income)

#calculate Emi Amount
Product_price = 30000
tenure = 10

monthly_emi = Product_price / tenure
print(monthly_emi)

#Area of rectangle 
length = 150 
breadth = 20

area_of_rectangle = length * breadth
print(area_of_rectangle)

#convert Hours into Min
min_seconds = 60
hour = 2

converting = hour * min_seconds 
print(converting)

#average of 5 Numbers
mark1 = 15
mark2 = 20
mark3 = 30
mark4 = 56
mark5 = 75

sum = mark1 + mark2 + mark3 + mark4 + mark5 
average = sum / 5

print(average)

#Comparison Operator
# Check voting eligibility.
# Find larger of two numbers.
# Check if marks are greater than pass mark.
# Compare two salaries.
# Compare product prices.

#1
age = 20
eligible_age = 18

if age >= eligible_age :
    print("You Are Eligible For Voting")

else:
    print("You are Not Eligible For Voting!")

#2
first_number = 10
second_number = 20

if first_number > second_number :
    print("First Number is Largest")
else:
    print("second Number is Largest")

#3
mark1 = 15
mark2 = 20
mark3 = 30
mark4 = 56
mark5 = 75

total_mark = mark1 + mark2 + mark3 + mark4 + mark5 
Pass_mark = 300

if total_mark >= Pass_mark :
    print("You Passed😊")

else:
    print("You Failed🫤")

#4
girl1_salary = 20000
girl2_salary = 35000

if girl1_salary <= girl2_salary :
   print("Girl1 would be : 😒")
else:
    print("Girl1 Would be : 😋")

#5
Iphone = 150000
samsung = 100000

if Iphone >= samsung :
    print("Iphones are Too expensive")

else:
    print("samsung is bit cheaper")


#Employee Bonus System
salary = 15000
experience = 3

if salary >= 20000 and experience >= 2 :
    print("Eligible For Increment")
else:
    print("Not eligible!")

#Discount System
Order_Amount = 2000

if Order_Amount >= 2000 :
    print("Free Delivery")
else:
    print("Includes Delivery Charge")

#Chat System
last_seen = 5

if last_seen <= 5 :
   print("Online 🟢")
else:
    print("Offline 🍎")

#Movie Ticket Eligibility

age = 15
has_ticket = True

if age > 18 and has_ticket == True:
    print("Eligible for the Movie")
else:
    print("Not eligible")

#Bank Loan Approval

salary = 35000
cibil = 750
is_blacklisted = True

if salary >= 35000 and cibil >= 750 and not is_blacklisted:
    print("Loan Approved")
else:
    print("Loan Denied")


#elif statement
age = 18

if age > 18 :
    print("You became Adult")
elif age < 18 :
    print("You are Minor")

Score = 75

if Score > 90 :
    print("Grade : A")
elif Score >=80 :
    print("Grade : B")
elif Score >= 70 :
    print("Grade : C")
elif Score >=60 :
    print("Grade : D")
 
#else case also included
day = 8

if day == 1 :
    print("Monday")
elif day == 2 :
    print("Tuesday")
elif day == 3 :
    print("Wednesday")
elif day == 4 :
    print("Thursday")
elif day == 5 :
    print("Friday")
elif day == 6 :
    print("Saturday")
elif day == 7 :
    print("Sunday")
else :
    print("A week only contains 7 days")

a = 200
b = 33
c = 500

# if a > b and c > a :
#     print("Both are True")

if a > b or c > a :
    print ("One of this is True")

if not a < b :
    print ("A id less than b")


#nested if
x = 41

if x >= 10 :
    print("X is Greater Than 10")
    if x >= 20 :
        print("X is Greater Than 20!")
    else:
        print("X is not Above 20")


#signal System
color = input("Enter The Colour : ")

if color == 'Red' :
    print("Stop !")
elif color == 'Yellow' :
    print("Be ready")
elif color == 'Green' :
    print("Lets Go")
else :
    print("Invalid Signal")

# Month Finder
month = input("Enter the Month : ")

if month == "1" :
    print("Its January")
elif month == "2" :
    print("Its February")
elif month == '3' :
    print("Its March")
elif month == "4" :
    print("Its April")
elif month == "5" :
    print("Its May")
elif month == "6" :
    print("Its june")
else : 
    print("Invalid Month")

# Login System

username = input("Enter The User Name : ")
password = input("Enter the Password : ")

if username == "Anirudh7884" :
    print("Valid Username")
    
    if password == "12345678" :
      print("Login Successfully")

    else:
        print("Invalid Credentials")

else : 
    print("Login Failed")

# Atm Pin system
Pin = input("Enter the Pin : ")
is_verified = False

if Pin == "1234" :
   is_verified = True
   print("Pin Verified")

   if is_verified == True :
       print("Access Granted")
    
else :
       print("Wrong Pin")

# Voting System
age = int(input("Enter The Age : "))

if age >= 18 :
    print("Can Able to Vote")

    if age > 60 :
        print("Senior Citizen")

else :
    print("Too Young")

# Money Withdrawal

Balance = 20000
amount = int(input("Enter the Amount : "))

if amount > 0 :
    
    if amount <= Balance :
        print("Withdraw sucessfully")
        print("Remaining Balance : ", Balance - amount )

    else : 
        print("Insufficient Balance")
        print("Remaining Balance : ", Balance)

else :
    print("Invalid Amount")

# Student Result
mark = int(input("Enter the Mark : "))

if mark >= 40 : 
    print("pass")

    if mark >= 90 :
        print("A Grade")

    elif mark >= 80 :
        print("B Grade")
        
    elif mark >= 70 :
        print("C Grade")

    elif mark >= 60 :
        print("C Grade")

else:
    print("Failed!")


# Employees Bonus

salary = int(input("Enter your Salary : "))

if salary >= 25000 : 
    print("Eligible For Bonus")

    if salary >= 50000 : 
        print("Bonus 💲20000 ")
    
    else:
        print("Bonus 💲5000")

else :
    print("Not Eligible for Bonus ")

# loan eligibilty

age = int(input("Enter your Age : "))
salary = int(input("Enter your Salary : "))
cibil = int(input("Enter You Cibil Score : "))

if age > 22 and age <= 70 :
    print("Age Eligible")

    if salary >= 25000 and cibil >= 720 :
        print("Loan Eligible")
    
    else:
        print("Loan Not Eligible")

else : 
    print("Age Not Eligible")

