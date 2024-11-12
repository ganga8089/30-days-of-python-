'''
name:ganga
date:12-11-2024
version1.1
Python program that accepts the user's first and last name and prints them in reverse order.
'''
first_name=input("Enter your first name:")
last_name=input("Enter your last name:")
Full_name=first_name + last_name
print(f"Your name in reverse order is {Full_name[::-1]}")