# ========================================
# SETS IN PYTHON
# ========================================
#
# Sets are unordered collections of UNIQUE elements
# - Blazingly fast for membership testing (x in set)
# - Automatically remove duplicates
# - Cannot contain mutable elements (no lists, dicts, or sets inside sets)
# - Useful for mathematical set operations (union, intersection, difference)

# ========================================
# CREATING SETS
# ========================================

# Create a set with curly braces
friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Eric'}
print(friends_set)
# Output: {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
# Note: 'Eric' appears only once (duplicates removed)

# Create from a list
friends = ['John', 'Michael', 'Terry', 'Eric', 'Graham']
friends_set_from_list = set(friends)
print(friends_set_from_list)
# Output: {'John', 'Michael', 'Terry', 'Eric', 'Graham'}

# Create from a tuple
friends_tuple = ('John', 'Michael', 'Terry', 'Eric', 'Graham')
friends_set_from_tuple = set(friends_tuple)
print(friends_set_from_tuple)
# Output: {'John', 'Michael', 'Terry', 'Eric', 'Graham'}

# Create from a string (splits into characters)
letters = set("hello")
print(letters)
# Output: {'h', 'e', 'l', 'o'} - only unique characters


# ========================================
# EMPTY COLLECTIONS
# ========================================

# Empty list
empty_list = []
empty_list = list()

# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty set
# ❌ WRONG: empty_set = {}  # This creates an empty DICTIONARY, not a set!
# ✅ CORRECT:
empty_set = set()
print(type(empty_set))  # <class 'set'>


# ========================================
# SET OPERATIONS (MATHEMATICAL)
# ========================================

friends_set = {'John', 'Michael', 'Terry', 'Eric', 'Graham'}
my_friends_set = {'Reg', 'Loretta', 'Colin', 'Eric', 'Graham'}

# UNION - all unique elements from both sets (A ∪ B)
all_friends = friends_set.union(my_friends_set)
print(f"Union: {all_friends}")
# Output: {'John', 'Michael', 'Terry', 'Eric', 'Graham', 'Reg', 'Loretta', 'Colin'}
# Alternative syntax: friends_set | my_friends_set


# INTERSECTION - elements present in BOTH sets (A ∩ B)
common_friends = friends_set.intersection(my_friends_set)
print(f"Intersection: {common_friends}")
# Output: {'Eric', 'Graham'}
# Alternative syntax: friends_set & my_friends_set


# DIFFERENCE - elements in first set but NOT in second (A - B)
only_in_friends = friends_set.difference(my_friends_set)
print(f"Difference: {only_in_friends}")
# Output: {'John', 'Michael', 'Terry'}
# Alternative syntax: friends_set - my_friends_set


# SYMMETRIC DIFFERENCE - elements in either set but NOT in both (A △ B)
unique_to_each = friends_set.symmetric_difference(my_friends_set)
print(f"Symmetric Difference: {unique_to_each}")
# Output: {'John', 'Michael', 'Terry', 'Reg', 'Loretta', 'Colin'}
# Alternative syntax: friends_set ^ my_friends_set


# ========================================
# SET METHODS (MODIFYING)
# ========================================

# Add a single element
my_set = {1, 2, 3}
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# Add multiple elements (update)
my_set.update([5, 6, 7])
print(my_set)  # {1, 2, 3, 4, 5, 6, 7}

# Remove an element (raises KeyError if not found)
my_set.remove(7)
print(my_set)  # {1, 2, 3, 4, 5, 6}

# Discard an element (does NOT raise error if not found)
my_set.discard(10)  # No error even though 10 doesn't exist
print(my_set)  # {1, 2, 3, 4, 5, 6}

# Pop - remove and return an arbitrary element
popped = my_set.pop()
print(f"Popped: {popped}, Remaining: {my_set}")

# Clear all elements
my_set.clear()
print(my_set)  # set()


# ========================================
# SET MEMBERSHIP & COMPARISONS
# ========================================

numbers = {1, 2, 3, 4, 5}

# Check membership (VERY FAST - O(1))
print(3 in numbers)      # True
print(10 in numbers)     # False
print(10 not in numbers) # True

# Subset - check if all elements of A are in B
set_a = {1, 2, 3}
set_b = {1, 2, 3, 4, 5}
print(set_a.issubset(set_b))  # True (set_a ⊆ set_b)
# Alternative: set_a <= set_b

