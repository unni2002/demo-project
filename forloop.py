x="krishnaveni"
for i in x:
    print(i)
x=["bike","bus","car","train"]
print(x)
for i in x:
    print(i)
y=(1,2,3,4,5)
print(y)
for i in y:
    print(y)
z={"mango","apple","orange","kiwi"}
print(z)
for i in z:
    print(z)
a={"name":"krishnaveni","age":22,"place":"perumbavoor","hobby":"listening music"}
print(a)
for i in a:
    print(a)
for i in a.keys():
    print(i)
for i in a.values():
    print(i)
for i in a.items():
    print(i)
for i in range(11):
    print(i)
for i in range(1,11):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(1,11):
    if i==5:
        break
    print(i)
for i in range(1,11):
    if i==5:
        continue
    print(i)
x=[1,2,3,4]
y=["a","b","c","d"]
for i in x:
    for j in y:
        print(i,j)
a=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in a:
    sum+=i
print(sum)
b=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(1,11):
    if i%2==0:
        sum+=i
print(sum)
c=[1,2,3,4,5,6,7,8,9,10]
sum=0
for i in range(1,11):
    if i%2!=0:
        sum+=i
print(sum)
x=5
factorial=1
for i in range(1,x+1):
    factorial*=i
print(factorial)
n=5
a,b=0,1
for i in range(n+1):
    print(a)
    a,b=b,a+b

