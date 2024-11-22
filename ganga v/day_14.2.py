'''
name:ganga
datee:22-11-2024
version1.1
Python program that finds all palindromes in the list ['racecar', 'python', 'madam', 'level'].
'''
list=['racecar', 'python', 'madam', 'level']
palindrome_list=[]
for element in list:
    if element==element[::-1]:
        palindrome_list.append(element)
print('palindrome list=',palindrome_list)
