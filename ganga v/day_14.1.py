'''
name:ganga
date:22-11-2024
version1.1
 Python program that prints the square of each number in the list

'''
list=[]
number_elements=int(input("Enter number of elements in list:"))
for i in range(number_elements):
    element=int(input("Enter the element:"))
    list.append(element)
print("list=",list)
square_list=[]
for number in list:
    square_list.append(number**2)
print("Squared list=",square_list)