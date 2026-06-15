# #1. Circle

# print("1. Area Of Circle = pir^2 ")
# r = int(input("Enter value of Radius : "))
# pi = 22/7

# CirArea = pi * r**2;

# print("Area of Circle = ", CirArea)

# print("2. Perimeter of Circle = 2pi r")

# CirPeri = 2 * pi * r;
# print("Perimeter of Circle = ", CirPeri)

# print("-------------------------------------------------------")

# #2. Rectangle
# print("1. Areea of Rectangle = l * b")

# l = int(input("Enter value of length : "))
# b = int(input("Enter value of breadth : "))

# RecArea = l * b
# print("Area of Rectangle = ", RecArea)

# print("2. Perimeter of Rectangle = 2(l+b)")
# PeriRec = 2 * (l+b)
# print("Perimeter of Rectangle = ", PeriRec)

# print("-------------------------------------------------------")

# #3. Rhombus
# print("1. Area Of Rhombus = 1/2 (d1*d2)")
# d1 = int(input("Enter value of diagonal d1 : "))
# d2 = int(input("Enter value of diagonal d2 : "))

# RhoArea = 1/2 * (d1 * d2)

# print("Area of Rhombus = ", RhoArea)

# print("2. Perimeter of Rhombus = 4Side")
# RhoSide = int(input("Enter value of Side of Rhombus : "))

# RhoPeri = 4 * RhoSide
# print("PErimeter of Rhombus = ", RhoPeri)

# print("-------------------------------------------------------")

#4. Trapezium 
# print("1. Area of Trapezium = 1/2(a+b)h")
# a = int(input("Enter value of a : "))
# b = int(input("Enter value of b base : "))
# h = int(input("Enter value of h heigth : "))
# TraArea = 1/2 * (a + b) * h
# print("Area of Trapezium = ", TraArea)

# print("2. Perimeter of Trapezium = s1 + s2 + s3 + s4")
# s1 = int(input("Enter value of Side 1 : "))
# s2 = int(input("Enter value of Side 2 : "))
# s3 = int(input("Enter value of Side 3 : "))
# s4 = int(input("Enter value of Side 4 : "))

# TraPeri = s1 + s2 + s3 + s4
# print("Perimeter of Trapezium = ", TraPeri)

# print("-------------------------------------------------------")
# #5. Triangle
# print("1. Area of Triangle : 1/2 (b*h)")
# b = int(input("Enter value of base : "))
# h = int(input("Enter value of height : "))
# TriArea = 1/2 * (b*h)
# print("Area of Triangle = ", TriArea)

# print("2. Perimeter of Triangle : s1 + s2 + s3")
# s1 = int(input("Enter value  of Side 1 : "))
# s2 = int(input("Enter value  of Side 2 : "))
# s3 = int(input("Enter value  of Side 3 : "))

# TriPeri = s1 + s2 + s3
# print("Perimeter of Triangle = ", TriPeri)

print("-------------------------------------------------------")
#6. Cylinder 
print("1. Area of Cylinder : (2 pi r h) + (2 pi r^2)")
pi = 22/7
r = int(input("Enter value of Radius : "))
h = int(input("Enter value of height : "))

CylArea = (2 * pi * r * h) + (2 * pi * r**2)

print("Area of Cylinder = ", CylArea)

print("Perimeter of Cylinder : 4r + 2h")
CylPeri = (4*r) + (2*h)
print("Perimeter of Cylinder = ", CylPeri)