import math

circle_area = float(input("Enter area of circle: "))
square_area = float(input("Enter area of square: "))

circle_radius = math.sqrt(circle_area/math.pi)
side_length = math.sqrt(square_area)

circumference = 2 * math.pi * circle_radius
perimeter = 4 * side_length

if (circumference > perimeter):
    print("Circle")
else:
    print("Square")
