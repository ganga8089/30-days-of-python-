'''
name:Ganga
date:17-11-2024
version1.1
Python program that checks whether a number is within a specified range:
Between 10 and 20 (inclusive),
Between 30 and 40 (inclusive),
Otherwise, print "Out of range".
'''
number=int(input("Enter a number:"))
if number>=10 and number<=20:
    print(f"The given number {number} is between 10 and 20.")
elif number>=30 and number<=40:
    print(f"The given number {number} is between 30 and 40.")
else:
    print("Out of range!!")