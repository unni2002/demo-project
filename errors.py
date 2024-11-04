#print(x)
'''try:
    print(x)
except:
    print("an error is there")'''
'''try:
    print(x)
#except NameError:
    print("check the variable")
#except:
    print("an error is there")'''
try:
    print("x")
except:
    print("an error is there")
else:
    print("there is no errors")
finally:
    print("program is successfully completed")

x=int(input("enter a number"))
if x<=0:
    raise Exception("negative numbers are not allowed")