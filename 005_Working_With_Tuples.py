# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 21:39:17 2024

@author: prash
"""

my_list = [ 1, 3.6, "Check"]
my_tuple = ( 1, 3.6, "Check")

x = tuple(my_list)

x= list(x)

#my_tuple.append(4) AttributeError: 'tuple' object has no attribute 'append'

#my_tuple.sort() AttributeError: 'tuple' object has no attribute 'sort'
len(my_tuple)
my_tuple[0]
my_tuple[-1]
my_tuple[1:]
my_tuple.index(3.6)
"Check" in my_tuple