class sample:
    x=10
obj=sample()
print(obj.x)

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def myfun(self):
        print("my name is"+self.name)

p1 = Person("veni",22)
p1.myfun()
'''print(p1.name)
print(p1.age)
p2 = Person("minnumon",160)
print(p2.name)
print(p2.age)'''

#inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def printname(self):
        print(self.name, self.age)

class Student(Person):
    pass

x=Student("seetha",50)
x.printname()

