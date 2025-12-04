# ========================================
# SORT() VS SORTED() IN PYTHON
# ========================================
#
# Two ways to sort in Python:
# 1. list.sort() - modifies the original list (in-place)
# 2. sorted() - returns a new sorted list (doesn't modify original)

# ========================================
# BASIC DIFFERENCES
# ========================================

# Using .sort() - IN-PLACE (modifies original)
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]
# Original list is changed!

# Using sorted() - RETURNS NEW LIST (original unchanged)
numbers = [5, 2, 8, 1, 9]
sorted_numbers = sorted(numbers)
print(sorted_numbers)  # [1, 2, 5, 8, 9]
print(numbers)         # [5, 2, 8, 1, 9] - original unchanged!


# ========================================
# KEY DIFFERENCES SUMMARY
# ========================================

# list.sort():
# - Method (only works on lists)
# - Modifies original list in-place
# - Returns None
# - Slightly faster (no copy created)
# - Syntax: list.sort(key=None, reverse=False)

# sorted():
# - Built-in function (works on any iterable)
# - Returns new sorted list
# - Original unchanged
# - Works with lists, tuples, strings, sets, dicts, etc.
# - Syntax: sorted(iterable, key=None, reverse=False)


# ========================================
# SORTING IN ASCENDING ORDER (DEFAULT)
# ========================================

# Numbers
numbers = [42, 7, 15, 3, 100]
print(sorted(numbers))  # [3, 7, 15, 42, 100]

# Strings (alphabetical order)
names = ['Zoe', 'Alice', 'Bob', 'Charlie']
print(sorted(names))  # ['Alice', 'Bob', 'Charlie', 'Zoe']

# Mixed case (uppercase comes before lowercase in ASCII)
words = ['apple', 'Banana', 'cherry', 'Apple']
print(sorted(words))  # ['Apple', 'Banana', 'apple', 'cherry']


# ========================================
# SORTING IN DESCENDING ORDER
# ========================================

numbers = [5, 2, 8, 1, 9]

# Using .sort() with reverse=True
numbers.sort(reverse=True)
print(numbers)  # [9, 8, 5, 2, 1]

# Using sorted() with reverse=True
numbers = [5, 2, 8, 1, 9]
descending = sorted(numbers, reverse=True)
print(descending)  # [9, 8, 5, 2, 1]


# ========================================
# SORTING WITH KEY PARAMETER
# ========================================

# Sort by length of strings
words = ['python', 'is', 'awesome', 'and', 'fun']
sorted_by_length = sorted(words, key=len)
print(sorted_by_length)  # ['is', 'and', 'fun', 'python', 'awesome']

# Sort strings case-insensitive
words = ['apple', 'Banana', 'cherry', 'Apple']
sorted_case_insensitive = sorted(words, key=str.lower)
print(sorted_case_insensitive)  # ['apple', 'Apple', 'Banana', 'cherry']

# Sort by absolute value
numbers = [-5, 2, -8, 1, 9, -3]
sorted_by_abs = sorted(numbers, key=abs)
print(sorted_by_abs)  # [1, 2, -3, -5, -8, 9]

# Sort by last character
words = ['hello', 'world', 'python', 'code']
sorted_by_last = sorted(words, key=lambda x: x[-1])
print(sorted_by_last)  # ['code', 'hello', 'world', 'python']


# ========================================
# SORTING COMPLEX DATA STRUCTURES
# ========================================

# Sort list of tuples (by first element by default)
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78)]
sorted_students = sorted(students)
print(sorted_students)  # [('Alice', 85), ('Bob', 92), ('Charlie', 78)]

# Sort by second element (grade)
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)  # [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort by grade descending
sorted_by_grade_desc = sorted(students, key=lambda x: x[1], reverse=True)
print(sorted_by_grade_desc)  # [('Bob', 92), ('Alice', 85), ('Charlie', 78)]


# Sort list of dictionaries
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

# Sort by age
sorted_by_age = sorted(people, key=lambda x: x['age'])
print(sorted_by_age)
# [{'name': 'Bob', 'age': 25}, {'name': 'Alice', 'age': 30}, {'name': 'Charlie', 'age': 35}]

# Sort by name
sorted_by_name = sorted(people, key=lambda x: x['name'])
print(sorted_by_name)
# [{'name': 'Alice', 'age': 30}, {'name': 'Bob', 'age': 25}, {'name': 'Charlie', 'age': 35}]


# ========================================
# SORTING OTHER ITERABLES
# ========================================

# sorted() works with any iterable!

# Sort a tuple (returns list)
my_tuple = (5, 2, 8, 1, 9)
sorted_tuple = sorted(my_tuple)
print(sorted_tuple)  # [1, 2, 5, 8, 9] - returns list, not tuple!

# Sort a string (returns list of characters)
text = "python"
sorted_chars = sorted(text)
print(sorted_chars)  # ['h', 'n', 'o', 'p', 't', 'y']
print(''.join(sorted_chars))  # 'hnoptv'

# Sort a set
my_set = {5, 2, 8, 1, 9}
sorted_set = sorted(my_set)
print(sorted_set)  # [1, 2, 5, 8, 9]

# Sort dictionary keys
my_dict = {'banana': 3, 'apple': 5, 'cherry': 2}
sorted_keys = sorted(my_dict)
print(sorted_keys)  # ['apple', 'banana', 'cherry']

# Sort dictionary by values
sorted_by_values = sorted(my_dict.items(), key=lambda x: x[1])
print(sorted_by_values)  # [('cherry', 2), ('banana', 3), ('apple', 5)]


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Top N items
scores = [85, 92, 78, 95, 88, 76, 90]
top_3 = sorted(scores, reverse=True)[:3]
print(f"Top 3 scores: {top_3}")  # [95, 92, 90]

