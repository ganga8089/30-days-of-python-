'''
name:ganga
date:23-11-2024
version1.1
 python program that print largest, smallest, second smallest and second largest number in a list.
'''
list=[]
number_elements=int(input("Enter number of elements in list:"))
for element in range(number_elements):
    element=int(input("Enter element:"))
    list.append(element)
print("List=",list)
list.sort()
largest_number=list.pop()
smallest_number=list.pop(0)
print(f"Largest number = {largest_number} and smallest number= {smallest_number}")
second_largest=list.pop()
second_smallest=list.pop(0)
print(f"Second Largest number = {second_largest} and second smallest number= {second_smallest}")

