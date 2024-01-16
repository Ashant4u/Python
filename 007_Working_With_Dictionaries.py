# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 22:17:05 2024

@author: prash
"""

my_dict = {}

planet_dict = {
    "Mercury" : 8,
    "Venus" : 6,
    "Earth" : 5,
    "Mars" : 7,
    "Jupiter": 1,    
    "Saturn" : 2,
    "Uranus" : 3,
    "Neptune": 4
    }

len(planet_dict)

planet_dict["Mars"]
planet_dict["Jupiter"]

planet_dict.get("Mars")

planet_dict.get("Pluto") #NO Message if not present
planet_dict.get("pluto",0) #Default value if not present

planet_dict["Pluto"]#KeyError: 'Pluto'

"Saturn" in planet_dict

planet_dict.keys()
planet_dict.values()

planet_dict["Pluto"] = 9

planet_dict["Uranus"] = 4
planet_dict["Neptune"] = 3


planet_dict.pop("Earth")