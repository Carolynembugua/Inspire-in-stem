#!/usr/bin/python

###################
#squares
#Name : CAROLYNE MBUGUA
#date : 5/24/2022
###################

squares = [] #empty list
for numbers in range (0,10) :
    square = numbers **2
    squares.append(square)
print(squares) 

#cubes
cubes = [] #empty list
for numbers in range (0,10) :
    cube = numbers **3
    cubes.append(cube)
print(cubes)   

#sum
sum = 0
for numbers in  range (0,10) :
    sum = sum + numbers
print(sum)   

#If statements
Age = 20
if Age >= 18 :
    print("you are allowed to drive")
else:
    print("You are allowed to drive")       

#Write a programme that gets the user input and adds ksh 10,000 to her account if she is between 25 - 30 years    