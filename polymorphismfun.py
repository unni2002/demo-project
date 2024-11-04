x="python is a programming language"
print(x)
print(len(x))
y=["apple","orange","mango","kiwi"]
print(y)
print(len(y))
z=(1,2,3,4,5)
print(z)
print(len(z))
a={"car","bike","bus","train"}
print(a)
print(len(a))
b={"name":"krishnaveni","age":22,"place":"valayanchirangara"}
print(b)
print(len(b))

#class based polymorphism

class Car:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Driver!")

class Boat:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")

car1 = Car("benz","honda")
boat1 = Boat("cruise","minar")
plane1 = Plane("ethihad","airways")

car1.move()
boat1.move()
plane1.move()
print(car1.brand)
print(car1.model)

