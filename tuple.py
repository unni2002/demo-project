x=(1,2,3,4,5)
print(x)
print(type(x))
print(len(x))
print(2 in x)
print(4 not in x)
print(6 in x)
for i in x:
    print(i)
print(x[4])
print(x[2:5])
print(x[4:])
print(x[:3])
print(x[-1])
print(x[-3:-1])
print(x[-4:])
print(x[:-2])
y=("car","bike","bus","train")
a=x+y
print(a)
a=x*2
print(a)
print(a.count("bus"))
z=list(x)
print(z)
print(type(z))
z.append(6)
print(z)
z.remove(3)
print(z)
x=tuple(z)
print(x)