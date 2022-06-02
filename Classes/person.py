
###################
#classes                                                  1
#Name : CAROLYNE MBUGUA
#date : 6/2/2022
###################
class Person :
    def __init__(self,_name,_age) :
        self.name = _name
        self.age = _age

    def sayHello (self) :
        print('Hello,my name is' + self.name + 'and I am' +str(self.age) +"years old")
person1 = Person('Ian', 18)
person1.sayHello()
person2 = Person('Faith',20)
person2.sayHello()