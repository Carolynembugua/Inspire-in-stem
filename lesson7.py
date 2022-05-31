#!/usr/bin/python

city = "Mombasa"
print(city[:3])
print(city[-1:])
print(city[5:])

fruits = ["apple","mango","lemon"]
print(fruits[-1])
fruits[1] = 'guava'
print(fruits)


f_name = "sheila mutuku" #small letters
#.upper() convert to upper case
print(f_name.upper())
s_name = "MUMBUA MUTUKU"
#.lower() convert to lower case
print(s_name.lower())

#concatination - converting from one data type to another
# int -> float float x
# float -> int
#int -> string
number = 6
print(str(number))

x = 4 #x is an integer
print(float(x))

y = 3.24
print(int(y))

f_name = "Julie"
s_name = "Atieno"
full_name = f_name + s_name
print(full_name)

name = "Rege Jean"
print(name.replace('g','n'))

name = "Julie Atieno"
print(name.replace('l','t'))

#the split () method returns a list where the text one character with another in a sentence
msg = "hello from Julie Atieno ,how are you"
print(msg.split())

print (len(msg))