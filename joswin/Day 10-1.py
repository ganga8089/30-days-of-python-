'''author:Joswin Shaju
date:18/11/24
check if the given string is a palindrome '''

str=input("enter the string:")
palindrome=str[::-1]
if str==palindrome:
    print(f"{str} is a palindrome!")
else:
    print(f"{str }is not a palindrome")