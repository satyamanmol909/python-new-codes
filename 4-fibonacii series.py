x = int(input("Enter the last term: "))
a = 0
b = 1
fibonacii=[]
i = 1
while i <= x:
    fibonacii.append(a)
    fib = a + b
    a = b
    b = fib
    i += 1
print(fibonacii)
z=int(input("enter the index to find the value:"))
print(fibonacii[z])