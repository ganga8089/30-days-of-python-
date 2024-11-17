'''
name:Ganga
date:17-11-2024
version1.1
Python program that assigns a grade based on a student's score using the following criteria:
90 and above: "A"
80 to 89: "B"
70 to 79: "C"
60 to 69: "D"
Below 60: "F"
'''
score=int(input("Enter student's score:"))
if  score>=90:
    print("Grade:'A' ")
elif score>=80:
    print("Grade:'B' ")
elif score>=70:
    print("Grade:'C' ")
elif score>=60:
    print("Grade:'D' ")
else:
    print("Grade:'F' ")