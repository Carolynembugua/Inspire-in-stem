#!/usr/bin/python

###################
#   main   ---                                                   
#   Name : CAROLYNE MBUGUA
#   Date : 6/6/2022
###################

import operations
from student import student
from teachers import Teachers

print (operations.add_numbers(5,6))
print (operations.sub_numbers(530,305))
print (operations.mult_numbers(19,5))
print (operations.div_numbers(9,3))

from student import student

new_student = student("cheryl", "swimming","2015",)
print(student.greet_student())

new_teacher = Teachers("Mr Mburu",89764,"Literature",30000) 
print(Teachers.get_tsc_no())

