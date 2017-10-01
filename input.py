#! /usr/bin/env python

name = input('Name: ')
job = input('Occupation: ')
location = input('Location: ')

print("Hi {0}, being a {1} in {2} must be exciting!".format(name, job, location))

response = input('Is it? ')
if response in ('yes', 'y', 'yeah'):
    print("How exciting!")
elif response in ('no', 'n', 'nope'):
    print("That's too bad!")
else:
    print("Yeah, I thought so too!")
    

num1 = input('Enter a number: ')
num2 = input('Enter another number: ')
print(int(num1) + int(num2))