mark=int(input("Enter the mark:"))
if mark>=90:
    print("Grade A")
elif 80<=mark<=89:
    print("Grade B")
elif 70<=mark<=79:
    print("Grade C")
elif 60<=mark<=69:
    print("Grade D")
else:
    print("Failed")