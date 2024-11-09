'''
author:ganga
version:1.1
date:9-11-2024
python program to find area and perimeter of a given rectangle
'''
length = int(input("Enter length of the rectangle:"))
breadth = int(input("Enter breadth of the rectangle:"))
Area = length * breadth
perimeter = 2 * (length + breadth)
print("Area of the rectangle=", Area)
print("Perimeter of the rectangle=", perimeter)