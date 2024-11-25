'''
name:ganga
date:25-11-2024
version1.1
Python program to find the list of words that are longer than n from a given list of words.
'''
list_words=[]
number=int(input("Enter a number:"))
string=input("Enter a string:")
word=string.split()
for i in word:
    if len(i)>number:
        list_words.append(i)
print("list of words:",list_words)