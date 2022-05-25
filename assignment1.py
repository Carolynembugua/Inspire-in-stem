#!/usr/bin/python

#area of a circle,surface area of cylinder,volume of a cylinder,volume of cube

#area of a circle 
PI = 3.142
radius = input ("enter radius of circle")
print("the radius of the circle is" + str (radius))
area = PI * int(radius) * int(radius)
print("the area of the circle is" + str(area))

#volume of a cylinder
PI = 3.142
radius = input ("enter radius of cylinder ")
height = input ("enter height of cylinder ")
print("the radius of the cylinder " + str (radius))
print("the height of the cyinder " + str (height))
volume = PI * int(radius) * int(radius) * int(height)
print("the volume of the cylinder is " + str (volume))

#volume of a cube
length = input ("enter length of cube")
width = input ("enter width of cube")
height = input ("enter height of cube")
volume = int(length) * int(width) * int(height)
print("the volume of the cube is " + str (volume))

#surface area of an open cylinder 
PI = 3.142
radius = input ("enter radius of cylinder ")
diameter = input ("enter diameter of cylinder ")
height = input ("enter height of cylinder ")
surfaceArea = PI * int(radius) * int(radius) + PI * int(diameter) * int(height)
print(" the surfaceArea of an open cylinder is " + str (surfaceArea)) 