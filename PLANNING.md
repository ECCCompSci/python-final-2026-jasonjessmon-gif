# 📝 Project Planning Worksheet

**Name:** Jason Jessmon  
**Date:** 5/7/2026  
**Project Title:** Number Guessing Game

---

## Step 1 — What will your program do?

*Write 2–3 sentences describing your project. What happens when the user runs it? What will they see or do?*

> The game wil pick a secret number. Then the game will let the user guess at what that secret number is. It will tell them if their guess is too high, too low, or correct.

---

## Step 2 — What will you ask the user?

*List every `input()` question you plan to use.*

1. How many digits do you want the secret number to be?
2. What's your guess for the secret number? It has " + str(digits) + " digits. 
3. Do you want to retry? y/n? 

---

## Step 3 — What variables do you need?

*List the variable names you plan to use and what each one stores.*

| Variable Name | What It Stores | Data Type |
|---------------|---------------|-----------|
| digits| How many digits the user wants the secret number to be| integer|
|calculatedDigits | The highest possible number the secret number could be. | integer|
| secretNumber| The secret number | integer|
| secretNumberGuess| The user's guess at what the secret number is. | integer|
|retryVar |The user's decision of whether they want to play again. | string|
---

## Step 4 — What decisions will your program make?

*Describe each `if/elif/else` check your program will use.*

- If int(secretNumberGuess) == secretNumber, then print "You got it right! The secret number was " + str(secretNumber)
- Elif int(secretNumberGuess) > secretNumber, then print "Wrong! The secret number is lower than that!"
- Else print "Wrong! The secret number is higher than that!"
- If if retryVar == "y" or "Y" or "yes" or "Yes", then guessingGame()
- Else print("OK!")

*(Add more rows if needed.)*

---

## Step 5 — What will the output look like?

*Write out what a sample run of your program might look like. Pretend you are the user.*
Program output here: How many digits do you want the secret number to be? Pick an integer:
User types: 1
Program responds: The game will pick a secret number. Then the game will let the user guess at what that secret number is. It will tell them if their guess is too high, too low, or correct.
What's your guess for the secret number? It has 1 digits.
User types: 5
Program responds: You got it right! The secret number was 5. Thanks for using my program!
