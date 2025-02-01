x=int (input("enter the number:"))
def factorial():
    fact=1
    for i in range(1,x+1):
        fact=fact*i
        print(fact)
    return fact
print("factorial of",x,"=",factorial())