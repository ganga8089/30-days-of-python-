'''
name:Ganga
date:18-11-2024
version1.1
Python program to check if a string is a palindrome or not.
'''
str=input("Enter a string:")
str=str.lower()
if str==str[::-1]:
    print("The given string is a palindrome!")
else:
    print("The given string is not a palindrome!")
