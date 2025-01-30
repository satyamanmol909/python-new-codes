#program of calculator
x=float(input("enter the first number:"))
y=float(input("enter the second  number:"))
c=input("enter the operator as (+,-,*,/,%):")
if c=='+':
    print("sum=",x+y)
elif c=="-":
    print("subtract=",x-y)
elif c=='*':
    print("product=",x*y)
elif c=='%':
    print("mudulo=",x%y)
elif c=='/':
    print("quotient=",x/y)
