#Learning about lists
motorcycle_owner = "Joy Mwaura"
plate_number = ['H2134','Y1234','S1234']
motorcycle = ['honda','yamaha','suzuki']
motorcycle = "yamaha"
#print(motorcycle + plate_number)

motorcycle = ['honda', 'yamaha', 'suzuki']
print(motorcycle)

#Accessing list items using index
#print(motorcycle
motorcycle[1] = "Bugatti" #changing element in a list
#print(" I love " + str (motorcycle[1]))

#Adding an element in a list
motorcycle.append('Bugatti') #adding an item to a list
print(motorcycle)
#task --- print the motorcycle and their plate number

#deletion of an item from a list --del
del motorcycle[2] #deleting an item from the list
print(motorcycle)

popped_motorcycle = motorcycle.pop()
print(motorcycle)
#My name is Joy Mwaura and I own a a motorcycle plate number
p_statement = (f"My name is {motorcycle_owner} and I own {motorcycle[1]} plate number {plate_number[0]}")
print(p_statement)

#Removing an item from a list
motorcycle.remove('Bugatti')
print(motorcycle)

school = ['Joy','Hope','Mercy','Mary']
pupil = [ 'Peace','Patience','Amani','Charles']
for pupil in pupil :
    print(f'Hello I am {pupil}')
