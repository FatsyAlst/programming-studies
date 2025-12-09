 # ===================================
# MATH TUTOR - MULTIPLICATION PRACTICE
# ===================================
# Scrimba Python 101 Course - Project 2
# An interactive math quiz program that tests multiplication skills
# Tracks score, timing, and provides detailed feedback

# ===================================
# STEP 1: IMPORT REQUIRED MODULES
# ===================================
from random import randrange as r  # Generate random numbers for questions
from time import time as t         # Track how long the quiz takes


# ===================================
# STEP 2: GET QUIZ CONFIGURATION
# ===================================
# Ask user how many questions they want to practice
no_questions = int(input('How many questions do you want?: '))

# Set the difficulty by limiting the maximum number range
# For example: max_num=10 gives multiplication tables up to 10x10
max_num = int(input("Highest number used in practice?: "))


# ===================================
# STEP 3: INITIALIZE TRACKING VARIABLES
# ===================================
# Score counter - tracks correct answers
score = 0

# List to store all questions and answers for review at the end
answer_list = []


# ===================================
# STEP 4: QUIZ LOOP - GENERATE AND ASK QUESTIONS
# ===================================
# Start the timer before first question
start = t()

for q in range(no_questions):
    # Generate two random numbers within the specified range
    # r(1, max_num + 1) gives numbers from 1 to max_num (inclusive)
    num1, num2 = r(1, max_num + 1), r(1, max_num + 1)
    
    # Calculate the correct answer
    ans = num1 * num2
    
    # Ask the user for their answer
    u_ans = int(input(f'{num1} X {num2} = '))
    
    # Store question, correct answer, and user's answer for later review
    answer_list.append(f'{num1} X {num2} = {ans}. You answered {u_ans}')
    
    # Check if answer is correct and increment score
    if u_ans == ans:
        score += 1
    
    # End timer (updates each iteration, final value after last question)
    end = t()


# ===================================
# STEP 5: DISPLAY RESULTS
# ===================================
# Calculate and display comprehensive results
print(f'''Thank you for playing!
You got {score} out of {no_questions}
That is {(score/no_questions)*100}% correct
You took {round(end-start,1)} seconds for it, an average of {round((end-start)/no_questions,1)} per question
''')


# ===================================
# STEP 6: SHOW DETAILED ANSWER REVIEW
# ===================================
# Display all questions with correct answers and user's responses
for a in answer_list:
    print(a)


# ===================================
# EXAMPLE OUTPUT
# ===================================
# How many questions do you want?: 3
# Highest number used in practice?: 10
# 7 X 4 = 28
# 9 X 6 = 54
# 3 X 8 = 25
#
# Thank you for playing!
# You got 2 out of 3
# That is 66.66666666666666% correct
# You took 15.3 seconds for it, an average of 5.1 per question
#
# 7 X 4 = 28. You answered 28
# 9 X 6 = 54. You answered 54
# 3 X 8 = 24. You answered 25


# ===================================
# CONCEPTS USED IN THIS PROJECT
# ===================================
# 1. Module imports with aliases - from random import randrange as r
# 2. random.randrange() - Generating random numbers within range
# 3. time.time() - Measuring elapsed time
# 4. input() with int() - Getting numeric user input
# 5. for loop with range() - Iterating fixed number of times
# 6. Multiple assignment - num1, num2 = r(), r()
# 7. Lists and .append() - Storing data during execution
# 8. String formatting with f-strings - f'{num1} X {num2} = '
# 9. Conditional logic - if statement for checking answers
# 10. Mathematical operations - multiplication, division, percentages
# 11. round() function - Formatting decimal numbers
# 12. Multi-line strings with ''' - Formatted output display
# 13. Loop iteration - for loop to review stored answers


# ===================================
# PROGRAM FLOW
# ===================================
# 1. Import necessary modules (random, time)
# 2. Get configuration from user (question count, max number)
# 3. Initialize variables (score=0, empty answer list)
# 4. Start timer
# 5. Loop through questions:
#    - Generate random numbers
#    - Calculate correct answer
#    - Get user's answer
#    - Store question details
#    - Check if correct and update score
# 6. End timer
# 7. Display summary (score, percentage, time statistics)
# 8. Show detailed review of all questions and answers


# ===================================
# FUTURE IMPROVEMENT CHALLENGES
# ===================================

# CHALLENGE 1: ENHANCED ERROR HANDLING
# -------------------------------------
# Goal: Make the program more robust
# Tasks:
# - Validate numeric input (handle non-integer input)
# - Add minimum question limit (at least 1 question)
# - Handle invalid max_num (ensure it's positive)
# - Add try-except blocks for all input operations
# - Allow user to quit mid-quiz (handle KeyboardInterrupt)
# Skills practiced: Exception handling, input validation, defensive programming

# CHALLENGE 2: IMMEDIATE FEEDBACK WITH USER PREFERENCE
# ------------------------------------------------------
# Goal: Give customizable feedback options
# Tasks:
# - Ask user at start: "Show feedback after each question? (y/n)"
# - If yes: Print "Correct! ✓" or "Wrong! The answer was X ✗" after each answer
# - If no: Only show summary at the end (current behavior)
# - Show running score during quiz if feedback enabled (e.g., "Score: 5/7")
# - Add encouraging messages based on streaks ("3 in a row!")
# - Optional: Use colors (green for correct, red for incorrect) with colorama module
# - Save user's preference for next session (persistent settings)
# Skills practiced: User preferences, conditional feedback, settings management, terminal colors

