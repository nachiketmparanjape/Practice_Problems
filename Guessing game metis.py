# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 20:35:06 2016

@author: Nachiket
"""

from random import randint

n = randint(0,100)

choice = 101
attempt = 1
while attempt < 11:
    while 1:
        try:
            choice = (int(raw_input(" Attempt number %s / 10. \nGuess the number between 0 to 100 -\t" %attempt)))
            break
        except ValueError:
            faith = True
            print "Please enter a valid numerical option"
            #Attempt does not get wasted here as it could be mistyped, in case drunk people play this game :P
        
    if choice > 100:
        print "The number is below 100!"
        
    elif choice < 0:
        print "The number is not negative!"
    
    elif choice > n:
        print "Your Guess is too high!"
        
    elif choice < n:
        print "Your Guess in too low!"
        
    elif choice == n:
        print "Congratulations! Correct Guess! You have won!"
        break
    if attempt == 10:
        print "You are out of attempts! You have lost!"
    attempt += 1
    
        