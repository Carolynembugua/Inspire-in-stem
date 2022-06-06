#!/usr/bin/python

###################
#   operations                                                
#   Name : CAROLYNE MBUGUA
#   Date : 6/6/2022
###################

def add_numbers  (x,y) :
    result = x + y
    return result

def sub_numbers(x,y) :
    result = x - y
    return result    

def mult_numbers (x,y) :
    result = x * y
    return result

def div_numbers (x,y) :
    result = x / y  
    return result

class student :
    def __init__(self, name,hobby, year_of_birth) :
        self.name = name
        self.hobby = hobby
        self.year_of_birth = year_of_birth
    def greet_student(name) :
        print("Hello from " + name.title) 