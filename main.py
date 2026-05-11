# ============================================================
# Python Final Project 2026
# Name: 
# Date: 
# Project Title: 
# Description: (Write 1-2 sentences explaining what your program does)
# ============================================================


# ---- SECTION 1: Setup / Variables ----
# Create your starting variables here.
# Example: player_name = ""
import random
digits = input("How many digits do you want the secret number to be? Pick an integer: ")
calculatedDigits = 10**int(digits) -1
secretNumber = random.randint(1, calculatedDigits)
# ---- SECTION 2: Welcome Message ----
# Greet the user and explain what your program does.

print("Welcome!")
print("The game will pick a secret number. Then the game will let the user guess at what that secret number is. It will tell them if their guess is too high, too low, or correct.")



# ---- SECTION 3: Get Input from User ----
# Use input() to ask the user for information.
# Remember: input() always returns a string.
# Use int() or float() if you need a number.

# Example:
# player_name = input("What is your name? ")
# score = int(input("Enter a number: "))
def guessingGame():
    secretNumberGuess = input("What's your guess for the secret number? It has " + str(digits) + " digits. ")

# ---- SECTION 4: Logic (if / elif / else) ----
# Use if/elif/else to make decisions based on user input or variables.
    if int(secretNumberGuess) == secretNumber:
        print("You got it right! The secret number was " + str(secretNumber))
        return
    elif int(secretNumberGuess) > secretNumber:
        print("Wrong! The secret number is lower than that!")
        retry()
    else:
        print("Wrong! The secret number is higher than that!")
        retry()



def retry():
    retryVar = input("Do you want to retry? y/n? ")
    if retryVar == "y" or "Y" or "yes" or "Yes" or "eYs" or "eys":
        guessingGame()
    else:
        print("OK!")


guessingGame()


# Example:
# if score >= 90:
#     print("Great job!")
# elif score >= 70:
#     print("Good work!")
# else:
#     print("Keep practicing!")



# ---- SECTION 5: Final Output ----
# Print a final message, result, or summary to the user.
print("Thanks for using my program!")
