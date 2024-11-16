'''
name:Ganga
date:16-11-2024
version 1.1
Python program using if-else to check whether a given year is a leap year or not.
'''
year=int(input("Enter a year:"))
if year % 4 == 0:
    print(f"The given year {year} is a leap year")
else:
    print(f"The given year {year} is not a leap year")