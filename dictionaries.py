# a dictionary is  a collection of key value pair. 
#syntax : dictionary =  {'ke'}:{'value'}
#use curly brackets{}
names = ['John','Mary']
colours = {'colour': 'red'} 
vehicle = {'type':'toyota','plate_number':'GT45QX'}
print(colours)
print(type(colours))
print(type(names))
#print(type(names)) # we use the type  method to 
#Accessing values in a dictionary

print(vehicle['type']) # You can access the value of an element inside a dictionary
print(vehicle['plate_number'])

person = {'name':'Ivy nyanjui','phone_number':'0789765432','address':'4490-00100','gender':'non binary'}
person['age'] = '25'
person['fav_colour'] = 'pastel green'
#print(person['name'])
#print(person['phone number'])
#print(person['address'])
#print(person['gender'])
#print(type(person))
print(person)
del person ['phone_number'] 
print(person)
#looping over dictionaries
for key, value in person .items() :
    print(f"{key}:{value}")
