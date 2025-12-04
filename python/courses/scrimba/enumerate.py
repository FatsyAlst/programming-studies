# ========================================
# ENUMERATE IN PYTHON
# ========================================
#
# enumerate() adds a counter to an iterable and returns it as an enumerate object
# Instead of manually tracking index with a variable, use enumerate()!
#
# Syntax: enumerate(iterable, start=0)

# ========================================
# BASIC ENUMERATE USAGE
# ========================================

print('Python 101 - Enumerate')

friends = ['Brian', 'Judith', 'Reg', 'Loretta', 'Colin']

# ❌ OLD WAY: Manual counter
# i = 0
# for friend in friends:
#     print(i, friend)
#     i = i + 1  # or i += 1

# ✅ BETTER WAY: Using enumerate()
for i, friend in enumerate(friends):
    print(i, friend)
# Output:
# 0 Brian
# 1 Judith
# 2 Reg
# 3 Loretta
# 4 Colin


# ========================================
# CUSTOM START INDEX
# ========================================

# Start counting from a different number (default is 0)
for num, friend in enumerate(friends, 51):
    print(num, friend)
# Output:
# 51 Brian
# 52 Judith
# 53 Reg
# 54 Loretta
# 55 Colin

# Using start parameter (more explicit)
for num, friend in enumerate(friends, start=1):
    print(num, friend)
# Output:
# 1 Brian
# 2 Judith
# 3 Reg
# 4 Loretta
# 5 Colin


# ========================================
# UNDERSTANDING ENUMERATE OBJECTS
# ========================================

# enumerate() returns an enumerate object (iterator)
print(type(enumerate(friends)))
# Output: <class 'enumerate'>

# Convert to list to see all tuples at once
print(list(enumerate(friends)))
# Output: [(0, 'Brian'), (1, 'Judith'), (2, 'Reg'), (3, 'Loretta'), (4, 'Colin')]

# With custom start
print(list(enumerate(friends, 51)))
# Output: [(51, 'Brian'), (52, 'Judith'), (53, 'Reg'), (54, 'Loretta'), (55, 'Colin')]


# ========================================
# ENUMERATE WITH DIFFERENT ITERABLES
# ========================================

# Enumerate a string
for num, letter in enumerate('python', start=5):
    print(num, letter)
# Output:
# 5 p
# 6 y
# 7 t
# 8 h
# 9 o
# 10 n

# Enumerate a tuple
my_tuple = ('a', 'b', 'c')
for i, item in enumerate(my_tuple):
    print(f"Index {i}: {item}")
# Output:
# Index 0: a
# Index 1: b
# Index 2: c

# Enumerate a dictionary (iterates over keys)
my_dict = {'name': 'Felipe', 'age': 20, 'city': 'São Carlos'}
for i, key in enumerate(my_dict):
    print(f"{i}: {key} = {my_dict[key]}")
# Output:
# 0: name = Felipe
# 1: age = 20
# 2: city = São Carlos


# ========================================
# UNPACKING ENUMERATE TUPLES
# ========================================

# Without unpacking - get the whole tuple
for friend in enumerate(friends, 51):
    print(friend)
# Output:
# (51, 'Brian')
# (52, 'Judith')
# (53, 'Reg')
# (54, 'Loretta')
# (55, 'Colin')

# With unpacking - separate index and value
for num, friend in enumerate(friends, 51):
    print(f"Number {num}: {friend}")
# Output:
# Number 51: Brian
# Number 52: Judith
# Number 53: Reg
# Number 54: Loretta
# Number 55: Colin


# ========================================
# NESTED ENUMERATE (ADVANCED)
# ========================================

# Enumerate an enumerate object!
for item in enumerate(enumerate(friends, 51), -100):
    print(item)
# Output:
# (-100, (51, 'Brian'))
# (-99, (52, 'Judith'))
# (-98, (53, 'Reg'))
# (-97, (54, 'Loretta'))
# (-96, (55, 'Colin'))

# Unpacking nested enumerate
for outer_idx, (inner_idx, friend) in enumerate(enumerate(friends, 51), -100):
    print(f"Outer: {outer_idx}, Inner: {inner_idx}, Friend: {friend}")
# Output:
# Outer: -100, Inner: 51, Friend: Brian
# Outer: -99, Inner: 52, Friend: Judith
# ...


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Creating numbered lists
print("\nTodo List:")
tasks = ["Buy groceries", "Study Python", "Go to gym"]
for i, task in enumerate(tasks, 1):
    print(f"{i}. {task}")
