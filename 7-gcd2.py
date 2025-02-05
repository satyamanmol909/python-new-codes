x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    smaller = y
else:
    smaller = x

for i in range(smaller, 0, -1):
    if x % i == 0 and y % i == 0:
        print("The GCD is:", i)
        break
