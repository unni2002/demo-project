x="every day brings new choices"
print(x)
print(len(x))
print(x[10])
for i in x:
    print(i)
print(x[5:15])
print(x[10:])
print(x[:20])
print(x[-1])
print(x.upper())
y="  krishna"
print(y)
print(y.strip())
print(x.replace("day","moment"))
X="nothing is impossible. the word itself says i am impossible"
print(X.split("."))
print(x.count("e"))
z=22
a=f"my name is veni i am {z}"
print(a)
z="goodmorning\n have a gud day"
print(z)
print(y.strip())
q="good things, takes time"
print(q)
print(q.split(","))
print(y)
print(type(x))
print(type(y))
print(type(x))
x=5
factorial=1
for i in range(1,x+1):
    factorial*=i
print(factorial)
def addTwo(inp1,inp2):
    total=inp1+inp2
    return total
print(addTwo(5,10))
def sum(N):
    sum=0
    for i in range(n+1):
        sum=sum+i
    print(sum)
n=5
sum(n)

y=13
if y>=5 and y<=20:
    print("yes")
else:
    print("no")

for i in range(1,11):
    if i==5:
        break
    print(i)

for i in range(1,11):
    if i==5:
        continue
    print(i)

def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for character in string:
        if character in vowels:
            count+=1
    return count
string = input("enter a string:")
vowel_count = count_vowels(string)
print("number of vowels: ",vowel_count)


