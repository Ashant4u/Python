# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 19:18:57 2024

@author: prash
"""

"""
What to do today

if it is sunny
 i will go for a run

"""

weather = "sunny"

if weather == "sunny":
    print("I will go for run")


weather = "cloudy"

if weather == "sunny":
    print("I will go for run")
    

weather = "cloudy"

if weather == "sunny":
    print("I will go for run")
else:
    print("Lets stay in the bed")

weather = "cloudy"

if weather == "sunny":
    print("I will go for run")
elif weather == "cloudy":
    print("Let's hit the gym")
else:
    print("Lets stay in the bed")
    


weather = "sunny"
temp = 20

if weather == "sunny" and temp > 15:
    print("I will go for run")
else:
    print("Lets stay in the bed")

weather = "sunny"
temp = 12

if weather == "sunny" or temp > 15:
    print("I will go for run")
else:
    print("Lets stay in the bed")
    
sunny = True


if sunny:
    print("I will go for run")
else:
    print("Lets stay in the bed")
    
    
i = 4

if i % 2 == 0:
    print(f"{i} is even number")
else:
    print(f"{i} is odd number")