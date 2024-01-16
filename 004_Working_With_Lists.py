# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 20:49:26 2024

@author: prash
"""

list1 =[]
type(list1)

list1 = list()

list1 = [1, 255.55, "Python", 400000, True]
print(list1)

len(list1)

#Accessing elements and slicing

list1[0]
list1[3]

#list1[5] Index  out of range

list1[-1]
list1[-2]

list2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(list2))

#print(list2[start:end])
#print(list2[:end])
#print(list2[start:])

print(list2[4:7])
print(list2[4:])
print(list2[:4])


list2[-4:-1]



#Adding elements

planets = ["Mercury","Venus","Earth"]

print(planets)

planets.append("Jupiter")
print(planets)
planets.insert(3, "Mars")
print(planets)

outer_planets =["Saturn","Uranus","Neptune","Pluto"]

planets.extend(outer_planets)
print(planets)
[1,2,3] + [4,5,6]

#Removing elements
planets.remove("Pluto")
print(planets)

del planets[2]
print(planets)

planets.pop(2)

#Finding index of element

planets.index("Mercury")
planets.index("Earth")
#planets.index("Tatooin") value error

"Earth" in planets
"Tatooin" in planets

#sorting list
planets.sort()
print(planets)
planets.sort(reverse=True)
print(planets)

#copying list

list1 = [1,2,3]
list2 = list1

print (list1)
print (list2)

list2.append(4)
print (list1)
print (list2)



list1 = [1,2,3]
list2 = list1.copy()



list2.append(4)
print (list1)
print (list2)































