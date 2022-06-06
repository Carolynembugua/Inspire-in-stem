f = open("lesson.txt")

f = open("lesson1.txt",'x')
print (f.readline())

"""

with open (" lesson2.txt",'w') as f :
    f.write("This is my new file\n")
    f.write("This is file \n")
    f.write("I love me\n")
    f.write("today is cold af!\n") 

#reading the file
print(f.read())
f.close()

f.read()
f.seek()
"""