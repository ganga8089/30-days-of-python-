'''author:Joswin Shaju
date:21/11/24
print colours which are not in the other list'''

colour_list_1=[]
colour_list_2=[]
limit1=int(input("enter the limit:"))
for i in range(limit1):
    colour1=input("enter the colours in list1:")
    colour_list_1.append(colour1)
limit2=int(input("enter the limit:"))
for j in range (limit2):
    colour2 = input("enter the colours in list2:")
    colour_list_2.append(colour2)
unique=[]
for i in colour_list_1:
    if i not in colour_list_2:
        unique.append(i)

print(colour_list_1)
print(colour_list_2)
print(unique)