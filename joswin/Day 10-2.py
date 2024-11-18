'''author:Joswin Shaju
date:18/11/24
do some mathematical calculations'''


calc=int(input("enter your choice-1=add,2=subtract,3=multiply,4=divide,4=exponentiation:"))
num_1=int(input("enter the nunber:"))
num_2=int(input("enter the number:"))
if calc==1:
    addn=num_1+num_2
    print("addition:",addn)
elif calc==2:
    sub=num_1-num_2
    print("subtraction:",sub)
elif calc==3:
    mult=num_1*num_2
    print("multiplication:",mult)
elif calc==4:
    divd=num_1/num_2
    print("division:",divd)
elif num==5:
    expo=num_1**num_2
else:
    print("invalid number")