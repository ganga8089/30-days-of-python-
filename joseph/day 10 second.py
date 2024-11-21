print("1-add")
print("2-substract")
print("3-multiply")
print("4-divide")
print('5-exponential')
choice=int(input("chooose an operation:"))
if choice in [1,2,3,4,5]:
    num1=int(input("Enter first number:"))
    num2=int(input("Enter second number:"))

    if choice==1:
        result=num1+num2
        print(num1,"+",num2,"=",result)
    elif choice==2:
        result=num1-num2
        print(num1,"-",num2,"=",result)
    elif choice==3:
        result=num1*num2
        print(num1,"*",num2,"=",result)
    elif choice==4:
        result=num1/num2
        print(num1,"/",num2,"=",result)
    else:
        result=num1**num2
        print(num1,"**",num2,"=",result)
else:
    print("invalid operation")