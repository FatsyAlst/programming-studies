# ===================================
# LIST AND DICTIONARY COMPREHENSIONS
# ===================================
# Comprehensive guide to comprehensions in Python

# ===================================
# 1. LIST COMPREHENSION - BASICS
# ===================================

# Traditional way with for loop
numbers = []
for i in range(5):
    numbers.append(i)
print(numbers)  # [0, 1, 2, 3, 4]

# List comprehension - more concise and Pythonic
numbers = [i for i in range(5)]
print(numbers)  # [0, 1, 2, 3, 4]

# Basic syntax: [expression for item in iterable]


# ===================================
# 2. LIST COMPREHENSION WITH EXPRESSIONS
# ===================================

# Squaring numbers
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# Multiplying by 2
doubled = [x * 2 for x in range(1, 6)]
print(doubled)  # [2, 4, 6, 8, 10]

# Working with strings
names = ["alice", "bob", "charlie"]
capitalized = [name.capitalize() for name in names]
print(capitalized)  # ['Alice', 'Bob', 'Charlie']

# Getting lengths
lengths = [len(name) for name in names]
print(lengths)  # [5, 3, 7]


# ===================================
# 3. LIST COMPREHENSION WITH CONDITIONS (FILTER)
# ===================================

# Filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in numbers if x % 2 == 0]
print(evens)  # [2, 4, 6, 8, 10]

# Filter odd numbers
odds = [x for x in numbers if x % 2 != 0]
print(odds)  # [1, 3, 5, 7, 9]

# Filter strings by length
words = ["hi", "hello", "hey", "goodbye"]
long_words = [word for word in words if len(word) > 3]
print(long_words)  # ['hello', 'goodbye']

# Filter positive numbers
numbers = [-5, -2, 0, 3, 7, -1, 9]
positives = [x for x in numbers if x > 0]
print(positives)  # [3, 7, 9]


# ===================================
# 4. LIST COMPREHENSION WITH IF-ELSE (TRANSFORM)
# ===================================

# Syntax: [expression_if_true if condition else expression_if_false for item in iterable]

# Label numbers as even or odd
numbers = [1, 2, 3, 4, 5]
labels = ["Even" if x % 2 == 0 else "Odd" for x in numbers]
print(labels)  # ['Odd', 'Even', 'Odd', 'Even', 'Odd']

# Replace negative numbers with 0
numbers = [-5, 3, -2, 7, -1, 9]
cleaned = [x if x > 0 else 0 for x in numbers]
print(cleaned)  # [0, 3, 0, 7, 0, 9]

# Convert temperature scale
celsius = [0, 10, 20, 30, 40]
fahrenheit = [(c * 9/5) + 32 for c in celsius]
print(fahrenheit)  # [32.0, 50.0, 68.0, 86.0, 104.0]


# ===================================
# 5. NESTED LIST COMPREHENSIONS
# ===================================

# Flatten a 2D list
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)  # [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Create a multiplication table
table = [[i * j for j in range(1, 6)] for i in range(1, 6)]
print(table)
# [[1, 2, 3, 4, 5],
#  [2, 4, 6, 8, 10],
#  [3, 6, 9, 12, 15],
#  [4, 8, 12, 16, 20],
#  [5, 10, 15, 20, 25]]

# Matrix transpose
matrix = [[1, 2, 3], [4, 5, 6]]
transposed = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transposed)  # [[1, 4], [2, 5], [3, 6]]

# Nested filtering
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
even_from_matrix = [num for row in matrix for num in row if num % 2 == 0]
print(even_from_matrix)  # [2, 4, 6, 8]


# ===================================
# 6. LIST COMPREHENSION WITH MULTIPLE ITERABLES
# ===================================

# Cartesian product (all combinations)
colors = ["red", "blue"]
sizes = ["S", "M", "L"]
products = [(color, size) for color in colors for size in sizes]
print(products)
# [('red', 'S'), ('red', 'M'), ('red', 'L'), ('blue', 'S'), ('blue', 'M'), ('blue', 'L')]

# Using zip() for parallel iteration
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
results = [f"{name}: {score}" for name, score in zip(names, scores)]
print(results)  # ['Alice: 85', 'Bob: 92', 'Charlie: 78']


