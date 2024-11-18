'''
name:Ganga
date:18-11-2024
version1.1
Python program to accept two numbers and perform the arithmetic operations
'''
print("\t\t\t MENU")
menu='''1)Add
2)Substract
3)Multiply
4)Divide
5)Exponentiation'''
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


