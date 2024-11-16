'''author:Joswin Shaju
date:16/11/24
to check if a year is leap year or not'''

year=int(input("enter the year:"))
if year%4==0:
    print(f"{year} is a leap year!!")
else:
    print(f"{year} is not a leap year!!")