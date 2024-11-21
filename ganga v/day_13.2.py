'''
name:ganga
date:21-11-2024
version1.1
Python  program to find sum of factors of a number.
'''
number=int(input("Enter a number:"))
sum=0
for i in range(1,number+1):
    if number % i==0:
        sum+=i
print("Sum=",sum)