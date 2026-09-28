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