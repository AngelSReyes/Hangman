"""
Author          : Ben Fisher and Angel Reyes
Date Created    : 16/08/2021
Date Modified   : 17/08/2021
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
    letter = input("Please enter a letter:\n")
    print("You entered: " + letter)
    return letter
    

def checkIfLetterIsInKeyword(letter, randomWord):
    if letter in randomWord:
        print("yes this letter is in the keyword!")
    else:
        print("oh no!")



def letterpositionlister(letter,randomWord,letterlist):
    letterlist.append(letter)
    letterpositionlist=list(map(randomWord.find,letterlist))
    return letterpositionlist 

def letterprintout(letter,randomWord,letterpositionlist,letterlist):
    forstop=len(letterlist)
    wordreadout=list("#" *len(randomWord))
    if letter in randomWord:
        for x in range(0,(forstop)):
          wordreadout[letterpositionlist[x]]=letterlist[x]
        wordreadout="".join(wordreadout)
    return print(wordreadout)  
        


def main():
    print("Welcome to our game!")
    letterlist=[]
    randomWord = randomKeywordList()
    letter = getLetterFromUser()
    letterpositionlist=letterpositionlister(letter,randomWord,letterlist)

    checkIfLetterIsInKeyword(letter, randomWord)
    letterpositionlister(letter,randomWord,letterlist)
    letterprintout(letter,randomWord,letterpositionlist,letterlist)
    getLetterFromUser()
    checkIfLetterIsInKeyword(letter, randomWord)
    letterpositionlister(letter,randomWord,letterlist)
    letterprintout(letter,randomWord,letterpositionlist,letterlist)
    getLetterFromUser()
    checkIfLetterIsInKeyword(letter, randomWord)
    letterpositionlister(letter,randomWord,letterlist)
    letterprintout(letter,randomWord,letterpositionlist,letterlist)


    
    
    
    


if __name__ == "__main__":
    main()