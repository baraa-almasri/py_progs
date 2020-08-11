#!/bin/python3
import math
from cpp_pair_stl_mimic import Pair

# reminder    x = radius*cos(theta), y = radius*sin(theta)
# hence    theta = arccos(x/radius) or arcsin(y/radius)


def genXcartesian(radius, angle) -> float:
    return radius*math.cos(angle)


def genYcartesian(radius, angle) -> float:
    return radius*math.sin(angle)


radius = float(input("Enter the radius of the Circumferting circle: "))

print("Enter the cartesian coordinates of polygon's center (x,y): ")
x, y = float(input()), float(input())

noOfSides = int(input("Enter number of sides of the polygon: "))

# from r = S/2sin(pi/n)    |  S is the side length
# we got S = r*2sin(pi/n)  |    for future confusion
side = radius*2*math.sin(math.pi/noOfSides)

# the angle between two neighbouring diameters of the polygon in radians
angle = (math.pi*2)/noOfSides
theta = angle
print("\n------------------------")
print("Side length = %f" % side)
print("------------------------\n")

pairXY = Pair(0, 0)  # point pair template and nothing makes more sense than the origin

# calculating points' polar coordinates (compared to the center of the polygon),
# then converting them into catesian coordinates(compared to the center of the polygon),
# and adding the coordinates of the center.
# then voila we got the coordinates of the vertices(heads) 🎉🎉

points = [pairXY]*(noOfSides+1)
for point in range(1, noOfSides+1):
    points[point] = Pair(x + genXcartesian(radius, theta), y + genYcartesian(radius, theta))
    print("Point", point, "(", points[point].first, ",", points[point].second, ")")
    theta += angle # theta represents sum of angels of the polygon

# also I started indexes with one so the first is the origin (0,0)


# Points with index-1
# to calculate the slopes duh.😐
prevPoints = [pairXY]*(noOfSides+1)
differences = [pairXY]*(noOfSides+1)

for point in range(1, noOfSides+1):
    
    prevPoints[point].first = points[point-1].first
    prevPoints[point].second = points[point-1].second

    differences[point] = Pair(points[point].first - prevPoints[point].first
            , points[point].second - prevPoints[point].second)


# difference between the first and the last point so it's useful for their line
differences[1].first = points[1].first - points[noOfSides].first
differences[1].second = points[1].second - points[noOfSides].second


print("\n------------------------\n")
# finally the slopes and lines equation generation
slope = None

for point in range(1, noOfSides+1):
    # for vertical slopes since you can't devide by zero 🙃
    if differences[point].first == 0:
        print("Side %d Equation: " % point, end="")
        print("y", point, " =", points[point].first)
    # for normal slopes that doesn't involve deviding by zero 🎉
    else:
        slope = differences[point].second / differences[point].first
        print("Side %d Equation: " % point, end="")
        print("y%d = %f*(x - %f) + %f" % (point, slope, points[point].first, points[point].second))
        #print("y", point, " =", slope, "*( x -", points[point].first, ") + ", points[point].second)

# last but not least, I liked to add it, so that every juicable thing is here 👽👽
print("\n------------------------\n")
print("Circumferting circle's equation:")
print("(x - %lf)^2 + (y - %lf)^2 = %lf \n" %(x, y, pow(radius, 2)))

## Mafs LOL