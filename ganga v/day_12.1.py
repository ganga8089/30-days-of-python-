'''
name:ganga
date:20-11-2024
version1.1
Python program to input numbers from the user to form a list and print that list using for loop.
'''
list=[]
number=int(input("Enter number of iterates:"))
for num in range(number):
    element=int(input("Enter the element:"))
    list.append(element)
print("List=",list)
