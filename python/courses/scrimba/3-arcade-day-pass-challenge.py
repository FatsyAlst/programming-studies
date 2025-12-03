# Scrimba Python 101 - Exercise 3: Arcade Day Pass Challenge
#
# Topic: Basic Arithmetic Operations and Floor Division
# This exercise practices variable usage and mathematical operations including
# multiplication for totals and floor division (//) for whole number results.
#
# Requirements:
# - Store customer information and pass details in variables
# - Calculate total tokens, total cost, and available games
# - Use floor division to ensure games count is a whole number
# - Print a formatted summary of the purchase

# 🕹️ Arcade Day Pass Tracker — Challenge Steps
#
# 1) Create variables to store:
#    - customer name
#    - number of passes
#    - tokens per pass
#    - price per pass
#    - tokens required per game
#
# 2) Calculate:
#    - total tokens
#    - total cost
#    - games available  (use 'floor division' to get a whole number)
#
# 3) Print a summary with:
#    - customer name
#    - passes bought
#    - total tokens
#    - total cost
#    - games available

# Step 1: Store customer and pass information
customer_name = 'FHX'                     # str: Customer identifier
number_of_passes = 3                       # int: Quantity of passes purchased (note: typo in variable name)
tokens_per_pass = 5                       # int: Tokens included per pass
price_per_pass = 10                       # int/float: Cost per pass
tokens_required_per_game = 5              # int: Tokens needed to play one game (note: typo in variable name)

# Step 2: Calculate totals 
# total_tokens = numer_of_passes * tokens_per_pass
# total_cost = numer_of_passes * price_per_pass
# games_available = total_tokens // tokers_required_per_game  # Floor division returns whole number

total_tokens = number_of_passes * tokens_per_pass
total_cost = number_of_passes * price_per_pass
games_available = total_tokens // tokens_required_per_game

# Step 3: Print summary 

print("===== ARCADE DAY PASS =====")
print("Customer:", customer_name)
print("Passes:", number_of_passes)
print("Tokens:", total_tokens)
print(f"Total Cost: ${total_cost:.2f}")
print("Games Available: " + str(games_available))
