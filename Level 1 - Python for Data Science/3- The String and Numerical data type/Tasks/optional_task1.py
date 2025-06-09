#The math library can be imported to use the sqrt() function
import math

side1 = float(input("Enter the lenght of the first side of the triangle:"))
side2 = float(input("Enter the lenght of the second side of the triangle:"))
side3 = float(input("Enter the lenght of the third side of the triangle:"))

s = (side1 +side2 + side3) / 2
# area = (s * (s - side1) * (s - side2) * (s - side3))**0.5 - alternative solution that does not require the sqrt() function
area = math.sqrt((s * (s - side1) * (s - side2) * (s - side3)))
print(f"The area of the triangle is:{area}")