# ===================================
# 7. DICTIONARY COMPREHENSION - BASICS
# ===================================

# Traditional way with for loop
squares_dict = {}
for x in range(5):
    squares_dict[x] = x**2
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Dictionary comprehension - more concise
squares_dict = {x: x**2 for x in range(5)}
print(squares_dict)  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# Basic syntax: {key_expression: value_expression for item in iterable}


# ===================================
# 8. DICTIONARY COMPREHENSION WITH EXPRESSIONS
# ===================================

# Create dictionary from two lists
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
people = {name: age for name, age in zip(names, ages)}
print(people)  # {'Alice': 25, 'Bob': 30, 'Charlie': 35}

# String lengths dictionary
words = ["hello", "world", "python"]
lengths_dict = {word: len(word) for word in words}
print(lengths_dict)  # {'hello': 5, 'world': 5, 'python': 6}

# Enumerate to dictionary
fruits = ["apple", "banana", "cherry"]
fruit_dict = {i: fruit for i, fruit in enumerate(fruits)}
print(fruit_dict)  # {0: 'apple', 1: 'banana', 2: 'cherry'}

# Swap keys and values
original = {"a": 1, "b": 2, "c": 3}
swapped = {value: key for key, value in original.items()}
print(swapped)  # {1: 'a', 2: 'b', 3: 'c'}


# ===================================
# 9. DICTIONARY COMPREHENSION WITH CONDITIONS
# ===================================

# Filter dictionary by value
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
high_scorers = {name: score for name, score in scores.items() if score >= 90}
print(high_scorers)  # {'Bob': 92, 'David': 95}

# Filter dictionary by key
prices = {"apple": 1.50, "banana": 0.75, "cherry": 3.00, "date": 2.50}
cheap_fruits = {fruit: price for fruit, price in prices.items() if price < 2.00}
print(cheap_fruits)  # {'apple': 1.5, 'banana': 0.75}

# Filter even numbers from dictionary
numbers_dict = {x: x**2 for x in range(10)}
even_squares = {k: v for k, v in numbers_dict.items() if k % 2 == 0}
print(even_squares)  # {0: 0, 2: 4, 4: 16, 6: 36, 8: 64}


# ===================================
# 10. DICTIONARY COMPREHENSION WITH IF-ELSE
# ===================================

# Categorize numbers as even or odd
numbers = [1, 2, 3, 4, 5]
categories = {x: "Even" if x % 2 == 0 else "Odd" for x in numbers}
print(categories)  # {1: 'Odd', 2: 'Even', 3: 'Odd', 4: 'Even', 5: 'Odd'}

# Apply discount to expensive items
prices = {"laptop": 1000, "mouse": 25, "keyboard": 75, "monitor": 300}
discounted = {item: price * 0.9 if price > 100 else price for item, price in prices.items()}
print(discounted)  # {'laptop': 900.0, 'mouse': 25, 'keyboard': 75, 'monitor': 270.0}

# Grade classification
scores = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 95}
grades = {name: "A" if score >= 90 else "B" if score >= 80 else "C" for name, score in scores.items()}
print(grades)  # {'Alice': 'B', 'Bob': 'A', 'Charlie': 'C', 'David': 'A'}


# ===================================
# 11. NESTED DICTIONARY COMPREHENSION
# ===================================

# Create nested dictionary
students = ["Alice", "Bob", "Charlie"]
subjects = ["Math", "Science"]
grades = {student: {subject: 0 for subject in subjects} for student in students}
print(grades)
# {'Alice': {'Math': 0, 'Science': 0},
#  'Bob': {'Math': 0, 'Science': 0},
#  'Charlie': {'Math': 0, 'Science': 0}}

# Grid coordinates
grid = {(x, y): x * y for x in range(3) for y in range(3)}
print(grid)
# {(0, 0): 0, (0, 1): 0, (0, 2): 0, (1, 0): 0, (1, 1): 1, (1, 2): 2, 
#  (2, 0): 0, (2, 1): 2, (2, 2): 4}


# ===================================
# 12. SET COMPREHENSION
# ===================================

# Set comprehension - similar to list comprehension but with {}
# Automatically removes duplicates

