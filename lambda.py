x=lambda a,b:a+b
print(x(10,20))
y=lambda a,b,c:a*b*c
print(y(12,4,8))
x=["apple","orange","mango","kiwi"]
y=list(map(lambda a:a.upper(),x))
print(y)
x=[10,20,30,40,50]
y=list(filter(lambda z:z>30,x))
print(y)
a=[1,2,3]
b=list(map(lambda x:x**2,a))
print(b)
z=[1,2,3,4,5,6,7]
v=list(filter(lambda a:a%2==0,z))
print(v)
x=[1,2,3,4,5,6]
b=list(filter(lambda c:c%2!=0,x))
print(b)


