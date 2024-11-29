'''
krishna
python program that checks whether a number is within a specified range:
'''

number=int(input("Enter a number:"))
if number>=10 and number<=20:
    print(f"The given number {number} is between 10 and 20.")
elif number>=30 and number<=40:
    print(f"The given number {number} is between 30 and 40.")
else:
    print("Out of range")
