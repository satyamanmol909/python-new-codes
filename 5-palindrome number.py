x=input("enter the number to check:")
y=""
for char in x:
    y=char+y
if x==y:
    print(x,"is palindrome ")
else:
    print(x,"is not palindrome")