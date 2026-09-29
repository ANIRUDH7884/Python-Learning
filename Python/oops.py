#class and Object

class human :
    pass

h1 = human()
h1.name = 'Anirudh',
h1.age = 22

#task 1
class students :

 def __init__(self, name, age):
    self.name = name
    self.age = age

 def introduce(self):
    print("Hi, I am", self.name, "and I am", self.age)

student1 = students("Anirudh", 22)
student2 = students("Ammu", 22)
student1.introduce()

print(student2.name)
print(student2.age)

#Bank Excersise
class Bank:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
        else:
            print("Enter amount greater than 0")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter valid amount")
        elif amount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= amount
            print("Withdrawn:", amount)

    def show_balance(self):
        print("Current Balance:", self.balance)


acc1 = Bank("Anirudh T Anil", 7000)

acc1.deposit(500)
acc1.withdraw(8000)
acc1.withdraw(1000)

acc1.show_balance()

