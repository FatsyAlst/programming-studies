# ===================================
# RAFFLE PRIZE PICKER - FINAL PROJECT
# ===================================
# Scrimba Python 101 Course - Final Challenge
# A program that randomly selects winners for a raffle with multiple prizes

# 🏆 Raffle Prize Picker — Challenge Steps
#
# 1. Ask how many people are entering the raffle (at least 3 names).
# 2. Use a loop to collect their names into a list.
# 3. Ask for exactly 3 prize names (in order) and store them in a list.
# 4. Randomly pick 3 different winners from the participant list.
# 5. Print out who wins which prize and make sure the final one
#    is clearly marked as the Grand Prize. 🏆
#
# Hint: Use loops, lists, and a tool that picks random items without repeats.

import random

# ===================================
# STEP 1: GET NUMBER OF PARTICIPANTS
# ===================================
# Collect the number of raffle members with validation
# Requirements: At least 3 members, must be a valid integer

raffle_members = []
while True:
    try:
        num_members = int(input("Please, enter how many members will joining the raffle: "))
        if num_members < 3: 
            raise ValueError
        break
    except ValueError:
        print("Wrong imput format or not enough members (we need 3 at least!). Try again")


# ===================================
# STEP 2: COLLECT PARTICIPANT NAMES
# ===================================
# Loop through and collect each participant's name
# Using strip() to remove whitespace and capitalize() for consistency

for i in range(num_members):
    name = input(f"Enter the {i+1} member name: ").strip().capitalize()
    raffle_members.append(name)


# ===================================
# STEP 3: COLLECT PRIZE NAMES
# ===================================
# Collect exactly 3 prizes in order (1st, 2nd, 3rd place)
# Prizes are stored in the order they are entered

prizes = []
for i in range(3):
    prize = input(f"Enter the prize for the {i+1} place: ").strip().capitalize()
    prizes.append(prize)


# ===================================
# STEP 4: RANDOMLY SELECT WINNERS
# ===================================
# Use random.sample() to pick 3 different winners without replacement
# This ensures no person wins multiple prizes

winners = random.sample(raffle_members, 3)


# ===================================
# STEP 5: COMBINE WINNERS WITH PRIZES
# ===================================
# Use zip() to pair each winner with their corresponding prize
# Creates an iterator of tuples: (winner_name, prize_name)

summary = zip(winners, prizes)


# ===================================
# HELPER FUNCTION: ORDINAL SUFFIX
# ===================================
# Converts numbers to ordinal format (1st, 2nd, 3rd, 4th, etc.)

def get_ordinal(n):
    return f"{n}{'st' if n == 1 else 'nd' if n == 2 else 'rd' if n == 3 else 'th'}"


# ===================================
# STEP 6: DISPLAY RESULTS
# ===================================
# Loop through the winner-prize pairs with index tracking
# Special formatting for the Grand Prize (1st place)
# Using enumerate(start=1) to begin counting from 1 instead of 0

for index, (winner, prize) in enumerate(summary, start = 1):
    if index == 1:
        print(
            f"🏆 {winner} wins the Grand Prize ({get_ordinal(index)} place): {prize}")
    else:
        print(f"{winner} wins {get_ordinal(index)} place: {prize}")


# ===================================
# EXAMPLE OUTPUT
# ===================================
# Please, enter how many members will joining the raffle: 5
# Enter the 1 member name: alice
# Enter the 2 member name: bob
# Enter the 3 member name: charlie
# Enter the 4 member name: david
# Enter the 5 member name: eve
# Enter the prize for the 1 place: car
# Enter the prize for the 2 place: laptop
# Enter the prize for the 3 place: gift card
#
# 🏆 Charlie wins the Grand Prize (1st place): Car
# Alice wins 2nd place: Laptop
# David wins 3rd place: Gift card


# ===================================
# CONCEPTS USED IN THIS PROJECT
# ===================================
# 1. while loop with break - Input validation loop
# 2. try-except - Error handling for invalid input
# 3. for loop with range() - Collecting multiple inputs
# 4. list.append() - Building lists dynamically
# 5. str.strip() - Removing whitespace from input
# 6. str.capitalize() - Formatting names consistently
# 7. random.sample() - Selecting unique random items
# 8. zip() - Combining two lists into pairs
# 9. enumerate(start=) - Tracking index with custom starting point
# 10. f-strings - String formatting with variables
# 11. Tuple unpacking - Accessing tuple elements in loop
# 12. Functions - Creating reusable code (get_ordinal)
# 13. Conditional expressions - Ternary operators for concise logic


# ===================================
# FUTURE IMPROVEMENT CHALLENGES
# ===================================

# CHALLENGE 1: REFACTORING & MODULARITY
# --------------------------------------
# Goal: Make the code more reusable and organized
# Tasks:
# - Extract input validation into a get_valid_number(min_val, max_val, prompt) function
# - Create a get_names(count, item_type) function for collecting multiple names
# - Create a display_results(winners, prizes) function for output
# - Separate concerns: input gathering, processing, output
# Skills practiced: Functions, DRY principle, code organization

