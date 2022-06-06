import random
print ('Welcome to password generator')

phone_no = input("enter your phone number")
email = input("enter your email address")
name = input("enter your name")
char = phone_no + email +name 
num_passwords = int(input('numbers of passwords you would like to generate'))
len_passwords = int(input('enter the desired password length'))
print('\n Here are your paasswords :')
for passwords in range (num_passwords) :
    password = ''
    for  c in range (len_passwords) :
         password += random.choice(char)
    print (password)        