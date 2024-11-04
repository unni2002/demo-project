x={"name":"krishnaveni","age":22,"place":"perumbavoor","qualification":"ma"}
print(x)
print(type(x))
print(len(x))
print(x["age"])
print(x.get("place"))
print(x.keys())
print(x.values())
print(x.items())
print("age" in x)
print("name" not in x)
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
x["name"]="unni"
print(x)
x.update({"age":23})
print(x)
x["gender"]="female"
print(x)
x.update({"hobby":"listening music"})
print(x)
y=x.copy()
print(y)
z=dict(x)
print(z)
x.pop("gender")
print(x)
x.popitem()
print(x)
del x["age"]
print(x)
x.clear()
print(x)
#del x
family={"child1":{"name":"ammu","age":25},
        "child2":{"name":"paru","age":21},
        "child3":{"name":"achu","age":20}}
print(family)
print(family["child2"])
print(family["child2"]["age"])