# ========================================
# ZIP & UNZIP IN PYTHON
# ========================================
#
# The zip() function combines multiple iterables (lists, tuples, etc.)
# into pairs/tuples. Think of it like a zipper bringing two sides together!
#
# The zip object can be "unzipped" using the * operator with zip() again.

# ========================================
# BASIC ZIP() USAGE
# ========================================

# Example 1: Zipping two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]

# Combine them into pairs
zipped = zip(names, ages)
print(list(zipped))
# Output: [('Alice', 25), ('Bob', 30), ('Charlie', 35)]


# Example 2: Zipping three lists
cities = ["New York", "London", "Tokyo"]
countries = ["USA", "UK", "Japan"]
populations = [8_000_000, 9_000_000, 14_000_000]

combined = zip(cities, countries, populations)
print(list(combined))
# Output: [('New York', 'USA', 8000000), ('London', 'UK', 9000000), ('Tokyo', 'Japan', 14000000)]


# ========================================
# ZIP WITH DIFFERENT LENGTH LISTS
# ========================================

# zip() stops when the SHORTEST list ends
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

result = zip(list1, list2)
print(list(result))
# Output: [(1, 'a'), (2, 'b'), (3, 'c')]
# Note: 4 and 5 are ignored!


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Creating dictionaries from two lists
keys = ["name", "age", "city"]
values = ["Felipe", 20, "São Carlos"]

# Method 1: Using dict() constructor
person = dict(zip(keys, values))
print(person)
# Output: {'name': 'Felipe', 'age': 20, 'city': 'São Carlos'}

# Method 2: Using dictionary comprehension
person_dict = {key: value for key, value in zip(keys, values)}
print(person_dict)
# Output: {'name': 'Felipe', 'age': 20, 'city': 'São Carlos'}


# Use Case 2: Parallel iteration over multiple lists
products = ["Laptop", "Mouse", "Keyboard"]
prices = [1000, 25, 75]
quantities = [2, 5, 3]

print("Shopping Cart:")
for product, price, qty in zip(products, prices, quantities):
    total = price * qty
    print(f"{product}: ${price} x {qty} = ${total}")
# Output:
# Laptop: $1000 x 2 = $2000
# Mouse: $25 x 5 = $125
# Keyboard: $75 x 3 = $225


# Use Case 3: Transposing a matrix (rows → columns)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Transpose using zip with unpacking
transposed = list(zip(*matrix))
print(transposed)
# Output: [(1, 4, 7), (2, 5, 8), (3, 6, 9)]


# ========================================
# UNZIPPING WITH zip(*iterable)
# ========================================

# "Unzipping" means separating combined data back into original lists
pairs = [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Unzip using * operator
names, ages = zip(*pairs)

print(names)  # ('Alice', 'Bob', 'Charlie')
print(ages)   # (25, 30, 35)

# Convert tuples back to lists if needed
names_list = list(names)
ages_list = list(ages)


# Example: Unzipping coordinate pairs
coordinates = [(10, 20), (30, 40), (50, 60)]
x_coords, y_coords = zip(*coordinates)

print(f"X coordinates: {x_coords}")  # (10, 30, 50)
print(f"Y coordinates: {y_coords}")  # (20, 40, 60)


# ========================================
# UNZIPPING DICTIONARIES
# ========================================

# Example: Working with dictionary keys and values
en_sv_dict = {"hello": "hej", "goodbye": "hejdå", "thank you": "tack"}

# Method 1: Using .keys() and .values()
en = list(en_sv_dict.keys())
sv = list(en_sv_dict.values())
print(f"English: {en}")
print(f"Swedish: {sv}")
# Output: 
# English: ['hello', 'goodbye', 'thank you']
# Swedish: ['hej', 'hejdå', 'tack']

# Method 2: Using .items() with zip(*dict.items())
# This unzips the key-value pairs from the dictionary
en1, sv1 = zip(*en_sv_dict.items())
print(f"English (unzipped): {en1}")
print(f"Swedish (unzipped): {sv1}")
# Output:
# English (unzipped): ('hello', 'goodbye', 'thank you')
# Swedish (unzipped): ('hej', 'hejdå', 'tack')

# Key difference: 
# - .keys()/.values() → returns lists
# - zip(*dict.items()) → returns tuples (more memory efficient)


# Example: Rebuilding dictionary after unzipping
languages, translations = zip(*en_sv_dict.items())
rebuilt_dict = dict(zip(languages, translations))
print(rebuilt_dict)
# Output: {'hello': 'hej', 'goodbye': 'hejdå', 'thank you': 'tack'}

# Or using dict comprehension:
rebuilt_dict2 = {lang: trans for lang, trans in zip(languages, translations)}
print(rebuilt_dict2)
# Output: {'hello': 'hej', 'goodbye': 'hejdå', 'thank you': 'tack'}


# ========================================
# ZIP WITH ENUMERATE
# ========================================

# Combine zip() with enumerate() for index + multiple lists
students = ["Ana", "Bruno", "Carlos"]
grades = [85, 92, 78]

for index, (student, grade) in enumerate(zip(students, grades), start=1):
    print(f"{index}. {student}: {grade}")
# Output:
# 1. Ana: 85
# 2. Bruno: 92
# 3. Carlos: 78


# ========================================
# ADVANCED: zip_longest() FROM itertools
# ========================================

# What if you DON'T want to stop at the shortest list?
from itertools import zip_longest

list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c']

# zip_longest() continues until the LONGEST list ends
result = zip_longest(list1, list2, fillvalue='?')
print(list(result))
# Output: [(1, 'a'), (2, 'b'), (3, 'c'), (4, '?'), (5, '?')]


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# zip():
# - Combines multiple iterables element-by-element
# - Returns an iterator of tuples
# - Stops at the shortest iterable
# - Syntax: zip(iter1, iter2, iter3, ...)

# Unzipping:
# - Use zip(*zipped_data) to separate combined data
# - Returns tuples (convert to list if needed)
# - Syntax: list1, list2 = zip(*pairs)

# Common patterns:
# - dict(zip(keys, values)) → Create dictionary
# - for x, y in zip(list1, list2) → Parallel iteration
# - list(zip(*matrix)) → Transpose matrix
# - zip_longest() → Keep all elements (from itertools)


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Create a dictionary from these lists
# countries = ["Brazil", "USA", "Japan"]
# capitals = ["Brasília", "Washington", "Tokyo"]

# Exercise 2: Calculate total price for shopping cart
# items = ["Coffee", "Bread", "Milk"]
# prices = [5.50, 3.00, 4.25]
# quantities = [2, 1, 3]

# Exercise 3: Unzip this list of tuples
# data = [("Python", 1991), ("Java", 1995), ("JavaScript", 1995)]
# Separate into languages and years

# Exercise 4: Find pairs where sum > 10
# list_a = [5, 3, 8, 1]
# list_b = [6, 2, 4, 9]


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Use zip() for parallel iteration over multiple sequences
# - Convert zip object to list/dict when you need to reuse it
# - Use zip(*data) for simple unzipping
# - Use zip_longest() when you need all elements

# ❌ DON'T:
# - Forget that zip() returns an iterator (use list() to see contents)
# - Assume zip() will wait for longer lists (it stops at shortest)
# - Overuse zip() when a simple loop would be clearer