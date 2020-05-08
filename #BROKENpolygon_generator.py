#!/bin/python3
import math
from cpp_pair_stl_mimic import Pair

# reminder    x = radius*cos(theta), y = radius*sin(theta)
# hence    theta = arccos(x/radius) or arcsin(y/radius)


def genXcartesian(radius, angle):
    return radius*math.cos(angle)


def genYcartesian(radius, angle):
    return radius*math.sin(angle)


radius = float(input("Enter the radius of the Circumferting circle: "))

print("Enter the cartesian coordinates of polygon's center (x,y): ")
x, y = float(input()), float(input())

noOfSides = int(input("Enter number of sides of the polygon: "))

# radius = S/2sin(pi/n)
# S = radius*2sin(pi/n)
side = radius*2*math.sin(math.pi/noOfSides)

# the angle between two neighbouring diameters of the polygon
angle = (math.pi*2)/noOfSides
theta = angle
print("\n------------------------")
print("Side length = %d" % side)
print("------------------------\n")

pairXY = Pair(0, 0)  # point pair template and nothing makes more sense than the origin

points = [pairXY]*(noOfSides+1)
for point in range(1, noOfSides+1):
    points[point] = Pair(x + genXcartesian(radius, theta), y + genYcartesian(radius, theta))
    print("Point", point, "(", points[point].first, ",", points[point].second, ")")
    theta += angle  # add proper comment plz


# Points with index-1
# to calculate the slopes duh.😐
prevPoints = [pairXY]*(noOfSides+1)
differences = [pairXY]*(noOfSides+1)

for point in range(1, noOfSides+1):
    prevPoints[point] = Pair(points[point-1].first, points[point-1].second)

    differences[point] = Pair(points[point].first - prevPoints[point].first, points[point].second - prevPoints[point].second)
    #differences[point].first =
    #differences[point].second =

# add comment from cpp version plz
differences[1] = Pair(points[1].first - prevPoints[noOfSides].first, points[1].second - prevPoints[noOfSides].second)
#differences[1].first = points[1].first - prevPoints[noOfSides].first
#differences[1].second = points[1].second - prevPoints[noOfSides].second

#for i in differences:
#    print(i.first)
#    print(i.second)
#    print()
#for i in prevPoints:
#    print(i.first)
#    print(i.second)
#    print()

print("\n------------------------\n")
# comment
slope = None
for point in range(1, noOfSides+1):
    # comment
    if differences[point] == 0:
        print("Side %d Equation: " % point, end="")
        print("y", point, " =", points[point].first)
    # comment
    else:
        slope = differences[point].second / differences[point].first
        print("Side %d Equation: " % point, end="")
        print("y%d = %f*(x - %f) + %f" % (point, slope, points[point].first, points[point].second))
        #print("y", point, " =", slope, "*( x -", points[point].first, ") + ", points[point].second)

# comment
print("\n------------------------\n")
print("Circumferting circle's equation:")
print("(x - %lf)^2 + (y - %lf)^2 = %lf \n" %(x, y, pow(radius, 2)))

## Mafs LOL