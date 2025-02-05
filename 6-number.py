for i in range(100, 1000):
    z = 0
    sum = 0
    for char in str(i):
        z = int(char)
        sum = sum + z

    if str(i)[0] != str(i)[1] and str(i)[1] != str(i)[2] and str(i)[0] != str(i)[2]:
        if sum% 5 == 0:
            print(i)

