#!/usr/bin/python

###################
#fUNCTIONS                                                       1
#Name : CAROLYNE MBUGUA
#date : 5/31/2022
###################

# it is a block of code which gets executed together

#Defining a function/ initializing
def say_hello() :
    print("Hello from JKUAT")
    x = 4
    y = 7
    z = x +y
    print(z)
say_hello()

def bark() :
    print("dogs bark")
bark()    
def neigh() :   
    print("horses neigh")
neigh()    
def bray() :   
    print("donkeys bray")
bray()    
def moo ():   
    print("cows moo")
moo()

#function to add numbers
def add_numbers(x,y) :
    sum_numbers = x + y
    print("The sum of the numbers is :", sum_numbers)
add_numbers(40,50)
add_numbers(100,400)
add_numbers(1,4)   

 #function to multiply numbers
def products(x,y) :
    prod_nums = x * y
    print("The product of the numbers is :" , prod_nums)
products(40,50)    
products(100,400)
products(1,4)

def print_name(name = "Ivy Wacera") :
    print(name)
print_name("Ivan mwangi")    

#Returning from a function
def get_sum(num1,num2) :
    sum_nums = num1 + num2
    return sum_nums
print(get_sum(7,12))

#function that gets squares of numbers
def powers(number,power) :
    pow_nums = number ** power
    return pow_nums
print(powers(6,4))    

def get_full_name(f_name,s_name) :
    full_name = f_name +"" + s_name
    return full_name.title()
print(get_full_name("Joy" ,"Chomba"))

 #returning a dictionary from a function
def create_full_name(first_name,second_name) :
    person = {'first':first_name,'second':second_name}
    return person
student = create_full_name('Bob','Marley')
print(student)

#Parsing a list in a function
def greet_friends(names):
    for name in names :
        msg = "hello " + name.title() +"!"
        print(msg)
friends = ['sheila','kira','alexa','mwende']
greet_friends(friends)        
