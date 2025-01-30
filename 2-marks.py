"""Write a program to find out whether a student has
 passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. 
Assume 3 subjects and 
take marks as an input from the user. """
s1 = int(input("Enter marks for subject 1: "))
s2 = int(input("Enter marks for subject 2: "))
s3 = int(input("Enter marks for subject 3: "))
fm = int(input("Enter the full marks for each subject: "))

total = s1 + s2 + s3
s1p = (s1 / fm) * 100
s2p = (s2 / fm) * 100
s3p = (s3 / fm) * 100
totalp = (total / (3 * fm)) * 100

if s1p >= 33 and s2p >= 33 and s3p >= 33 and totalp >= 40:
    print("Student has passed.")
else:
    print("Student has failed.")