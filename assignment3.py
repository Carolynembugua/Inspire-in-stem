#!/usr/bin/python

#Write a programme that gets the user input and adds ksh 10,000 to her account if she is between 25 - 30 years    


#get user input
age = input("What is your age")
gender = input("What gender are you ? male / female")
acc_bal = 0

if ( int(age)> 25 ) and ( int(age) < 30 ) :
    acc_bal = acc_bal + 10,000
    print("Confirmed you have received ksh 10,000")
else : 
    print("Sorry no money for you")   

#Write a program to withdaw ksh 25,000 if account balance is between ksh 100,000 to 200,000
#30% if acc balance btwn 500,000  and 1M
#Above 1M deduct 15,000