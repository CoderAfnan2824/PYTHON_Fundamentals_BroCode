import math
radius = float(input("Enter radius of circle: "))

c = 2 * math.pi * radius

print(f"Circumference of circle is {round(c,2)}")
# above function will store 2 digits after decimal



# find area of circle
area = math.pi * pow(radius, 2)
print(f"Area of circle with radius {radius} is {area}")