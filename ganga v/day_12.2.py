'''
name:ganga
date:20-11-2024
version1.1
Python program to loop to calculate the sum of all numbers in a list.
'''
sum=0
list=[]
while True:
    element=int(input("Enter element:"))
    list.append(element)
    choice=input("Do you want to continue?'y' or 'n':")
    if choice=='n':
        break
print("List=",list)
for number in list:
    sum=sum+number
print("Sum=",sum)
