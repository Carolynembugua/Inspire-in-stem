#!/usr/bin/python

###################
#TUPLES                                                       1
#Name : Alexandria Omondi
#date : 5/31/2022
###################
#muteable - changeable
    #lists[],dictionaries{}

#immuteable - unchangeable
    #tuples()


fruits = ['mango','orange','pineapple','jackfruit']
fruits[2] = 'kiwi'
print(fruits)

#Tuple    
new_fruits = ('guava','apple','banana','pawpaw')
print(new_fruits[2])
#new_fruits[2] = 'mango'
#print(new_fruits)

cars = ('audi','bmw','v.w','toyota')
cars = ('nissan','bmw','v.w','toyota')
print(cars)

fav_foods = ('chicken','spaghetti','biryani')

for fav_food in fav_foods :
    print(fav_food)