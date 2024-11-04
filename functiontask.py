'''a=int(input("enter a number"))
if a%2==0:
    print(a," is even")
else:
    print("a is odd")'''
'''a=8
def even():
    if a%2==0:
        print(a,"is even")
    else:
        print(a, "is odd")
even()'''
'''x=[1,2,3,4,5,6,7,8,9,10]
def sum():
    for i in range(1,11):'''


'''def getSum(num):
 if num == 1:
    return 1
    return num + getSum(num-1)

num = 10
print(getSum(num))'''

'''a=int(input("enter a number"))
def sumofrange(x):
    sum=0
    for i in range(1,x+1):
        sum+=i
    print(sum)
sumofrange(a)'''

'''x=int(input("enter a number"))
def getsum(x):
    sum=0
    for i in range(1,x+1):
        if i%2==0:
            sum+=i
    print(sum)
getsum(x)'''

#factorial
'''x=int(input("enter a number"))
def getsum(x):
    sum=1
    for i in range(1,x+1):
        sum*=i
    print(sum)
getsum(x)'''

#fibanocci
x=int(input("enter a number"))
def sum(x):
    a=0
    b=1
    for i in range(x):
        print(a)
        c=a+b
        a=b
        b=c
sum(x)