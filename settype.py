x={"veni","seetha","mikhila","gokul","red"}
print(x)
print(len(x))
print("seetha" in x)
print("mikhila" not in x)
for i in x:
    print(i)
x.add("vismaya")
print(x)
y={"red","orange","black","white"}
print(y)
x.update(y)
print(x)
a=x.union(y)
print(a)
x.intersection(y)
print(x)
z={"dog","cat","elephant","lion"}
print(z)
s={"parrot","dog","crow","lovebirds"}
print(s)
a=z.intersection(s)
print(a)
b=z.difference(s)
print(b)
z.remove("lion")
print(z)
z.discard("cat")
print(z)
z.discard("tiger")
print(z)
z.pop()
print(z)
z.clear()
print(z)
#del z
w=["apple","orange","grapes","watermelon"]
print(w)
w[2]="kiwi"
print(w)
x=frozenset(w)
print(x)
x[3]="guava"
print(x)