# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:53:46 2024

@author: prash
"""

my_set = {1,2,3}

my_sett = set([1,2,3])

my_set ={1,2,2,3,4,4,5,6} #Unique values
print(my_set)

my_set[0] # Not Indexed

len(my_set)

my_set.add(9)

my_set.update({22,23,234})

my_set.discard(22)
my_set.remove(22) #Key error if not present

set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.difference(set2)
set2.difference(set1)

set1.difference_update(set2)


set1 = {1,2,3,4,5}
set2 = {3,4,5,6,7}

set1.intersection(set2)
set1.intersection_update(set2)

set1.difference_update(set2)