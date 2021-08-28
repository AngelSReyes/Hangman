"""
Author          : Ben Fisher and Angel Reyes
Date Created    : 16/08/2021
Date Modified   : 27/08/2021
Version         : 0.2
Description     : Hangman game
History         : 0.1   : File creation
                : 0.2   : Added hangman character for error letters
"""

#Import required libraries
import random       # Randomize the list of key words to guess from

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


def checkIfLetterIsInKeyword(inputtedLetter, randomWord, inputtedRightLetterList, inputtedWrongLetterList):
    """
    Checks that this letter is in the random key word. 
    If yes, add this to the inputtedLetterList which is the list of the inputted letters by the user
    """
    #if the letter is right, it goes in "inputtedRightLetterList", if it isnt, it goes in "inputtedWrongLetterList"
    # "inputtedWrongLetterList" is then used to print the hangman
    # Check if the user's inputted letter is in the random keyword
    if inputtedLetter in randomWord:
        if inputtedLetter in inputtedRightLetterList:
            print("letter has already been inputted and is right, please enter another letter!")
        # if yes then add this to the user's inputted letter list to save and return
        else: 
            inputtedRightLetterList.append(inputtedLetter) 
    else:
        if inputtedLetter in inputtedWrongLetterList:
            print("letter has already been inputted and is wrong, please enter another letter!")
        if inputtedLetter.isalpha() == False:
            print("This is not a letter, please enter a letter!")
        else:
            if len(inputtedLetter)>=2:
                print("Please only enter 1 letter!")

        inputtedWrongLetterList.append(inputtedLetter)
        print("oh no!")
        
    return inputtedRightLetterList



def chancesLeftToPlay(usedChances, maxChance,randomWord,inputtedLetter):
    """
    Increments the usedChances and if this equals the max change return true
    """  
    if inputtedLetter not in randomWord:
           usedChances = usedChances + 1

    maxChance = 6
    if usedChances >= maxChance:
        return True, usedChances
    else:
        return False, usedChances
    
    


def letterPrintOut(randomWord, inputtedRightLetterList):
    """
    Displays the _ _ _ _ for the keyword.
    """
    print("\nGuess the word: ")

    # Loop every letter in the random keyword 
    for x in randomWord:
        # if the letter is in the key then print this out
        # the end =" " is to ensure that the print doesn't go on a new line 
        if x in inputtedRightLetterList:
            print(x, end =" ")
        # if not then print a _
        else:
            print("_", end =" ")

def hangmanPrintOut(inputtedWrongLetterList):
    """
    Displays the hangman character. 
    """
    wrongCount=len(inputtedWrongLetterList)
    print("\n _________\n|         |\n")
    if wrongCount >=1:
        print("|         O\n")
    else:
        print("|\n")
    if wrongCount >=2:
        print("|       / |",end ="")
    else:
        print("|")
    if wrongCount >= 3:
        print(" \ \n")
    else:
        print("\n")
    if wrongCount >= 4:
        print("|        / ",end = "")
    else:
        print("|")
    if wrongCount >= 5:
        print("\ \n |\ \n |_\ ")
    else:
        print("\n|\ \n|_\ ")

   
def wannaPlayAgain(endgame):
    playAgain=input("\n\n would you like to play again? y/n")
    if playAgain == ("y"):
        endgame==False
        return True, endgame
    if playAgain == ("n"):
        return False, endgame
    else: 
        print("please enter y/n")
        playAgain=input("\n\n would you like to play again? y/n")


"""
def winner(randomWord, inputtedRightLetterList,endgame):
    if len(randomWord)==len(inputtedRightLetterList):
        endgame == True
        return True, endgame
    else:
        return False, endgame
"""
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
    inputtedRightLetterList=[]
    inputtedWrongLetterList=[]
    usedChances = 0
    endgame = False
    randomWord = randomKeywordList()

    while(endgame == False):
        letterPrintOut(randomWord, inputtedRightLetterList)
        hangmanPrintOut(inputtedWrongLetterList)
        inputtedLetter = getLetterFromUser()
        endgame, usedChances = chancesLeftToPlay(usedChances, 6, randomWord,inputtedLetter)
        inputtedRightLetterList = checkIfLetterIsInKeyword(inputtedLetter, randomWord, inputtedRightLetterList, inputtedWrongLetterList)
        print("____________________________________________")

    while(endgame == True):
        print("Game Over!!")
        wannaPlayAgain(endgame)

    """
    Needs:
        1. What happens that the user failed the game (almost, tried to make a return loop but it wouldnt reset endgame)
        2. What happens that the user passed the game (struggling, made a winner function but still thinking about how game knows you've won)
        3. What happens when user inputs a number x
        4. What happens when user inputs a special character x
        5. What happens when user inputs multiple letters x
        6. Make the UI nicer, e.g. have a hangman character, print messages format
        7. What if the user wants to add their own list of keywords
        8. Let the user know what letters theyve already inputted and was wrong
        9. What happens then the user inputs the same correct letter x
        10. What happens then the user inputs the same incorrect letter x
        11. Error message for entering no characters
    """
    
    
    
    
    


if __name__ == "__main__":
    main()