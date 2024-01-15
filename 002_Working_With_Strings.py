# -*- coding: utf-8 -*-
"""
Created on Mon Jan 15 21:00:30 2024

@author: prash
"""

string1 = "data"
string2 = "science"
string3 = "infinity"

print(len(string1))
string1.index("d")
string3[0] #Indexing
string3[3:6] #Slicing

string1.replace('a', 'o')

print(string1)

string1a = string1.replace('a', 'o') # Replace

print(string1a)

string4 = string1 + '-' + string2 + '-' + string3 #concat

print(string4)
string4.upper()
string4.lower()
string4.title()

string4.split('-')

string4.count('-')

#Error print("Don't know")

print('He  said "One small step for a man"')
print('Don\'t know')
print("He  said \"One small step for a man\"")

#String formatting

my_string = " RED ALERT - Meltdown in Sector 7G. Please contact: Homer"

alert_level = "RED"
errortype = "Meltdown"
sector = "7G"
contact_name = "Homesick"




my_string = f" {alert_level} ALERT - {errortype} in Sector {sector}. Please contact: {contact_name}"

print(my_string)

my_string = " {} ALERT - {} in Sector {}. Please contact: {}".format(alert_level,errortype,sector,contact_name)

print(my_string)






















