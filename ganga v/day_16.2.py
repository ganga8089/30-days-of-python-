'''
name:ganga
date:25-11-2024
version1.1
Python program to multiply all the items in a list.
'''
number_elements=int(input("Enter the number of elements in the list:"))
list=[]
for i in range(number_elements):
    element=int(input("Enter element:"))
    list.append(element)
print("List=",list)
product=1
for number in list:
    product*=number
print("product of elements in the list:",product)
