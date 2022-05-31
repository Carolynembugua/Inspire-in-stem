#!/usr/bin/python


#first n terms of A.P
#a =first_number
#d = steps (common difference)
#n = number of terms

a = int(input("enter first number"))
d = int(input("enter the common difference")) 
n = int (input("enter the number"))
for i in range (1,n+1) :
    n_term = a + (i - 1) * d
    print(n_term)

sum_n = (n_term/2) * ( 2 * a + (n - 1) * d)    
print(sum_n)