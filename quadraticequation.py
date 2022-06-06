from math import sqrt
#!/usr/bin/python

###################
#QUADRATIC EQUATIONS                                                        1
#Name : CAROLYNE MBUGUA
#date : 5/31/2022
###################

#a -> coefficient of first term
#b -> coefficient of second term
#c = coefficient

a = int(input("Enter the coefficient of the first term (a) : "))
b = int(input ("Enter the coefficient of second term (b) : "))
c = int(input("Enter the coefficient (c) : "))
def find_roots(a,b,c) :
    y_1 = (-b - sqrt((b**2) - 4*a*c)) / (2*a)
    y_2 = (-b + sqrt((b**2) - 4*a*c)) / (2*a)
    print("The roots of the quadratic equations are :",y_1,y_2)   
find_roots(a,b,c)   

w = sqrt((b**2)-4*a*c)
def find_roots(a,b,c) :
    y_1 = (-b - w) / (2*a)
    y_2 = (-b + w) / (2*a)
    print("The roots of the quadratic equations are :",y_1,y_2)   
find_roots(a,b,c)   