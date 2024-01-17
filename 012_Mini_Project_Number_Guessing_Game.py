# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 21:27:13 2024

@author: prash
"""

#Version 1

CORRECT_NUMBER = 26

user_guess = int(input("What is your guess :"))

if user_guess == CORRECT_NUMBER:
    print("WOW , you got it - great guessing!")
else:
    print("Sorry, your guess is incorrect")
    

#Version 2

CORRECT_NUMBER = 26

while True:
    user_guess = int(input("What is your guess : "))

    if user_guess == CORRECT_NUMBER:
        print("WOW , you got it - great guessing!")
        break
    else:
        print("Sorry, your guess is incorrect")

#Version 3

import random

LOWER_BOUND = 1
UPPER_BOUND = 100
GUESS_COUNTER = 0
GUESS_LIMIT = 5
CORRECT_NUMBER = random.randint(0,100)


print(f"Try Guessing number which I am thinking. It is in between {LOWER_BOUND} and {UPPER_BOUND}.Good luck, You got {GUESS_LIMIT} guesses")
while True:
    user_guess = int(input("What is your guess : "))
    GUESS_COUNTER +=1
    remaining_guesses = GUESS_LIMIT - GUESS_COUNTER
    
    if LOWER_BOUND <= user_guess <= UPPER_BOUND:
        
        if user_guess == CORRECT_NUMBER:
            print(f"WOW , you got it in {GUESS_COUNTER} guesses - Well done!")
            break
        elif user_guess < CORRECT_NUMBER:
            print(f"your guess is too low, try again. Guessess remaining {remaining_guesses} guesses")
        else:
            print(f"your guess is too high, try again. Guessess remaining {remaining_guesses} guesses")
    else:
        print(f"your guess is outside range , try a guess between {LOWER_BOUND} and {UPPER_BOUND}")
        
    if remaining_guesses == 0:
        print(f"Sorry, you are out of guesses. The number you were after was {CORRECT_NUMBER}")
        break

    