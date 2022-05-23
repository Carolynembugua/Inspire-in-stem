#dictionaries

#!/usr/bin/python

############
#       Dictionaries
#       Name : Tatiana Juma
#       Date : 5/23/2022
######## # use curly brackets 
student = {"Name": "Tatiana","Age":36,"Gender": "Female"}
print(student["Name"])
print(student["Age"])
print(student["Gender"])
student["Id_No"] = "22101034"
student["Hobby"] = "binge watching movies"
student["favourite colour"] = "black"

student = {}
student["fav_food"] = "not yet found"
student["home_city"] = "Mombasa"
print(student)

#Modifying values

student["Name"] = "Claire"
student["Age"] = 20
print(student)

#deleting values
del student["fav_food"]
print(student)