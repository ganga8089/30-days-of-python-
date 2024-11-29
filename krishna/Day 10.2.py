'''
krishna
python program to accept two numbers and perform the arithmetic operations(+,-,*,**,/)depending on the choice made by the user. You have to display menu to choose
Menu:
1)add
2)substract
3)multiply
4)divide
5)exponentiation
'''

print(menu)
choice=int(input("Enter your choice:"))
number_1=int(input("Enter first number:"))
number_2=int(input("Enter second number:"))
if choice==1:
    result=number_1+number_2
    print("Result of addition:",result)
elif choice==2:
    result=number_1-number_2
    print("Result of substraction:",result)
elif choice==3:
    result=number_1*number_2
    print("Result of multiplication:",result)
elif choice==4:
    result=number_1/number_2
    print("Result of division:",result)
elif choice==5:
    result=number_1**number_2
    print("Result of exponentiation:",result)
else:
    print("Invalid choice")

