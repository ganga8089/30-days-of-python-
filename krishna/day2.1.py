'''12
Write a python program to accept two numbers and divide the second number from the first number and multiply the resultant by square root of second number.
'''

import math
number_1=int(input("enter the first number"))
number_2=int(input("enter the second number"))
final_result=number_2/number_1*(math.sqrt(number_2))
print(final_result)