# Basic set comprehension
squares_set = {x**2 for x in range(-5, 6)}
print(squares_set)  # {0, 1, 4, 9, 16, 25} (duplicates removed, unordered)

# Extract unique lengths
words = ["hello", "world", "hi", "python", "bye", "code"]
unique_lengths = {len(word) for word in words}
print(unique_lengths)  # {2, 3, 4, 5, 6}

# Filter and create set
numbers = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 8, 8, 9]
even_set = {x for x in numbers if x % 2 == 0}
print(even_set)  # {2, 4, 6, 8}


# ===================================
# 13. COMPREHENSIONS VS TRADITIONAL LOOPS
# ===================================

# Example: Filter and transform

# Traditional approach
result = []
for x in range(10):
    if x % 2 == 0:
        result.append(x ** 2)
print(result)  # [0, 4, 16, 36, 64]

# Comprehension approach (more Pythonic)
result = [x**2 for x in range(10) if x % 2 == 0]
print(result)  # [0, 4, 16, 36, 64]

# Dictionary example - Traditional
freq = {}
text = "hello world"
for char in text:
    if char != ' ':
        freq[char] = freq.get(char, 0) + 1
print(freq)  # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}

# Dictionary comprehension with counter logic needs traditional loop
# (But can use Counter from collections module)


# ===================================
# 14. COMMON USE CASES
# ===================================

# 1. Data transformation
temperatures_c = [0, 10, 20, 30]
temperatures_f = [(c * 9/5) + 32 for c in temperatures_c]
print(temperatures_f)  # [32.0, 50.0, 68.0, 86.0]

# 2. Filtering data
ages = [12, 18, 25, 16, 30, 14, 22]
adults = [age for age in ages if age >= 18]
print(adults)  # [18, 25, 30, 22]

# 3. Parsing and cleaning
urls = ["http://example.com", "https://test.com", "ftp://files.com"]
http_urls = [url for url in urls if url.startswith("http")]
print(http_urls)  # ['http://example.com', 'https://test.com']

# 4. Creating lookup dictionaries
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"}
]
user_lookup = {user["id"]: user["name"] for user in users}
print(user_lookup)  # {1: 'Alice', 2: 'Bob', 3: 'Charlie'}

# 5. String manipulation
sentence = "Hello World Python"
word_lengths = {word: len(word) for word in sentence.split()}
print(word_lengths)  # {'Hello': 5, 'World': 5, 'Python': 6}

# 6. Matrix operations
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
doubled_matrix = [[x * 2 for x in row] for row in matrix]
print(doubled_matrix)  # [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

# 7. Filtering dictionary by multiple conditions
inventory = {
    "apple": {"price": 1.50, "stock": 100},
    "banana": {"price": 0.75, "stock": 5},
    "cherry": {"price": 3.00, "stock": 50}
}
low_stock_expensive = {
    fruit: info for fruit, info in inventory.items() 
    if info["stock"] < 60 and info["price"] > 1.00
}
print(low_stock_expensive)  # {'banana': {'price': 0.75, 'stock': 5}, 'cherry': {'price': 3.0, 'stock': 50}}


# ===================================
# 15. PERFORMANCE CONSIDERATIONS
# ===================================

# List comprehensions are generally faster than loops
import time

# Using loop
start = time.time()
result = []
for i in range(1000000):
    result.append(i * 2)
loop_time = time.time() - start

# Using list comprehension
start = time.time()
result = [i * 2 for i in range(1000000)]
comp_time = time.time() - start

print(f"Loop time: {loop_time:.4f}s")
print(f"Comprehension time: {comp_time:.4f}s")
# Comprehension is typically faster!


# ===================================
# 16. WHEN TO USE COMPREHENSIONS
# ===================================

# ✅ USE comprehensions when:
# - Creating a new list/dict/set from an iterable
# - Simple transformation or filtering
# - One-liner logic that's readable
# - Performance matters (comprehensions are faster)

# ❌ DON'T use comprehensions when:
# - Logic is complex and hard to read
# - Need to handle exceptions
# - Multiple statements required
# - Side effects needed (printing, file writing, etc.)

# Good - Simple and readable
squares = [x**2 for x in range(10) if x % 2 == 0]

