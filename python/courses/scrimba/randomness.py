# ===================================
# RANDOMNESS IN PYTHON
# ===================================
# Comprehensive guide to the random and string modules

import random
import string

# ===================================
# 1. RANDOM MODULE - OVERVIEW
# ===================================

# The random module provides functions for generating random numbers
# and making random selections
# Import: import random

# Common use cases:
# - Generating random numbers for games, simulations, testing
# - Randomly selecting items from sequences
# - Shuffling data
# - Creating random passwords or IDs
# - Statistical sampling


# ===================================
# 2. RANDOM FLOAT NUMBERS
# ===================================

# random.uniform(a, b) - Returns random float between a and b (inclusive)
print("=== random.uniform() ===")
for i in range(5):
    print(random.uniform(1, 6))
# Output: Random floats like 3.847291, 1.294856, 5.123947, etc.

# random.random() - Returns random float between 0.0 and 1.0
print("\n=== random.random() ===")
for i in range(3):
    print(random.random())
# Output: Random floats like 0.394756, 0.871234, 0.123456

# Use case: Probabilities, weights, continuous distributions
probability = random.random()
if probability < 0.5:
    print("Heads")
else:
    print("Tails")


# ===================================
# 3. RANDOM INTEGERS
# ===================================

# random.randint(a, b) - Returns random integer between a and b (BOTH INCLUSIVE)
print("\n=== random.randint() ===")
for i in range(5):
    print(random.randint(1, 6))
# Output: Random integers like 3, 1, 6, 4, 2 (dice roll simulation)

# Use case: Dice rolls, random IDs, game mechanics
dice_roll = random.randint(1, 6)
print(f"You rolled a {dice_roll}")


# ===================================
# 4. RANDOM RANGE WITH STEP
# ===================================

# random.randrange(start, stop, step) - Returns random number from range with step
# Note: stop is EXCLUSIVE (just like range())
print("\n=== random.randrange() ===")
for i in range(5):
    print(random.randrange(2, 100, 2))
# Output: Random even numbers like 24, 88, 46, 12, 78

# Different variations
print(random.randrange(10))        # Random from 0 to 9
print(random.randrange(5, 15))     # Random from 5 to 14
print(random.randrange(0, 101, 5)) # Random multiples of 5: 0, 5, 10, ..., 100

# Use case: Even/odd numbers, multiples, specific sequences


# ===================================
# 5. RANDOM CHOICE FROM SEQUENCE
# ===================================

# random.choice(sequence) - Returns ONE random element from non-empty sequence
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print("\n=== random.choice() ===")
print(random.choice(friends_list))
# Output: One random friend like 'Terry'

# Works with any sequence
colors = ['red', 'blue', 'green', 'yellow']
print(random.choice(colors))

numbers = [10, 20, 30, 40, 50]
print(random.choice(numbers))

letters = 'abcdefghijklmnopqrstuvwxyz'
print(random.choice(letters))  # Random single character

# Use case: Random selection, random NPC dialogue, random item pickup


# ===================================
# 6. RANDOM SAMPLE - MULTIPLE UNIQUE ITEMS
# ===================================

# random.sample(sequence, k) - Returns list of k UNIQUE random elements
# Elements will NOT repeat (sampling without replacement)
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print("\n=== random.sample() ===")
print(random.sample(friends_list, 3))
# Output: 3 unique friends like ['Michael', 'John', 'Terry']

# Use cases
# Lottery numbers (no duplicates)
lottery = random.sample(range(1, 50), 6)
print(f"Lottery numbers: {lottery}")

# Random team selection
players = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank']
team = random.sample(players, 3)
print(f"Team: {team}")

# Note: k cannot be larger than sequence length
# random.sample([1, 2, 3], 5)  # ValueError!


# ===================================
# 7. RANDOM CHOICES - WITH REPLACEMENT
# ===================================

# random.choices(sequence, k=n) - Returns list of k random elements
# Elements CAN repeat (sampling with replacement)
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print("\n=== random.choices() ===")
print(random.choices(friends_list, k=3))
# Output: 3 friends (may repeat) like ['John', 'John', 'Michael']

# Difference: choices() allows duplicates, sample() doesn't
print(random.choices([1, 2, 3], k=10))  # Works! May have duplicates
# print(random.sample([1, 2, 3], 10))   # Error! Not enough unique elements

# Weighted choices (optional weights parameter)
options = ['common', 'uncommon', 'rare', 'legendary']
weights = [50, 30, 15, 5]  # Probabilities
loot = random.choices(options, weights=weights, k=10)
print(f"Loot drops: {loot}")

# Use case: Random with duplicates allowed, weighted random selection


# ===================================
# 8. SHUFFLE - RANDOMIZE IN PLACE
# ===================================

