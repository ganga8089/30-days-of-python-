'''author:Joswin Shaju
date:02/12/24
print palindrome in a list'''

palindrome=[]
list=['racecar','python','madam','level']
for word in list:
    if word==word[::-1]:
        palindrome.append(word)
print(palindrome)
