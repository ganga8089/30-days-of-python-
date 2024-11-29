'''
krishna
python program that assigns a grade based on a student's score using the following criteria:
'''

student_grades=int(input("enter the grade:"))
if student_grades>=90:
    print("Grade:A")
elif student_grades>=80:
    print("Grade:B")
elif student_grades>=70:
    print("Grade:C")
elif student_grades>=60:
    print("Grade:D")
elif student_grades>=50:
    print("Grade:E")
else:
    print("Grade:F")

