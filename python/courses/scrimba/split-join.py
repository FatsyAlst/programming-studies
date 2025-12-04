# ========================================
# SPLIT & JOIN IN PYTHON
# ========================================
#
# split() - Breaks a string into a list of substrings
# join() - Combines a list of strings into a single string
#
# These are inverse operations of each other!

# ========================================
# SPLIT() METHOD
# ========================================

# Basic split() - splits on whitespace by default
msg = 'Welcome  to  Python  101: Split  and Join'
words = msg.split()
print(words)
# Output: ['Welcome', 'to', 'Python', '101:', 'Split', 'and', 'Join']
# Note: Multiple spaces are treated as one separator


# Split with custom delimiter
csv = 'Eric,John,Michael,Terry,Graham'
names = csv.split(',')
print(names)
# Output: ['Eric', 'John', 'Michael', 'Terry', 'Graham']


# Split with limit (maxsplit parameter)
text = "one-two-three-four-five"
result = text.split('-', 2)  # Split only first 2 occurrences
print(result)
# Output: ['one', 'two', 'three-four-five']


# Split on newlines
multiline = "Line 1\nLine 2\nLine 3"
lines = multiline.split('\n')
print(lines)
# Output: ['Line 1', 'Line 2', 'Line 3']


# splitlines() - specifically for splitting on line breaks
text_with_lines = "First\nSecond\rThird\r\nFourth"
lines = text_with_lines.splitlines()
print(lines)
# Output: ['First', 'Second', 'Third', 'Fourth']


# ========================================
# JOIN() METHOD
# ========================================

# Basic join() - combine list elements with a separator
friends_list = ['Eric', 'John', 'Michael', 'Terry', 'Graham']

# Join with no separator (empty string)
result = ''.join(friends_list)
print(result)
# Output: 'EricJohnMichaelTerryGraham'

# Join with space separator
result = ' '.join(friends_list)
print(result)
# Output: 'Eric John Michael Terry Graham'

# Join with comma separator
result = ', '.join(friends_list)
print(result)
# Output: 'Eric, John, Michael, Terry, Graham'

# Join with newline
result = '\n'.join(friends_list)
print(result)
# Output:
# Eric
# John
# Michael
# Terry
# Graham


# ========================================
# COMBINING SPLIT & JOIN
# ========================================

# Remove extra whitespace from a string
msg = 'Welcome  to  Python  101: Split  and Join'
cleaned = ' '.join(msg.split())
print(cleaned)
# Output: 'Welcome to Python 101: Split and Join'
# How it works: split() removes extra spaces, join() adds single spaces back


# Remove all whitespace
no_spaces = ''.join(msg.split())
print(no_spaces)
# Output: 'WelcometoPython101:SplitandJoin'


# Convert CSV to formatted list
csv = 'apple,banana,cherry,date'
fruits = csv.split(',')
formatted = '\n• '.join(fruits)
print('• ' + formatted)
# Output:
# • apple
# • banana
# • cherry
# • date


# Replace separator in a string
path = "folder/subfolder/file.txt"
windows_path = '\\'.join(path.split('/'))
print(windows_path)
# Output: folder\subfolder\file.txt


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Parsing CSV data
data = "John,25,Engineer\nJane,30,Doctor\nBob,35,Teacher"
rows = data.split('\n')
for row in rows:
    name, age, job = row.split(',')
    print(f"{name} is {age} years old and works as a {job}")
# Output:
# John is 25 years old and works as a Engineer
# Jane is 30 years old and works as a Doctor
# Bob is 35 years old and works as a Teacher


# Use Case 2: Creating URL slugs
title = "Python Programming: Tips and Tricks"
slug = '-'.join(title.lower().split())
print(slug)
# Output: python-programming:-tips-and-tricks

# Better slug (remove punctuation)
import string
clean_title = title.translate(str.maketrans('', '', string.punctuation))
slug = '-'.join(clean_title.lower().split())
print(slug)
# Output: python-programming-tips-and-tricks


# Use Case 3: Word count
text = "Python is awesome. Python is fun. Python is powerful."
words = text.split()
word_count = len(words)
print(f"Word count: {word_count}")
# Output: Word count: 9


# Use Case 4: Reversing words in a sentence
sentence = "Hello World from Python"
reversed_sentence = ' '.join(sentence.split()[::-1])
print(reversed_sentence)
# Output: Python from World Hello


# ========================================
# ADVANCED EXAMPLES
# ========================================

# rsplit() - split from the right
path = "folder/subfolder/another/file.txt"
# Get only the filename (last part)
filename = path.rsplit('/', 1)[-1]
print(filename)
# Output: file.txt


# partition() - split into 3 parts (before, separator, after)
email = "user@example.com"
username, at, domain = email.partition('@')
print(f"User: {username}, Domain: {domain}")
# Output: User: user, Domain: example.com


# Join with different data types (convert to strings first)
numbers = [1, 2, 3, 4, 5]
# result = ', '.join(numbers)  # ❌ This would raise TypeError
result = ', '.join(map(str, numbers))  # ✅ Convert to strings first
print(result)
# Output: 1, 2, 3, 4, 5

# Or using list comprehension
result = ', '.join([str(num) for num in numbers])
print(result)
# Output: 1, 2, 3, 4, 5


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# split():
# - Method: string.split(separator, maxsplit)
# - Default separator: any whitespace
# - Returns: list of strings
# - Empty string splits to empty list: ''.split() → []

# join():
# - Method: separator.join(iterable)
# - The separator is a STRING (what you call .join() on)
# - Can only join strings (convert other types first)
# - Returns: single string

# Common patterns:
# - Clean whitespace: ' '.join(text.split())
# - Parse CSV: text.split(',')
# - Create paths: '/'.join(['folder', 'file.txt'])
# - Format lists: ', '.join(items)


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Parse this log entry
# log = "2025-12-04 10:30:15 ERROR Database connection failed"
# Extract: date, time, level, message

# Exercise 2: Create a function to clean extra spaces
# def clean_spaces(text):
#     # Your code here
#     pass
# Test: clean_spaces("Hello    World   !") → "Hello World !"

# Exercise 3: Convert snake_case to Title Case
# snake = "hello_world_from_python"
# Expected output: "Hello World From Python"

# Exercise 4: Parse a simple URL
# url = "https://www.example.com/path/to/page?query=value"
# Extract: protocol, domain, path, query


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Use split() without arguments to handle any whitespace
# - Use join() for efficient string concatenation (faster than +=)
# - Convert non-string elements before joining
# - Use splitlines() for cross-platform line splitting

# ❌ DON'T:
# - Use split('/') for file paths (use pathlib instead)
# - Forget that split() returns a list (even with one element)
# - Try to join non-string elements without converting first
# - Use + in loops for string concatenation (use join() instead)
