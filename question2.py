import math

# using a function, create a program that calculates the volume of the cylinder.
radius = float(input("Enter the radius of the cylinder: "))
height = float(input("Enter the height of the cylinder: "))
pie = math.pi
volume = pie * radius**2 * height
print(f"volume {volume:.3f}")