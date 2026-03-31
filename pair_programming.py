# import math function to use sin and cos
import math

# Functions takes in given polar coordinates (r and theta) and outputs cartesian coordinates (x and y)
def polar_to_cartesian(r, theta):
    x = r*math.cos(theta)
    y = r*math.sin(theta)
    return x,y

# Where to input r and theta
r = float(input("Enter radius (r): "))
theta = float(input("Enter angle in radians (theta): "))

x,y = polar_to_cartesian(r, theta)

# Prints answer to 2 decimal points
print("Cartesian coordinates:")  #looks good, but I would add a space after the : to make easier to read
print(f"x = {x: .2f}")
print(f"y = {y: .2f}")