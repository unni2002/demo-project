x={"name":"athira","age":23,"place":"airapuram","hobby":"playing"}
print(x)
print(x["age"])
print(x.get("place"))
print(x.keys())
print(x.values())
print(x.items())
print("age" in x)
print("place" not in x)
for i in x:
    print(i)
for i in x:
    print(x[i])
for i in x.keys():
    print(i)
for i in x.values():
    print(i)
for i in x.items():
    print(i)
x["name"]="kunji"
print(x)
x.update({"age":21})
print(x)
x["gender"]="female"
print(x)
x.update({"qualification":"b tec"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("qualification")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)
#del x