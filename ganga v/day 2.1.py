'''
name:ganga
date:10-11-2024
version:1.1
python program to accept two numbers and divide second number with first number and multiply the resultant with square root of second number.
'''
import math
number_1 = int(input("Enter first number"))
number_2 = float(input("Enter second number"))
final_result = number_2/number_1*(math.sqrt(number_2))
print(final_result)
