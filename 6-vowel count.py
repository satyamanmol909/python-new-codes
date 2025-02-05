#Write a Python program to count the number of vowels in a string
x=input("enter the string:")
y="aeiou"
count=0
for char in x:
    if char==y:

        count+=1
print(count)
