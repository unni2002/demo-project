x=["ma","mba","da","msc"]
print(x)
print(type(x))
print(len(x))
print("ma" in x)
print("msc" not in x)
for i in x:
    print(i)
print(x[2])
print(x[2:4])
print(x[3:])
print(x[:4])
print(x[-1])
print(x[-4:-2])
print(x[-4:])
print(x[:-3])
x[3]="ba"
print(x)
x.append("logistics")
print(x)
x.insert(4,"marketing")
print(x)
y=[20000,4000000,50000,10000]
print(y)
x.extend(y)
print(x)
y.sort()
print(y)
y.sort(reverse=True)
z=y.copy()
print(z)
a=list(y)
print(a)
b=x+y
print(b)
print(b.count("mba"))
x.remove("marketing")
print(x)
x.pop(2)
print(x)
x.pop()
print(x)
del x[2]
print(x)
x.clear()
print(x)
del x