# Use Case 2: Finding median (middle value)
numbers = [5, 2, 8, 1, 9, 3, 7]
sorted_nums = sorted(numbers)
median = sorted_nums[len(sorted_nums) // 2]
print(f"Median: {median}")  # 5

# Use Case 3: Alphabetizing names
names = ['Zoe', 'Alice', 'Bob', 'Charlie', 'David']
names.sort()
print(f"Alphabetical: {names}")  # ['Alice', 'Bob', 'Charlie', 'David', 'Zoe']

# Use Case 4: Organizing products by price
products = [
    {'name': 'Laptop', 'price': 1000},
    {'name': 'Mouse', 'price': 25},
    {'name': 'Keyboard', 'price': 75}
]
products.sort(key=lambda x: x['price'])
for p in products:
    print(f"{p['name']}: ${p['price']}")
# Mouse: $25
# Keyboard: $75
# Laptop: $1000


# ========================================
# MULTIPLE SORT CRITERIA
# ========================================

# Sort by multiple keys using tuple
students = [
    ('Alice', 'A', 85),
    ('Bob', 'B', 92),
    ('Charlie', 'A', 92),
    ('David', 'B', 85)
]

# Sort by grade (index 2), then by name (index 0)
sorted_students = sorted(students, key=lambda x: (x[2], x[0]))
print(sorted_students)
# [('Alice', 'A', 85), ('David', 'B', 85), ('Bob', 'B', 92), ('Charlie', 'A', 92)]

# Sort by section (index 1), then by grade descending
sorted_students = sorted(students, key=lambda x: (x[1], -x[2]))
print(sorted_students)
# [('Alice', 'A', 92), ('Charlie', 'A', 85), ('Bob', 'B', 92), ('David', 'B', 85)]


# ========================================
# STABILITY OF SORTING
# ========================================

# Python's sort is STABLE - equal elements maintain their original order
data = [('Alice', 85), ('Bob', 92), ('Charlie', 85), ('David', 92)]
sorted_data = sorted(data, key=lambda x: x[1])
print(sorted_data)
# [('Alice', 85), ('Charlie', 85), ('Bob', 92), ('David', 92)]
# Note: Alice and Charlie (both 85) maintain their original order


# ========================================
# WHEN TO USE WHICH?
# ========================================

# Use .sort() when:
# ✅ Working with lists only
# ✅ You want to modify the list in-place
# ✅ You don't need the original list
# ✅ Memory efficiency matters (no copy)

# Use sorted() when:
# ✅ Working with any iterable (tuple, string, set, dict, etc.)
# ✅ You need to keep the original unchanged
# ✅ You want a sorted copy
# ✅ Working with non-list iterables


# ========================================
# COMMON MISTAKES
# ========================================

# ❌ MISTAKE 1: Trying to use .sort() return value
numbers = [5, 2, 8, 1, 9]
result = numbers.sort()
print(result)  # None (sort() returns None!)
print(numbers)  # [1, 2, 5, 8, 9] - numbers is modified

# ✅ CORRECT: Don't assign .sort() to a variable
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # [1, 2, 5, 8, 9]


# ❌ MISTAKE 2: Trying .sort() on non-list
my_tuple = (5, 2, 8, 1, 9)
# my_tuple.sort()  # AttributeError: 'tuple' object has no attribute 'sort'

# ✅ CORRECT: Use sorted() for non-lists
my_tuple = (5, 2, 8, 1, 9)
sorted_tuple = sorted(my_tuple)  # Returns list


# ❌ MISTAKE 3: Comparing incompatible types
mixed = [1, 'hello', 3, 'world']
# sorted(mixed)  # TypeError: '<' not supported between 'int' and 'str'

# ✅ CORRECT: Use key to convert to comparable type
mixed = [1, 'hello', 3, 'world']
sorted_mixed = sorted(mixed, key=str)  # Convert all to strings
print(sorted_mixed)  # [1, 3, 'hello', 'world']


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# .sort():
# - List method only
# - In-place (modifies original)
# - Returns None
# - Faster (no copy)
# - Syntax: list.sort(key=None, reverse=False)

# sorted():
# - Built-in function
# - Works on any iterable
# - Returns new sorted list
# - Original unchanged
# - Syntax: sorted(iterable, key=None, reverse=False)

# Common parameters:
# - reverse=True → descending order
# - key=function → custom sorting logic
# - Both use Timsort algorithm (O(n log n))
# - Both are stable sorts


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Sort these words by length (shortest to longest)
# words = ['elephant', 'cat', 'dog', 'butterfly', 'ant']

# Exercise 2: Sort students by grade, then by name
# students = [('Bob', 85), ('Alice', 92), ('Charlie', 85)]

# Exercise 3: Find the 5 most expensive items
# prices = [10, 50, 30, 80, 20, 90, 40, 60, 70]

# Exercise 4: Sort filenames naturally (file1, file2, file10, not file1, file10, file2)
# files = ['file10.txt', 'file2.txt', 'file1.txt', 'file20.txt']
# Hint: Use key with int() on the numeric part


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Use .sort() to save memory when you don't need original
# - Use sorted() when you need original list preserved
# - Use key parameter for custom sorting logic
# - Use lambda for simple key functions
# - Use stable sort property for multi-level sorting

# ❌ DON'T:
# - Assign .sort() to a variable (it returns None)
# - Use .sort() on non-list iterables
# - Try to sort incompatible types
# - Call .sort() multiple times (sort once with proper key)
# - Forget that sorted() always returns a list

# Performance:
# - Both use Timsort: O(n log n) worst case, O(n) best case
# - .sort() is slightly faster (no copy overhead)
# - For large lists, memory usage differs significantly