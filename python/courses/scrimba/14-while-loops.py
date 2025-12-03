# Scrimba Python 101 - Exercise 14: While Loops
#
# Topic: While Loop Control Flow and Iteration
# This exercise demonstrates while loops for creating a number guessing game,
# showing multiple implementations with increasing complexity and features.
#
# Key Concepts:
# - while loop continues while condition is True
# - Loop counter variable (attempts) tracks iterations
# - break statement exits loop early
# - Nested conditionals inside loop body
# - += operator increments counter
# - try-except for error handling (in commented version)
# - while-else: else block executes if loop completes without break

print('Guessing game')
# Guess the correct number in 3 guesses. If you don’t get it right after 3 guesses you lose the game.
# Give user input box: 1. To capture guesses,
# print(and input boxes) 1. If user wins 2. If user loses
# Tip:( remember you won’t see  print statements durng execution, so If you want to see prints during whle loop, then print to the input box

# Modification 1: number 1-100, tell user if guess is too high/low ,and let them have 5-10 guesses.
# Tip:( remember you won’t see  print statements during execution, so If you want to see prints during whle loop, print to the input box (This is specific to this platform)
# Three Loop Questions:
# 1. What do I want to repeat?
#  -> Get user guess and check if correct
# 2. What do I want to change each time?
#  -> Increment attempt counter, provide feedback on guess
# 3. How long should we repeat?
#  -> Until correct guess or attempts exhausted

# ========== VERSION 1: Basic 3-attempt guessing game ==========
# number = '7'  # str: Target number (using string comparison)

# attempts = 1  # int: Counter starting at 1
# while attempts < 4:  # Loop while attempts is less than 4 (gives 3 tries)
#     guess = input('Try to guess the number: ')  # str: User's guess
#     if guess == number:
#         print(f"You got it! The number is {number}")
#         break  # Exit loop immediately on correct guess
#     else:
#         attempts += 1  # Increment counter for next iteration

# if attempts == 4:  # Check if loop ended due to running out of attempts
#     print("Sorry, you used all your attempts but still didn't get it")

# ========== VERSION 2: Extended 10-attempt game with high/low hints ==========
# number = 57  # int: Target number (now using integer)

# attempts = 1  # int: Counter starting at 1
# while attempts < 11:  # Loop while attempts is less than 11 (gives 10 tries)
#     guess = int(input('Try to guess the number: '))  # int: Convert input to integer
#     if guess == number:
#         print(f"You got it! The number is {number}")
#         break  # Exit on correct guess
#     else:
#         attempts += 1  # Increment counter
#         if guess < number:
#             print("Your guess is lower than the actual number")  # Hint: too low
#         else:
#             print("Your guess is higher than the actual number")  # Hint: too high


# if attempts == 11:  # Check if all attempts were used
#     print("Sorry, you used all your attempts but still didn't get it")

# ========== VERSION 3: Complex implementation with feedback in prompts ==========
number = 57  # int: Target number
attempt = 1  # int: Current attempt counter
guess_limit = 7  # int: Maximum allowed attempts
while attempt <= guess_limit + 1:  # Loop with extra iteration for final check
    if attempt == 1:  # First attempt
        guess = int(
            input(f"Attempt {attempt}/{guess_limit}. Try to guess the number: "))
        attempt += 1
    else:  # Subsequent attempts
        if guess == number and attempt != guess_limit + 1:  # Correct guess
            print(f"You got it! The number is {number}")
            break
        elif guess < number and attempt < guess_limit + 1:  # Too low, with attempts remaining
            guess = int(input(
                f"Your guess is lower than the actual number. Attempt {attempt}/{guess_limit}. Try again: "))
            attempt += 1
        elif guess > number and attempt < guess_limit + 1:  # Too high, with attempts remaining
            guess = int(input(
                f"Your guess is higher than the actual number. Attempt {attempt}/{guess_limit}. Try again"))
            attempt += 1

# ========== VERSION 4: Advanced version with random numbers and error handling ==========
# import random

# number = random.randint(1, 100)  # int: Random target between 1-100
# attempt = 1  # int: Attempt counter

# print("Guess the number between 1 and 100!")

# while attempt <= 11:  # Maximum 11 attempts
#     try:  # Error handling block
#         guess = int(input(f"Attempt {attempt}/11 - Your guess: "))

#         if guess == number:  # Correct guess
#             print(f"🎉 You won in {attempt} attempts! The number is, indeed, {number}!")
#             break  # Exit loop on win
#         elif guess < number:
#             print("Higher!")  # Hint: guess too low
#         else:
#             print("Lower!")  # Hint: guess too high

#         attempt += 1  # Increment only on valid input
#     except ValueError:  # Handle non-numeric input
#         print("Please enter a valid number!")
# else:  # while-else: executes if loop completes without break
#     print(f"Game Over! The number was {number}")
