"""
Homework 7
>Problem 4
Author: Derrick Unger
Date: 2/29/20
CSC232 Winter 2020
"""

# User Input
code = 0
while code == 0:
    try:
        puzzle = input("\nEnter puzzle: ").upper()
        whiteList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ-& "
        print("\nPuzzle: " + puzzle)

        # Check input validation
        for char in list(puzzle):
            if char not in list(whiteList):
                print("\nInvalid character input, please retry.\n")
                code = 0
                break
            else:
                code = 1

    except:
        print("Error, try again...")


# Hide Characters
hidden = []
for char in list(puzzle):
    if char.isalpha():
        hidden.append("*")
    else:
        hidden.append(char)

print("Puzzle: ", "".join(hidden))


# Ask for User for Guess
code = 0
whiteList2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while code == 0:
    try:
        print("Unused guesses: ", whiteList2)
        guess = input("\nEnter guess: ").upper()

        if guess not in list(puzzle):  # Incorrect Guesses
            print("\nIncorrect guess!\n")
        elif guess not in list(whiteList2):
            print("You already guessed that, or thats not a good guess.")
        else:  # Correct Guesses
            whiteList2 = whiteList2.replace(guess, "")  # Remove guess
            correctGuesses = []
            correctGuesses.append(guess)
            print("Correct guess!")

            # Remove asterisks from correct guesses
            hidden = []
            for char in list(puzzle):
                if char in whiteList2:  # If in remaining guesses, "*"
                    hidden.append("*")
                else:
                    hidden.append(char)
            hidden = "".join(hidden)
            print("Puzzle: ", hidden)

            # If not more asterisks, quit
            if hidden.find("*") == -1:
                code = 1

    except ZeroDivisionError:
        print("Error, try again...")

print("\nPuzzle solved, good job!!\n")
