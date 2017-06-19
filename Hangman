# Setup
from __future__ import print_function
import numpy

#Begin Game
print ("Let's play Hangman!")
print(" _____")
print(" |   |")
print(" | ")
print(" | ")
print(" | ")
print("_|_")

# letter bank
letter_bank = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"]

wrong_char = []

# Select word
word = raw_input("Please type a word. ")
# Confirm item
print("The secret word is: " + word)
"""""
# hangman ASCII art
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")
print("    ")


print(" _____")
print(" |   |")
print(" | ")
print(" | ")
print(" | ")
print("_|_")
"""""

def print_hangman(stage):
    if stage == 0:
        print(" _____")
        print(" |   |")
        print(" | ")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 1:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" | ")
        print(" | ")
        print("_|_")

    if stage == 2:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |   |")
        print(" | ")
        print("_|_")

    if stage == 3:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|")
        print(" | ")
        print("_|_")

    if stage == 4:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" | ")
        print("_|_")

    if stage == 5:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  /")
        print("_|_")
        print("One last chance!")

    if stage == 6:
        print(" _____")
        print(" |   |")
        print(" |   o")
        print(" |  /|\\")
        print(" |  / \\")
        print("_|_")
        print("Better luck next time!")


def printBlanks(solution, correctletters):
    # Set solved equal to true (innocent until proven guilty)
    solved = True
    # Loop over each letter in the word
    for l in solution:
        l = l.lower()  # not required but nice to have
        # Check if that letter is in the list of correct letters
        if l in correctletters:
            print (l + " ", end="")# If it is, print the letter and a space
        else:  # Remove "False" and replace it with the appropriate condition
            print ("_ ", end="") # If it isn't, print an underscore and a space
            solved = False # Also, set solved equal to False
    print()
    print()
    return solved

# Define a list to hold the correctly guessed letters
correctLetters  = []

# Define a variable to count the number of incorrect guesses
stage = 0

# Repeat forever, we'll use a break to get out
# Catch Death (Exit loop if they got 6 or more wrong)
while True:
    print_hangman(stage)
    if printBlanks(word, correctLetters):
        print ('You win!')
        break
    if stage >= 6:
        print ("You lose!")
        break
    # Define a variable to hold user input
    l = ''
    while(l == ''):
        l = raw_input("Please enter a letter. ")
    # Loop until they give a letter
    print ("TEST 3")
    # Check if the letter is in the word
    if l in word:  # Replace True with the correct condition
        correctLetters.append(l) # If it's right, put it in the correct letters list and let them know it was right
        print("%s is in the word!" % l)
    else:
        stage = stage + 1
        wrong_char.append(l) # If it's wrong, increment the wrong count and let them know it was wrong
        print("%s is not in the word!" % l)

# Reveal what the word was
print ("The word was " + word)
