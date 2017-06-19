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
# lists for words and guesses
word_chars = []
wrong_char = []

# Select word
word = raw_input("Please type a word. ")
# Confirm item
print("The secret word is: " + word)
for letter in word:
    word_chars.append(letter)
    print (word_chars)

# Finds occurences of one letter in the word
def findoccurences(word, letter):
    return [word.count(letter)]

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
# Prints each letter as a space in the word
for letter in word:
    print("_ ", end="")

# Insert letters
stage = 0
while stage < 6 :
    if True:
        if "_ " in word:
            print("Please enter a letter. ")
            letter_guessed = raw_input("Please enter a letter. ")
            while len(letter_guessed) != 1:
                if len(letter_guessed) == 1:
                    if letter_guessed in letter_bank:
                        def print_blanks(word, word_chars):
                            if letter_guessed in word_chars:
                                #  if character is in the word (True)
                                print("%s is in the word!" % letter_guessed)
                                return len(wrong_char)
                                letter_bank.remove(letter_guessed)
                                return stage == len(wrong_char)
                                print(stage=len(wrong_char))
                                print(word.replace("_ ", letter_guessed))
                            else:
                                #  if character is not in the word (False)
                                print("%s is not in the word!" % letter_guessed)
                                letter_bank.remove(letter_guessed)
                                wrong_char.append(letter_guessed)
                                print("_ ", letter_guessed)
                                stage = len(wrong_char)
                                stage += 1
                else:
                    print("You have already used that letter or the character is invalid! Try again.")  # if the character is invalid or already used.
        else:
            if word == word_chars:
                print("You have successfully guessed the word!")
                break

    elif False:
        print(stage == 6)