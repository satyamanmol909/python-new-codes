x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

if x > y:
    for i in range(y, 0, -1):
        if y % i == 0:
            for j in range(x, 0, -1):
                if x % j == 0:
                    if i == j:
                        print("gcd=",i)
                        break
            break
else:
    for i in range(x, 0, -1):
        if x % i == 0:
            for j in range(y, 0, -1):
                if y % j == 0:
                    if i == j:
                        print("gcd",i)
                        break
            break