# Output:
# 1. Buy groceries
# 2. Study Python
# 3. Go to gym


# Use Case 2: Finding index of specific items
numbers = [10, 20, 30, 20, 40]
target = 20
print(f"\nIndexes where {target} appears:")
for i, num in enumerate(numbers):
    if num == target:
        print(f"Index {i}")
# Output:
# Index 1
# Index 3


# Use Case 3: Modifying list while iterating (using index)
scores = [85, 92, 78, 90, 88]
for i, score in enumerate(scores):
    scores[i] = score + 5  # Add 5 bonus points
print(scores)
# Output: [90, 97, 83, 95, 93]


# Use Case 4: Creating dictionary from list
students = ['Alice', 'Bob', 'Charlie']
student_ids = {student: i for i, student in enumerate(students, 1001)}
print(student_ids)
# Output: {'Alice': 1001, 'Bob': 1002, 'Charlie': 1003}


# Use Case 5: Comparing lists element-by-element
list1 = ['a', 'b', 'c', 'd']
list2 = ['a', 'x', 'c', 'y']
print("\nDifferences:")
for i, (item1, item2) in enumerate(zip(list1, list2)):
    if item1 != item2:
        print(f"Index {i}: {item1} vs {item2}")
# Output:
# Index 1: b vs x
# Index 3: d vs y


# Use Case 6: Formatting output with alignment
data = ["Python", "JavaScript", "Go", "Rust"]
print("\nLanguages:")
for i, lang in enumerate(data, 1):
    print(f"{i:2d}. {lang:<15}")
# Output:
#  1. Python
#  2. JavaScript
#  3. Go
#  4. Rust


# ========================================
# ENUMERATE VS RANGE
# ========================================

# Using range(len()) - NOT PYTHONIC
print("\n❌ Not Pythonic:")
for i in range(len(friends)):
    print(i, friends[i])

# Using enumerate() - PYTHONIC
print("\n✅ Pythonic:")
for i, friend in enumerate(friends):
    print(i, friend)

# When you ONLY need the index, use range()
for i in range(5):
    print(f"Iteration {i}")

# When you need BOTH index and value, use enumerate()
for i, friend in enumerate(friends):
    print(f"{i}: {friend}")


# ========================================
# LIST COMPREHENSION WITH ENUMERATE
# ========================================

# Create list of tuples with custom formatting
formatted = [f"{i+1}. {friend}" for i, friend in enumerate(friends)]
print(formatted)
# Output: ['1. Brian', '2. Judith', '3. Reg', '4. Loretta', '5. Colin']

# Filter with enumerate
evens = [f"Index {i}: {num}" for i, num in enumerate([1, 2, 3, 4, 5, 6]) if num % 2 == 0]
print(evens)
# Output: ['Index 1: 2', 'Index 3: 4', 'Index 5: 6']


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# enumerate():
# - Syntax: enumerate(iterable, start=0)
# - Returns: enumerate object (iterator of tuples)
# - Each tuple: (index, value)
# - Default start: 0 (can be changed)
# - Works with: lists, tuples, strings, dicts, any iterable

# When to use:
# - Need both index AND value
# - Creating numbered lists
# - Finding positions of elements
# - Modifying list elements by index
# - Tracking iteration count

# When NOT to use:
# - Only need values (use regular for loop)
# - Only need indexes (use range())
# - Working with dictionaries (use .items() instead)


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Create a shopping list with numbers
# items = ['Milk', 'Bread', 'Eggs', 'Butter']
# Output: "1. Milk", "2. Bread", etc.

# Exercise 2: Find all indexes of 'a' in a string
# text = "banana"
# Expected: [1, 3, 5]

# Exercise 3: Create a dict mapping words to their lengths
# words = ['hello', 'world', 'python']
# Expected: {0: 5, 1: 5, 2: 6}

# Exercise 4: Print every 3rd item with its position
# data = list(range(20))
# Show items at positions 0, 3, 6, 9, etc.


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Use enumerate() when you need both index and value
# - Use start parameter for custom numbering
# - Unpack enumerate tuples for readability
# - Prefer enumerate() over range(len())

# ❌ DON'T:
# - Use range(len(list)) when enumerate() works
# - Manually track index with i = 0, i += 1
# - Forget that enumerate returns tuples
# - Use enumerate if you only need values (just iterate normally)

# Performance:
# - enumerate() is memory efficient (iterator, not list)
# - No performance overhead compared to manual indexing
# - Convert to list() only when you need all values at once
