# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 19:08:38 2024

@author: prash
"""

#version 1

n= 20
prime_list = []
number_range = set(range(2,n+1))
prime = number_range.pop()
prime_list.append(prime)
multiples = set(range(prime * 2, n+1,2))
number_range.difference_update(multiples)

#version 2


#Upper Bound
n= 100

#Empty List to collect prime numbers
prime_list = []

#number range
number_range = set(range(2, n+1))

#While loop
while number_range:
    prime = number_range.pop()
    prime_list.append(prime)
    multiples = set(range(prime * 2, n+1,prime))
    number_range.difference_update(multiples)


#print prime list
print(prime_list)

#number of primes found
count = len(prime_list)

#Largest of prime numbers
largest_prime = max(prime_list)

print(f"There are {count} prime numbers between 2 and {n} and largest of which is {largest_prime}")

#version 3



def primes_finder(n):
    #Empty List to collect prime numbers
    prime_list = []

    #number range
    number_range = set(range(2, n+1))

    #While loop
    while number_range:
        prime = number_range.pop()
        prime_list.append(prime)
        multiples = set(range(prime * 2, n+1,prime))
        number_range.difference_update(multiples)


    #print prime list
    #print(prime_list)

    #number of primes found
    count = len(prime_list)

    #Largest of prime numbers
    largest_prime = max(prime_list)

    print(f"There are {count} prime numbers between 2 and {n} and largest of which is {largest_prime}")
    
    return prime_list

prime_list=primes_finder(10000000)