# CHALLENGE 3: MULTIPLE OPERATION TYPES
# --------------------------------------
# Goal: Practice different math operations
# Tasks:
# - Let user choose operation: +, -, ×, ÷
# - Add "mixed mode" with random operations
# - Handle division (ensure no remainders or accept decimals)
# - Add exponents and square roots for advanced mode
# - Create difficulty levels (easy/medium/hard)
# Skills practiced: Menu systems, multiple algorithms, operation selection

# CHALLENGE 4: TIMED CHALLENGES
# ------------------------------
# Goal: Add time pressure and bonuses
# Tasks:
# - Set time limit per question (e.g., 10 seconds)
# - Award bonus points for fast answers (<5 seconds)
# - Show countdown timer for each question
# - End quiz if time runs out on a question
# - Create "speed round" mode
# Skills practiced: Time management, threading, real-time feedback

# CHALLENGE 5: ADAPTIVE DIFFICULTY
# ---------------------------------
# Goal: Adjust difficulty based on performance
# Tasks:
# - Start easy and increase difficulty with correct answers
# - Decrease difficulty after multiple wrong answers
# - Track which multiplication tables user struggles with
# - Focus practice on weak areas
# - Implement spaced repetition algorithm
# Skills practiced: Algorithm design, adaptive systems, data analysis

# CHALLENGE 6: DETAILED STATISTICS
# ---------------------------------
# Goal: Provide comprehensive performance analytics
# Tasks:
# - Calculate fastest/slowest question times
# - Show accuracy per operation type
# - Track improvement over multiple sessions
# - Create visual progress bars for statistics
# - Export statistics to CSV for analysis
# Skills practiced: Data analysis, statistics, file I/O, visualization

# CHALLENGE 7: LEADERBOARD & PERSISTENCE
# ---------------------------------------
# Goal: Save scores and create competition
# Tasks:
# - Save high scores to JSON file
# - Track multiple users with usernames
# - Display top 10 scores leaderboard
# - Show personal best and average scores
# - Add date/time stamps to all records
# Skills practiced: File I/O, JSON, data persistence, data structures

# CHALLENGE 8: PRACTICE MODES
# ----------------------------
# Goal: Add different quiz formats
# Tasks:
# - "Survival mode": Keep going until first wrong answer
# - "Time attack": Answer as many as possible in 60 seconds
# - "Perfect score": Must get all correct to pass
# - "Marathon mode": 100 questions with breaks
# - "Challenge mode": Increasingly difficult questions
# Skills practiced: Game design, multiple modes, user engagement

# CHALLENGE 9: VISUAL IMPROVEMENTS
# ---------------------------------
# Goal: Make the interface more appealing
# Tasks:
# - Clear screen between questions
# - Add ASCII art for correct/incorrect answers
# - Create progress bar showing quiz completion
# - Add animated countdown timer
# - Display score with visual elements (★★★☆☆)
# Skills practiced: Terminal graphics, ASCII art, user interface design

# CHALLENGE 10: HINTS AND HELP SYSTEM
# ------------------------------------
# Goal: Help users learn, not just test
# Tasks:
# - Allow user to request hint (shows part of answer)
# - Provide explanation when answer is wrong
# - Add "skip question" option (counts as wrong)
# - Show multiplication table for current numbers
# - Create tutorial mode with step-by-step solutions
# Skills practiced: Educational features, user assistance, teaching algorithms

# CHALLENGE 11: OBJECT-ORIENTED REFACTOR
# ---------------------------------------
# Goal: Restructure using OOP principles
# Tasks:
# - Create MathQuiz class with configuration
# - Create Question class for individual problems
# - Create User class with statistics tracking
# - Implement QuizSession class for timing/scoring
# - Use inheritance for different quiz types
# Skills practiced: OOP, classes, inheritance, encapsulation

# CHALLENGE 12: GUI VERSION
# --------------------------
# Goal: Create graphical interface
# Tasks:
# - Build GUI with tkinter
# - Add number pad for quick input
# - Display timer visually
# - Show score with progress bar
# - Create settings panel for configuration
# Skills practiced: GUI programming, event handling, tkinter

# CHALLENGE 13: MULTIPLAYER MODE
# -------------------------------
# Goal: Enable competitive play
# Tasks:
# - Two-player turn-based mode
# - Each player gets same questions
# - Track both players' scores separately
# - Declare winner at the end
# - Add bonus for answering first
# Skills practiced: Multi-user systems, turn management, competition logic

# CHALLENGE 14: WRONG ANSWER ANALYSIS
# ------------------------------------
# Goal: Identify and fix common mistakes
# Tasks:
# - Categorize wrong answers (off by one, digit swap, etc.)
# - Show most common mistakes
# - Create focused review of missed questions
# - Suggest which tables need more practice
# - Generate custom practice sets for weak areas
# Skills practiced: Error analysis, pattern recognition, personalized learning

# CHALLENGE 15: ACHIEVEMENTS SYSTEM
# ----------------------------------
# Goal: Gamify the learning experience
# Tasks:
# - Award badges for milestones (10 correct, 100 questions, etc.)
# - Track streaks (consecutive correct answers)
# - Create achievement categories (speed, accuracy, endurance)
# - Display achievement showcase
# - Save achievements to profile
# Skills practiced: Gamification, motivation design, persistent data

# BONUS CHALLENGE: MOBILE/WEB VERSION
# ------------------------------------
# Goal: Make the quiz accessible anywhere
# Tasks:
# - Create web version with Flask/Django
# - Build mobile app with Kivy/BeeWare
# - Add touch-friendly interface
# - Implement cloud sync for scores
# - Create shareable results on social media
# Skills practiced: Web development, mobile development, full-stack skills