# Bad - Too complex and hard to read
# result = [func1(func2(x)) if condition1(x) else func3(x) if condition2(x) else 0 
#           for x in data if validate(x) and check(x)]

# For complex logic, use traditional loops:
# result = []
# for x in data:
#     if validate(x) and check(x):
#         if condition1(x):
#             result.append(func1(func2(x)))
#         elif condition2(x):
#             result.append(func3(x))
#         else:
#             result.append(0)


# ===================================
# 17. GENERATOR EXPRESSIONS
# ===================================

# Generator expressions use () instead of []
# They don't create the whole list in memory (lazy evaluation)
# More memory efficient for large datasets

# List comprehension - creates entire list
list_comp = [x**2 for x in range(1000000)]  # Uses more memory

# Generator expression - creates values on demand
gen_exp = (x**2 for x in range(1000000))  # Uses less memory

# You can iterate over generator once
print(type(gen_exp))  # <class 'generator'>

# Convert to list if needed
# result = list(gen_exp)

# Use generator expression with sum(), max(), min(), etc.
total = sum(x**2 for x in range(100))
print(total)  # 328350

maximum = max(x**2 for x in range(10))
print(maximum)  # 81


# ===================================
# BEST PRACTICES
# ===================================

# 1. Keep it simple and readable
# Good
evens = [x for x in range(10) if x % 2 == 0]

# Bad - too complex
# result = [x if x > 0 else -x if x < -10 else 0 for x in data if x != None]

# 2. Use meaningful variable names
# Good
squared_numbers = [num**2 for num in numbers]

# Bad (example of poor naming)
# x = [n**2 for n in l]

# 3. Don't nest too deeply
# Avoid more than 2 levels of nesting

# 4. Use generator expressions for large datasets
# Good for large data
total = sum(x**2 for x in range(1000000))

# Avoid for large data (wastes memory)
# numbers = [x**2 for x in range(1000000)]
# total = sum(numbers)

# 5. Consider readability over conciseness
# If comprehension becomes hard to read, use a regular loop


# ===================================
# COMMON MISTAKES
# ===================================

# 1. Modifying original list in comprehension (side effects)
# ❌ DON'T
numbers = [1, 2, 3]
# [numbers.append(x*2) for x in numbers]  # Side effect, returns [None, None, None]

# ✅ DO
doubled = [x*2 for x in numbers]

# 2. Using list comprehension when you need a loop
# ❌ DON'T
# [print(x) for x in numbers]  # Creates unnecessary list of None values

# ✅ DO
for x in numbers:
    print(x)

# 3. Forgetting about generator expressions
# ❌ Memory inefficient
sum_of_squares = sum([x**2 for x in range(1000000)])

# ✅ Memory efficient
sum_of_squares = sum(x**2 for x in range(1000000))

# 4. Overly complex nested comprehensions
# ❌ Hard to read
# result = [[j for j in range(i)] for i in range(10) if i % 2 == 0]

# ✅ More readable
result = []
for i in range(10):
    if i % 2 == 0:
        result.append([j for j in range(i)])


# ===================================
# PRACTICE EXERCISES
# ===================================

# Exercise 1: List Comprehension
# Create a list of all numbers from 1-50 that are divisible by 3 or 5

# Exercise 2: Dictionary Comprehension
# Given: words = ["hello", "world", "python", "code"]
# Create a dictionary where keys are words and values are reversed words

# Exercise 3: Nested List Comprehension
# Create a 5x5 identity matrix using list comprehension
# [[1,0,0,0,0], [0,1,0,0,0], [0,0,1,0,0], [0,0,0,1,0], [0,0,0,0,1]]

# Exercise 4: Dictionary Filtering
# Given: students = {"Alice": 85, "Bob": 92, "Charlie": 78, "David": 65, "Eve": 95}
# Create new dict with only students who scored above 80, with their grade letter

# Exercise 5: Flattening and Filtering
# Given: data = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
# Flatten the list and keep only even numbers

# Exercise 6: Set Comprehension
# Given: text = "hello world"
# Create a set of all unique vowels in the text

# Exercise 7: Dictionary Transformation
# Given: temps_f = {"Monday": 68, "Tuesday": 77, "Wednesday": 86}
# Convert all temperatures to Celsius: (F - 32) * 5/9
