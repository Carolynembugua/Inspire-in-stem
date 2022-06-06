#!/usr/bin/python

###################
#classes                                                       1
#Name : CAROLYNE MBUGUA
#date : 6/2/2022
###################

class Person :
    def __init__ (self,_name,_age) :
        self.name = _name
        self.age = _age
    def sayHi(self) :
        print('Hello my name is ' + self.name + 'and I am' + str(self.age) + 'years old')    
Person1 = Person('Ivan',18)
Person1.sayHi()
Person2 = Person('Faith',20)
Person2.sayHi
