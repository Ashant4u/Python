# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:10:22 2024

@author: prash

while some condition is true:
    do something
    test the condition is still true

"""

i = 1

while i <= 5:
    print(i)
    i = i + 1

i = 1

while i <= 5:
    print(i)
    if i == 3:
        break
    i = i + 1