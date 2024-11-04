def hello():
    print("hello")
hello()
x=2
y=3
z=x+y
def sum():
    print(z)
sum()
def add(x,y):
    print(x+y)
add(10,20)
def hai(*x):
    print(x[2],x[1])
hai("apple","mango","kiwi","orange")
def hello(x,y,z):
    print(y+z)
hello(y=10,x=20,z=30)
def name(**x):
    print(x["a"])
name(a=2,b=4,c=6,d=8,e=10)
def hello(name="krishnaveni"):
    print(name)
hello("seethalakshmi")
hello()
def hey(x):
    return 10*x
print(hey(20))
def hai():
    pass
