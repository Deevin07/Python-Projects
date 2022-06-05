# -*- coding: utf-8 -*-
"""
Guess game

@author: Vineet
"""

import random

num = random.randint(1,100)

#rules
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

guesses = [0]

while True:
    
    guess = int(input("Guess the number between 1 to 100 \n  what is the number "))
    
    if guess < 1 or guess > 100:
        print("Out of Bounce please try again")
        continue
    
    if guess==num:
        print(f"Congratulation you have guessed the number in {len(guesses)} Guesses!!")
        break
        
    guesses.append(guess)
    
    if guesses[-2]:
        if abs(num-guess) < (num-guesses[-2]):
            print("Warmer")
        else:
            print("Colder")
            
    else:
        if abs(num-guess)<=10:
            print("WARM")
        else:
            print("COLD")