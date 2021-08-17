"""
Author          : Ben Fisher and Angel Reyes
Date Created    : 16/08/2021
Date Modified   : 
Version         : 0.1
Description     : Hangman game
History         : 0.1   : File creation
"""

#Import required libraries
import random

def exampleFunction():
    """
    Example function description
    """
    exampleVariable = "Hello world!"
    return exampleVariable


def randomKeywordList():
    keywordList = ["apple", "strawberry", "pineapple", "orange", "banana"]
    random.shuffle(keywordList)
    return keywordList[1]


def getLetterFromUser():
    letter = input("\n\nPlease enter a letter:\n")
    print("You entered: " + letter)
    return letter


def checkIfLetterIsInKeyword(letter, randomWord):
    if letter in randomWord:
        print("yes this letter is in the keyword!")
    else:
        print("oh no!")

def displayUserKeyword(randomWord, inputLetterList):
    len(randomWord)
    print("Found so far: ")
    for x in range(len(randomWord)):
        print("_", end =" ")

    



def main():
    print("Welcome to our game!\n")
    inputLetterList = []
    randomWord = randomKeywordList()

    displayUserKeyword(randomWord, inputLetterList)
    letter = getLetterFromUser()
    checkIfLetterIsInKeyword(letter, randomWord)
    displayUserKeyword(randomWord, inputLetterList)

    




if __name__ == "__main__":
    main()