# random.shuffle(list) - Shuffles list IN PLACE (modifies original)
# Returns None (like list.sort())
friends_list = ['John', 'Eric', 'Michael', 'Terry', 'Graham']
print("\n=== random.shuffle() ===")
random.shuffle(friends_list)
print(friends_list)
# Output: Shuffled list like ['Terry', 'John', 'Graham', 'Eric', 'Michael']

# Common use case: Card deck shuffling
deck = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# Note: Only works with mutable sequences (lists)
# Cannot shuffle tuples or strings directly


# ===================================
# 9. STRING MODULE - CHARACTER CONSTANTS
# ===================================

# The string module provides useful string constants
print("\n=== string module constants ===")

# Lowercase letters
print(string.ascii_lowercase)  # 'abcdefghijklmnopqrstuvwxyz'

# Uppercase letters
print(string.ascii_uppercase)  # 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# All ASCII letters (lowercase + uppercase)
print(string.ascii_letters)    # 'abcdefghijklmnopqrstuvwxyz' + 'ABC...'

# Digits
print(string.digits)           # '0123456789'

# Hexadecimal digits
print(string.hexdigits)        # '0123456789abcdefABCDEF'

# Punctuation
print(string.punctuation)      # '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# Whitespace characters
print(string.whitespace)       # ' \t\n\r\x0b\x0c'

# All printable characters
print(string.printable)        # Letters + digits + punctuation + whitespace


# ===================================
# 10. GENERATING RANDOM STRINGS - METHOD 1
# ===================================

# Using manual string concatenation
smallcaps = 'abcdefghijklmnopqrstuvwxyz'
largecaps = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
digits = '0123456789'

# Combine all characters
letters_numbers = string.ascii_letters + string.digits
print("\n=== Available characters ===")
print(letters_numbers)
# Output: 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'

# Generate random string using loop
print("\n=== Random string (Method 1: Loop) ===")
word = ''
for i in range(7):
    word += random.choice(letters_numbers)
print(word)
# Output: Random 7-character string like 'aB3xK9m'


# ===================================
# 11. GENERATING RANDOM STRINGS - METHOD 2
# ===================================

# Using join() with random.sample() - More Pythonic
print("\n=== Random string (Method 2: join + sample) ===")
word1 = ''.join(random.sample(letters_numbers, 7))
print(word1)
# Output: Random 7-character string like 'T4pLm9A' (all UNIQUE chars)

# Using join() with random.choices() - Allows duplicates
word2 = ''.join(random.choices(letters_numbers, k=7))
print(word2)
# Output: Random 7-character string like 'aaa3B9K' (may have duplicates)


# ===================================
# 12. PRACTICAL EXAMPLES - PASSWORD GENERATOR
# ===================================

print("\n=== Password Generator ===")

