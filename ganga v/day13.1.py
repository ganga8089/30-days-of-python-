'''
name:ganga
date:21-11-2024
version1.1
Python program that prints out all colors from color_list_1 that are not present in color_list_2.
'''
color_list_1=[]
while True:
    color=input("Enter colour:")
    color_list_1.append(color)
    choice=input("Do you want to continue? y or n")
    if choice=='n':
        break
color_list_2=[]
while True:
    color=input("Enter colour:")
    color_list_2.append(color)
    choice=input("Do you want to continue? y or n")
    if choice=='n':
        break
print("Colour_list_1=",color_list_1)
print("Colour_list_2",color_list_2)
list=[]
for i in color_list_1:
    if i not in color_list_2:
        list.append(i)
print("Colours in list1 that is not present in list2",list)