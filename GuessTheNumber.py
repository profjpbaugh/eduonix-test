#!/usr/bin/env python
# coding: utf-8
import random

def runGame():
    #get how many games
    howMany = input('How many games would you like to play?:  ')
    howMany = int(howMany)  #convert to int from string
    count = 0
    
    while count < howMany:
        guessedCorrect = False
        correctGuess = random.randint(1, 26)  #1 inclusive, 26 exclusive
        numGuesses = 0
        while not guessedCorrect:
            userNum = input('Select a random number between 1 and 25:  ')
            userNum = int(userNum)  #cast to integer from string
            numGuesses += 1  #add one for each inner loop iteration
            if(userNum > correctGuess):
                print('your number is too high')
            elif(userNum < correctGuess):
                print('your number is too low')
            else:
                guessedCorrect = True
            
        print('Congratulations, you guessed ' + str(correctGuess) + ' in ' + str(numGuesses) + ' guesses!')
        print('\n')  #extra padding
        count += 1   #outer loop counter
		
runGame()



