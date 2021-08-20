#!/usr/bin/env python3

import time #to time sleep function
import random #for words to randomly be selected
name = input("What is your name? ")
print ("Hello " + name,","  "Time to play guess it!")
time.sleep(1)
print ("Start guessing...\n")
time.sleep(0.5)
## A List Of Secret Words
words = ['romance','comedy','action','adventure','classic','horror']
word = random.choice(words)
guesses = ''
turns = 6
#play hangman for x amount tries until failure 
while turns > 0:         
    failed = 0
#if character is guessed correctly, letter will print for the word that was randomly selected
    for char in word:      
        if char in guesses:     
            print (char,end="")    
        else:
            print ("_",end=""),     
            failed += 1
#if you finished without failing you win            
    if failed == 0:        
        print ("\nYou won") 
        break
#have the player guess a letter
    guess = input("\nguess a character:") 
    guesses += guess                    
    if guess not in word:  
        turns -= 1
#print how many guesses are left
        print("\nWrong")    
        print("\nYou have", + turns, 'more guesses') 
        if turns == 0:           
            print ("\nYou Lose") 