def generate_password(length=12):
    """Generate random password with letters, digits, and punctuation"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Generate passwords
for i in range(3):
    print(generate_password(16))
# Output: Random secure passwords like 'a$B9&mP2#xK7!qL3'


# ===================================
# 13. PRACTICAL EXAMPLES - DICE SIMULATOR
# ===================================

print("\n=== Dice Simulator ===")

def roll_dice(num_dice=1, sides=6):
    """Simulate rolling dice"""
    rolls = [random.randint(1, sides) for _ in range(num_dice)]
    return rolls

# Roll 2 six-sided dice
print(f"2d6: {roll_dice(2, 6)}")  # [4, 3]

# Roll 3 twenty-sided dice
print(f"3d20: {roll_dice(3, 20)}")  # [15, 8, 19]


# ===================================
# 14. PRACTICAL EXAMPLES - RANDOM COLOR
# ===================================

print("\n=== Random Color Generator ===")

def random_hex_color():
    """Generate random hex color code"""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def random_rgb_color():
    """Generate random RGB color"""
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return f"rgb({r}, {g}, {b})"

print(random_hex_color())  # #a3f5b2
print(random_rgb_color())  # rgb(145, 67, 234)


# ===================================
# 15. PRACTICAL EXAMPLES - RANDOM DATA GENERATION
# ===================================

print("\n=== Random User Data ===")

def generate_username():
    """Generate random username"""
    adjectives = ['Cool', 'Super', 'Mega', 'Ultra', 'Epic']
    nouns = ['Dragon', 'Tiger', 'Phoenix', 'Warrior', 'Ninja']
    number = random.randint(100, 999)
    return f"{random.choice(adjectives)}{random.choice(nouns)}{number}"

def generate_email(username):
    """Generate random email"""
    domains = ['gmail.com', 'yahoo.com', 'hotmail.com', 'outlook.com']
    return f"{username.lower()}@{random.choice(domains)}"

username = generate_username()
email = generate_email(username)
print(f"Username: {username}")  # CoolDragon456
print(f"Email: {email}")        # cooldragon456@gmail.com


# ===================================
# 16. SEEDING FOR REPRODUCIBILITY
# ===================================

print("\n=== Random Seed ===")

# random.seed(n) - Initialize random number generator with seed
# Same seed = same sequence of "random" numbers

random.seed(42)
print(random.randint(1, 100))  # Always the same number with seed 42
print(random.randint(1, 100))  # Always the same second number

random.seed(42)  # Reset seed
print(random.randint(1, 100))  # Same as first number above

# Use case: Testing, debugging, reproducible simulations
# For truly random: don't set seed (uses system time by default)


# ===================================
# 17. COMPARISON - CHOICE VS SAMPLE VS CHOICES
# ===================================

print("\n=== Comparison Table ===")

data = [1, 2, 3, 4, 5]

# choice() - ONE element
print(f"choice(): {random.choice(data)}")  # Single element: 3

# sample() - Multiple UNIQUE elements (no replacement)
print(f"sample(3): {random.sample(data, 3)}")  # [2, 5, 1] - no duplicates

# choices() - Multiple elements WITH replacement (can duplicate)
print(f"choices(k=3): {random.choices(data, k=3)}")  # [2, 2, 5] - may duplicate

# Key differences:
# - choice(): Returns single element (not a list)
# - sample(): Returns list, no duplicates, k ≤ len(sequence)
# - choices(): Returns list, allows duplicates, k can be any size


# ===================================
# COMMON USE CASES
# ===================================

# 1. Game development - Random enemy spawns
enemy_types = ['goblin', 'orc', 'troll']
enemy = random.choice(enemy_types)

# 2. A/B Testing - Random assignment
user_group = random.choice(['A', 'B'])

# 3. Random file selection
import os
# files = os.listdir('.')
# random_file = random.choice(files)

# 4. Quiz questions - Random order
questions = ['Q1', 'Q2', 'Q3', 'Q4', 'Q5']
random.shuffle(questions)

# 5. Monte Carlo simulations
hits = sum(random.random()**2 + random.random()**2 <= 1 for _ in range(10000))
pi_estimate = 4 * hits / 10000

# 6. Random delays (with time module)
import time
# time.sleep(random.uniform(1, 3))  # Random delay between 1-3 seconds


# ===================================
# BEST PRACTICES
# ===================================

# 1. Use appropriate function for your needs
#    - Need one item? Use choice()
#    - Need multiple unique items? Use sample()
#    - Need multiple items (duplicates ok)? Use choices()

# 2. Use string constants instead of hardcoding
#    ✅ string.ascii_letters
#    ❌ 'abcdefghijklmnopqrstuvwxyzABC...'

# 3. Set seed only for testing/debugging
#    random.seed(42)  # Reproducible results

# 4. Use join() for efficient string building
#    ✅ ''.join(random.choices(chars, k=10))
#    ❌ Loop with += (slower for large strings)

# 5. Remember: shuffle() modifies in place
#    original = [1, 2, 3]
#    shuffled = original.copy()
#    random.shuffle(shuffled)  # Keep original intact


# ===================================
# COMMON MISTAKES
# ===================================

# 1. Confusing randint() and randrange()
# random.randint(1, 10)    # 1 to 10 INCLUSIVE
# random.randrange(1, 10)  # 1 to 9 (10 EXCLUSIVE)

# 2. Trying to assign shuffle() result
# ❌ shuffled = random.shuffle(my_list)  # Returns None!
# ✅ random.shuffle(my_list); shuffled = my_list

# 3. Using sample() with k larger than sequence
# ❌ random.sample([1, 2, 3], 5)  # ValueError!
# ✅ random.choices([1, 2, 3], k=5)  # Works, allows duplicates

# 4. Not copying list before shuffling
# ❌ random.shuffle(original_list)  # Modifies original!
# ✅ shuffled = original_list.copy(); random.shuffle(shuffled)

# 5. Using random for security (cryptography)
# ❌ random module is NOT cryptographically secure
# ✅ Use secrets module for passwords, tokens, security
import secrets
secure_token = secrets.token_hex(16)


# ===================================
# PRACTICE EXERCISES
# ===================================

# Exercise 1: Coin Flip Simulator
# Create function that simulates n coin flips and returns count of heads/tails

# Exercise 2: Random Phone Number Generator
# Generate random phone number: (XXX) XXX-XXXX

# Exercise 3: Lottery Number Generator
# Generate 6 unique numbers between 1-49 (sorted)

# Exercise 4: Random Team Generator
# Given list of 10 players, create 2 random teams of 5 players each

# Exercise 5: Password Validator
# Generate password with at least: 1 uppercase, 1 lowercase, 1 digit, 1 special char

# Exercise 6: Weighted Random Item Drop
# Simulate game loot system with different rarity levels and probabilities

# Exercise 7: Shuffle Playlist
# Create function that shuffles playlist without repeating last 3 songs
