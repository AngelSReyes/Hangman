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

def randomKeywordList():
    """
    Creates a list which has random keywords used to play hangman.
    Shuffles the list and returns the first value in the list.
    """
    keywordList = ["apple", "strawberry", "pineapple", "orange", "banana", "mango", 
                    "passionfruit", "watermelon", "dragonfruit"]
    random.shuffle(keywordList)
    return keywordList[0]


def getLetterFromUser():
    """
    Asks the user to input a letter.
    Returns the letter inputted from user.
    """
    inputtedLetter = input("\n\nPlease enter a letter:\n")
    return inputtedLetter


def checkIfLetterIsInKeyword(inputtedLetter, randomWord, inputtedLetterList):
    """
    Checks that this letter is in the random key word. 
    If yes, add this to the inputtedLetterList which is the list of the inputted letters by the user
    """
    # Check if the user's inputted letter is in the random keyword
    if inputtedLetter in randomWord:
        # if yes then add this to the user's inputted letter list to save and return
        inputtedLetterList.append(inputtedLetter) 
    else:
        if inputtedLetter.isalpha() == False:
            print("This is not a letter, please enter a letter!")
        else:
            if len(inputtedLetter)>=2:
                print("Please only enter 1 letter!")

        print("oh no!")
        
    return inputtedLetterList


def chancesLeftToPlay(usedChances, maxChance,randomWord):
    """
    Increments the usedChances and if this equals the max change return true
    """
    usedChances = usedChances + 1
    maxChance = (len(randomWord)+6)
    if usedChances >= maxChance:
        return True, usedChances
    else:
        return False, usedChances
    
    


def letterPrintOut(randomWord, inputtedLetterList):
    """
    Displays the _ _ _ _ for the keyword.
    """
    print("\nGuess the word: ")

    # Loop every letter in the random keyword 
    for x in randomWord:
        # if the letter is in the key then print this out
        # the end =" " is to ensure that the print doesn't go on a new line 
        if x in inputtedLetterList:
            print(x, end =" ")
        # if not then print a _
        else:
            print("_", end =" ")


""" def letterPositionLister(inputtedLetter,randomWord,inputtedLetterList):
    if inputtedLetter in randomWord:
        inputtedLetterList.append(inputtedLetter)
    letterPositionList=list(map(randomWord.find,inputtedLetterList))
    return letterPositionList  """  



def main():
    print("\n\
            -------------------------------------\n\
            ---- Welcome to Our Hangman Game! ----\n\
            -------------------------------------\n")
    inputtedLetterList=[]
    usedChances = 0
    endgame = False
    randomWord = randomKeywordList()

    while(endgame == False):
        letterPrintOut(randomWord, inputtedLetterList)
        inputtedLetter = getLetterFromUser()
        endgame, usedChances = chancesLeftToPlay(usedChances, (len(randomWord)+2), randomWord)
        inputtedLetterList = checkIfLetterIsInKeyword(inputtedLetter, randomWord, inputtedLetterList)
        print("____________________________________________")

    """
    Needs:
        1. What happens that the user failed the game 
        2. What happens that the user passed the game 
        3. What happens when user inputs a number
        4. What happens when user inputs a special character
        5. What happens when user inputs multiple letters
        6. Make the UI nicer, e.g. have a hangman character, print messages format
        7. What is the user wants to add their own list of keywords
        8. Let the user know what letters theyve already inputted and was wrong
        9. What happens then the user inputs the same correct letter
        10. What happens then the user inputs the same incorrect letter
    """
    
    
    
    
    


if __name__ == "__main__":
    main()