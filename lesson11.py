#!/usr/bin/python

###################
#for,if,while statements                                                        1
#Name : Alexandria Omondi
#date : 5/26/2022
###################

for numbers in range(0,20) :
    if(numbers % 2 == 0 ) :
        print(numbers)

#sum of all even numbers btwn 0 and 50
sum = 0
for numbers in range (0,20) :
    if(numbers % 2 == 0) :
            sum = sum +numbers 
print(sum)            
 
#product of odd numbers btwn 1 and  20
product = 1
for numbers in range (0,20) :
    if (numbers%2 == 1) :
        product = product * numbers
print(product)       

#calculate the factorial of 6.... 6!
#fact = number *  (number - 1)
#n! =  n * (n-1) * (n-2) * (n-3)-------


# < less than
# > greater than
# >= greater or equal to
# <= less or equal to 
# == equal to
# = assignment operator 
# % modulus

num = 0
while  num < 10 : 
    print (num)
    num = num + 1

num = 0
while num < 10 :
    if (num % 2 == 0) :
         print(num)
    num  = num + 1   