# Superset - check if A contains all elements of B
print(set_b.issuperset(set_a))  # True (set_b ⊇ set_a)
# Alternative: set_b >= set_a

# Disjoint - check if sets have NO common elements
set_c = {6, 7, 8}
print(set_a.isdisjoint(set_c))  # True (no overlap)


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Remove duplicates from a list
numbers_with_dupes = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6]
unique_numbers = list(set(numbers_with_dupes))
print(unique_numbers)  # [1, 2, 3, 4, 5, 6] (order may vary)

# To preserve order, use dict.fromkeys()
unique_ordered = list(dict.fromkeys(numbers_with_dupes))
print(unique_ordered)  # [1, 2, 3, 4, 5, 6]


# Use Case 2: Find common elements between lists
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(common)  # [4, 5]


# Use Case 3: Find unique elements across multiple lists
list_a = [1, 2, 3]
list_b = [3, 4, 5]
list_c = [5, 6, 7]
all_unique = set(list_a) | set(list_b) | set(list_c)
print(all_unique)  # {1, 2, 3, 4, 5, 6, 7}


# Use Case 4: Fast membership testing
# Lists are slow for large datasets (O(n))
large_list = list(range(1000000))
print(999999 in large_list)  # Slow

# Sets are MUCH faster (O(1))
large_set = set(range(1000000))
print(999999 in large_set)  # Blazingly fast!


# Use Case 5: Validate unique usernames
existing_users = {'alice', 'bob', 'charlie'}
new_user = 'bob'
if new_user in existing_users:
    print(f"Username '{new_user}' already taken")
else:
    existing_users.add(new_user)
    print(f"Username '{new_user}' registered")


# ========================================
# SET COMPREHENSION
# ========================================

# Create set with comprehension (like list comprehension)
squares = {x**2 for x in range(10)}
print(squares)
# Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}

# Filter even numbers
numbers = {x for x in range(20) if x % 2 == 0}
print(numbers)
# Output: {0, 2, 4, 6, 8, 10, 12, 14, 16, 18}


# ========================================
# FROZENSET (IMMUTABLE SET)
# ========================================

# Regular sets are mutable (can't be dictionary keys or set elements)
# Frozensets are immutable (can be used as dict keys or inside sets)

regular_set = {1, 2, 3}
frozen = frozenset([1, 2, 3])

# frozen.add(4)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'

# Can use frozenset as dictionary key
my_dict = {frozen: "This works!"}
print(my_dict[frozen])  # "This works!"

# Can have sets of frozensets
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# Sets:
# - Unordered (no indexing: set[0] doesn't work)
# - Unique elements only (duplicates removed)
# - Mutable (can add/remove elements)
# - Fast membership testing O(1)
# - Use {} or set() to create
# - Cannot contain lists, dicts, or other sets

# Common operations:
# - union() or | → all elements from both
# - intersection() or & → common elements
# - difference() or - → elements in first but not second
# - symmetric_difference() or ^ → unique to each set

# When to use sets:
# - Remove duplicates
# - Fast membership testing
# - Mathematical set operations
# - Finding common/unique elements


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Find students who passed both exams
# passed_math = {'Alice', 'Bob', 'Charlie', 'David'}
# passed_english = {'Bob', 'Charlie', 'Eve', 'Frank'}
# Find: students who passed both

# Exercise 2: Remove duplicates while preserving order
# data = [3, 1, 2, 1, 3, 4, 2, 5, 4]
# Expected output: [3, 1, 2, 4, 5]

# Exercise 3: Find common interests
# alice_hobbies = {'reading', 'gaming', 'cooking'}
# bob_hobbies = {'gaming', 'sports', 'reading'}
# Find: common hobbies

# Exercise 4: Validate email uniqueness
# emails = ['user1@example.com', 'user2@example.com', 'user1@example.com']
# Check if all emails are unique


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Use sets for fast membership testing (x in set)
# - Use sets to remove duplicates quickly
# - Use set operations for comparing collections
# - Use frozenset for immutable sets

# ❌ DON'T:
# - Try to index sets (no set[0])
# - Expect sets to maintain order (use list if order matters)
# - Put mutable objects in sets (lists, dicts)
# - Use {} for empty sets (creates dict, use set() instead)

# Performance:
# - Membership testing: set O(1) vs list O(n) → sets WIN
# - Iteration: similar speed
# - Memory: sets use more memory than lists