# CHALLENGE 2: ENHANCED INPUT VALIDATION
# --------------------------------------
# Goal: Make input handling more robust
# Tasks:
# - Check for duplicate participant names and ask for confirmation
# - Validate that prize names aren't empty strings
# - Handle edge case: number of prizes > number of participants
# - Add option to edit/remove names before drawing
# Skills practiced: Data validation, edge case handling, user experience

# CHALLENGE 3: IMPROVED OUTPUT FORMATTING
# ----------------------------------------
# Goal: Make results more visually appealing
# Tasks:
# - Display all participants first, then reveal winners one by one
# - Add visual separators and better formatting (boxes, colors)
# - Show which participants didn't win
# - Create a results summary table
# - Add time delay between winner announcements for suspense
# Skills practiced: String formatting, user interface design, time module

# CHALLENGE 4: DATA STRUCTURES UPGRADE
# -------------------------------------
# Goal: Use better data structures for complex data
# Tasks:
# - Store participants as dictionaries: {"name": "Alice", "entry_count": 1}
# - Store results as list of dicts: [{"winner": "Alice", "place": 1, "prize": "Car"}]
# - Sort results by place number before displaying
# - Add participant IDs for tracking
# Skills practiced: Dictionaries, data modeling, sorting

# CHALLENGE 5: ADDITIONAL FEATURES
# ---------------------------------
# Goal: Add useful functionality
# Tasks:
# - Allow users to specify which prize is the "Grand Prize"
# - Add "retry" option if user wants to redraw winners
# - Implement weighted probabilities (some entries count multiple times)
# - Add countdown animation before revealing each winner
# - Save raffle configuration to reload later
# Skills practiced: Feature development, user interaction, persistence

# CHALLENGE 6: FILE I/O & PERSISTENCE
# ------------------------------------
# Goal: Save and load raffle data
# Tasks:
# - Save results to a text file with timestamp
# - Create CSV output with all raffle details
# - Implement "raffle history" that tracks past events
# - Load previous participant lists from file
# - Export results in multiple formats (TXT, CSV, JSON)
# Skills practiced: File handling, data serialization, formats

# CHALLENGE 7: ADVANCED RANDOMIZATION
# ------------------------------------
# Goal: Implement sophisticated selection methods
# Tasks:
# - Add "drum roll" animation before revealing winners
# - Implement provably fair randomization with seed display
# - Allow manual seed input for reproducible draws
# - Add option for "runner-up" selections
# - Implement multiple drawing rounds
# Skills practiced: random module, seeding, algorithms

# CHALLENGE 8: ERROR HANDLING & EDGE CASES
# -----------------------------------------
# Goal: Handle all possible failure scenarios
# Tasks:
# - Handle KeyboardInterrupt (Ctrl+C) gracefully
# - Deal with very long names (truncate/wrap display)
# - Handle special characters in names properly
# - Add maximum participant limit with clear message
# - Validate prize count matches available winners
# Skills practiced: Exception handling, edge cases, defensive programming

# CHALLENGE 9: TYPE HINTS & DOCUMENTATION
# ----------------------------------------
# Goal: Make code more professional and maintainable
# Tasks:
# - Add type hints to all variables and functions
# - Write comprehensive docstrings for functions
# - Add inline comments explaining complex logic
# - Create a module-level docstring
# - Follow PEP 8 style guide strictly
# Skills practiced: Documentation, type hints, code standards

# CHALLENGE 10: UNIT TESTING
# ---------------------------
# Goal: Ensure code reliability through testing
# Tasks:
# - Write unit tests for validation functions
# - Test random selection with fixed seeds
# - Test edge cases (minimum participants, duplicate names)
# - Create mock input tests for user input functions
# - Achieve >80% code coverage
# Skills practiced: unittest module, test-driven development

# CHALLENGE 11: OBJECT-ORIENTED DESIGN
# -------------------------------------
# Goal: Restructure using OOP principles
# Tasks:
# - Create Raffle class with methods for setup and drawing
# - Create Participant class with properties
# - Create Prize class with value and description
# - Implement Winner class that combines participant and prize
# - Use inheritance/composition where appropriate
# Skills practiced: Classes, OOP, design patterns

# CHALLENGE 12: GUI VERSION
# --------------------------
# Goal: Create a graphical user interface
# Tasks:
# - Build GUI with tkinter or PyQt
# - Add buttons for "Add Participant", "Draw Winners", "Reset"
# - Display participants in a list widget
# - Animate winner selection visually
# - Add sound effects for winner announcements
# Skills practiced: GUI programming, event handling, user experience

# BONUS CHALLENGE: COMMAND-LINE INTERFACE
# ----------------------------------------
# Goal: Create a professional CLI tool
# Tasks:
# - Use argparse for command-line arguments
# - Add flags: --participants, --prizes, --output-file
# - Implement config file support (YAML/JSON)
# - Add verbose/quiet modes
# - Create man page / help documentation
# Skills practiced: CLI development, argument parsing, configuration
