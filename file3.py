#a=open("unni.txt","x")
#b=open("unni2.txt","x")

a=open("unni.txt","w")
b=open("unni2.txt","w")
txt="good morning,have a nice day"
a.write(txt)
b.write(txt)
a.close()
b.close()
b=open("unni2.txt","r")
d=b.read()
print(d)
b.close()