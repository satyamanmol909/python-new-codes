x=int(input("enter a number:"))
y=0
i=0
b=0
for j in str(x):
    b+=1
for i in str(x):
    y=(int(i)**b)+y
    print(i,y)
if x==y:
    print(x,"is armstrong number")
else:
    print(x,"is not armstrong number")