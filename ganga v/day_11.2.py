'''
name:ganga
date:19-11-2024
version1.1
Python program to print even numbers up to 50 and their sum.
'''
sum=0
print("Even numbers up to 50:")
for number in range(2,51,2):
    print(number,end=" ")
    sum+=number
print('\n' ''"Sum of even numbers up to 50=",sum)
