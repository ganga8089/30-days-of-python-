'''
name:ganga
date:23-11-2024
version1.1
Python for loop that generates the first 10 numbers in the Fibonacci sequence.
'''
first_number=1
second_number=0
third_number=0
for i in range(10):
    print(third_number,end=" ")
    third_number=first_number+second_number
    first_number=second_number
    second_number=third_number
