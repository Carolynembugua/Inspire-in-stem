#!/usr/bin/python

#fact = number *  (number - 1)
#n! =  n * (n-1) * (n-2) * (n-3)-------

number =int(input("enter the number"))
factorial = 1
if   (number) < 0 :
    print("Factorial of negative numbers does not exist")
elif  (number) ==  0 :
    print("Factorial of 0 = 1")  
else :
    for i in range (1 ,(number ) + 1) :   
        factorial = factorial * i
print("Factorial of number :",factorial) 

