'''author:Joswin Shaju
date:21/11/24
print the sum of all factors of a numbe'''


sum=0
factors=int(input("enter the number:"))
for num in range (1,factors+1):
    if factors%num==0:
        print(num)
        sum+=num
print("the sum of factors are",sum)

