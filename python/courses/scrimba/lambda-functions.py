# ========================================
# LAMBDA FUNCTIONS IN PYTHON
# ========================================
#
# Lambda functions are small anonymous functions (functions without a name)
# They can have any number of parameters but only ONE expression
# Syntax: lambda parameters: expression
#
# Think of them as "throwaway" functions for simple operations

# ========================================
# BASIC LAMBDA SYNTAX
# ========================================

# Regular function
def add(x, y):
    return x + y

print(add(5, 3))  # 8

# Same function as lambda
add_lambda = lambda x, y: x + y
print(add_lambda(5, 3))  # 8

# Lambda with single parameter
square = lambda x: x ** 2
print(square(5))  # 25

# Lambda with no parameters (rare but valid)
greet = lambda: "Hello, World!"
print(greet())  # Hello, World!


# ========================================
# LAMBDA VS REGULAR FUNCTIONS
# ========================================

# Regular function (named, multiple statements)
def multiply_and_add(x, y, z):
    result = x * y
    return result + z

# Lambda (anonymous, single expression)
multiply_and_add_lambda = lambda x, y, z: x * y + z

print(multiply_and_add(2, 3, 5))          # 11
print(multiply_and_add_lambda(2, 3, 5))   # 11

# Key differences:
# - Lambda: Single expression only, no statements (no if/else blocks, loops, etc.)
# - Regular: Multiple statements, more readable for complex logic
# - Lambda: Anonymous (usually), used inline
# - Regular: Named, reusable, easier to debug


# ========================================
# LAMBDA WITH BUILT-IN FUNCTIONS
# ========================================

# Using lambda with sorted()
students = [('Alice', 85), ('Bob', 92), ('Charlie', 78), ('David', 92)]

# Sort by grade (second element)
sorted_by_grade = sorted(students, key=lambda x: x[1])
print(sorted_by_grade)
# [('Charlie', 78), ('Alice', 85), ('Bob', 92), ('David', 92)]

# Sort by name length
names = ['Alice', 'Bob', 'Christopher', 'Dan']
sorted_by_length = sorted(names, key=lambda x: len(x))
print(sorted_by_length)  # ['Bob', 'Dan', 'Alice', 'Christopher']


# Using lambda with filter()
# filter(function, iterable) - keeps elements where function returns True
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)  # [2, 4, 6, 8, 10]

# Filter strings longer than 3 characters
words = ['hi', 'hello', 'bye', 'world', 'ok']
long_words = list(filter(lambda x: len(x) > 3, words))
print(long_words)  # ['hello', 'world']


# Using lambda with map()
# map(function, iterable) - applies function to every element
numbers = [1, 2, 3, 4, 5]

# Square all numbers
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # [1, 4, 9, 16, 25]

# Convert to uppercase
words = ['hello', 'world', 'python']
uppercase = list(map(lambda x: x.upper(), words))
print(uppercase)  # ['HELLO', 'WORLD', 'PYTHON']

# Multiple iterables with map
numbers1 = [1, 2, 3, 4]
numbers2 = [10, 20, 30, 40]
sums = list(map(lambda x, y: x + y, numbers1, numbers2))
print(sums)  # [11, 22, 33, 44]


# Using lambda with reduce()
# reduce(function, iterable) - reduces iterable to single value
from functools import reduce

numbers = [1, 2, 3, 4, 5]

# Sum all numbers
total = reduce(lambda x, y: x + y, numbers)
print(total)  # 15 (1+2+3+4+5)

# Find maximum
maximum = reduce(lambda x, y: x if x > y else y, numbers)
print(maximum)  # 5

# Product of all numbers
product = reduce(lambda x, y: x * y, numbers)
print(product)  # 120 (1*2*3*4*5)


# ========================================
# LAMBDA WITH CONDITIONAL EXPRESSIONS
# ========================================

# Ternary operator in lambda
# Syntax: value_if_true if condition else value_if_false

# Check if even or odd
check_even = lambda x: "Even" if x % 2 == 0 else "Odd"
print(check_even(4))  # Even
print(check_even(7))  # Odd

# Get absolute value
absolute = lambda x: x if x >= 0 else -x
print(absolute(-5))  # 5
print(absolute(10))  # 10

# Grade classifier
grade_letter = lambda score: 'A' if score >= 90 else 'B' if score >= 80 else 'C' if score >= 70 else 'F'
print(grade_letter(95))  # A
print(grade_letter(85))  # B
print(grade_letter(75))  # C


# ========================================
# LAMBDA IN SORTING COMPLEX DATA
# ========================================

# Sort list of dictionaries
people = [
    {'name': 'Alice', 'age': 30, 'salary': 70000},
    {'name': 'Bob', 'age': 25, 'salary': 50000},
    {'name': 'Charlie', 'age': 35, 'salary': 90000}
]

# Sort by age
sorted_by_age = sorted(people, key=lambda x: x['age'])
print([p['name'] for p in sorted_by_age])  # ['Bob', 'Alice', 'Charlie']

# Sort by salary descending
sorted_by_salary = sorted(people, key=lambda x: x['salary'], reverse=True)
print([p['name'] for p in sorted_by_salary])  # ['Charlie', 'Alice', 'Bob']

# Sort by multiple criteria (age, then salary)
sorted_multi = sorted(people, key=lambda x: (x['age'], x['salary']))
print([p['name'] for p in sorted_multi])  # ['Bob', 'Alice', 'Charlie']


# ========================================
# LAMBDA WITH LIST COMPREHENSION
# ========================================

# While you CAN use lambda in list comprehension, it's often unnecessary
numbers = [1, 2, 3, 4, 5]

# ❌ Using lambda (unnecessary)
squared = [(lambda x: x ** 2)(x) for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# ✅ Better: Direct expression
squared = [x ** 2 for x in numbers]
print(squared)  # [1, 4, 9, 16, 25]

# Lambda is useful when function is passed as argument
operations = [lambda x: x + 1, lambda x: x * 2, lambda x: x ** 2]
num = 5
results = [op(num) for op in operations]
print(results)  # [6, 10, 25]


# ========================================
# STORING LAMBDAS IN DATA STRUCTURES
# ========================================

# Dictionary of operations
operations = {
    'add': lambda x, y: x + y,
    'subtract': lambda x, y: x - y,
    'multiply': lambda x, y: x * y,
    'divide': lambda x, y: x / y if y != 0 else 'Error'
}

print(operations['add'](10, 5))       # 15
print(operations['multiply'](10, 5))  # 50
print(operations['divide'](10, 0))    # Error

# List of conditions
filters = [
    lambda x: x > 0,           # positive
    lambda x: x % 2 == 0,      # even
    lambda x: x < 100          # less than 100
]

number = 42
for i, f in enumerate(filters):
    print(f"Filter {i}: {f(number)}")  # True, True, True


# ========================================
# COMMON USE CASES
# ========================================

# Use Case 1: Quick data transformation
prices = [10.50, 20.99, 5.25, 15.00]
with_tax = list(map(lambda x: x * 1.10, prices))
print(with_tax)  # [11.55, 23.089, 5.775, 16.5]

# Use Case 2: Filtering data
emails = ['user@example.com', 'invalid', 'admin@site.org', 'test']
valid_emails = list(filter(lambda x: '@' in x, emails))
print(valid_emails)  # ['user@example.com', 'admin@site.org']

# Use Case 3: Custom sorting
words = ['Python', 'is', 'awesome', 'and', 'powerful']
sorted_words = sorted(words, key=lambda x: (len(x), x.lower()))
print(sorted_words)  # ['is', 'and', 'Python', 'awesome', 'powerful']

# Use Case 4: Event handlers (GUI programming simulation)
buttons = {
    'OK': lambda: print("OK pressed"),
    'Cancel': lambda: print("Cancelled"),
    'Submit': lambda: print("Form submitted")
}
# Simulate button click
buttons['OK']()  # OK pressed


# ========================================
# IMMEDIATELY INVOKED LAMBDA EXPRESSIONS
# ========================================

# You can define and call a lambda immediately by adding () at the end
# Syntax: (lambda parameters: expression)(arguments)

# Simple example: Calculate result immediately
result = (lambda x: x ** 2)(5)
print(result)  # 25

# Multiple parameters
sum_result = (lambda a, b, c: a + b + c)(2, 3, 4)
print(sum_result)  # 9

# With conditional
max_value = (lambda x, y: x if x > y else y)(10, 20)
print(max_value)  # 20


# Combining with function that returns lambda
def price_calc(start, hourly_rate):
    """Returns a function that calculates price based on hours"""
    return lambda hours: start + hourly_rate * hours

# Call the returned lambda immediately
total_price = price_calc(1, 25)(2)  # start=1, hourly_rate=25, hours=2
print(total_price)  # 51 (1 + 25*2)

# Breaking it down:
# Step 1: price_calc(1, 25) returns lambda hours: 1 + 25 * hours
# Step 2: (lambda hours: 1 + 25 * hours)(2) executes with hours=2
# Result: 1 + 25*2 = 51


# Another example: Temperature converter
def temp_converter(from_unit, to_unit):
    """Returns a converter function for temperatures"""
    conversions = {
        ('C', 'F'): lambda temp: temp * 9/5 + 32,
        ('F', 'C'): lambda temp: (temp - 32) * 5/9,
        ('C', 'K'): lambda temp: temp + 273.15,
        ('K', 'C'): lambda temp: temp - 273.15
    }
    return conversions.get((from_unit, to_unit), lambda temp: temp)

# Immediately invoke the returned lambda
celsius_to_fahrenheit = temp_converter('C', 'F')(25)
print(f"25°C = {celsius_to_fahrenheit}°F")  # 25°C = 77.0°F

# Or in one line (immediately invoked)
result = temp_converter('F', 'C')(77)
print(f"77°F = {result}°C")  # 77°F = 25.0°C


# Use case: Quick calculations without storing function
# ❌ Verbose way
square_func = lambda x: x ** 2
result = square_func(7)
print(result)  # 49

# ✅ Immediate invocation (if used only once)
result = (lambda x: x ** 2)(7)
print(result)  # 49


# Complex example: Chaining operations
result = (lambda x: (lambda y: x + y)(5))(10)
print(result)  # 15
# Breakdown: outer lambda gets x=10, inner lambda gets y=5, returns 10+5=15


# Real-world example: Quick data transformation
prices = [10, 20, 30, 40]
with_tax = [(lambda price: price * 1.10)(p) for p in prices]
print(with_tax)  # [11.0, 22.0, 33.0, 44.0]

# Note: This is often less readable than just: [p * 1.10 for p in prices]


# When to use immediately invoked lambdas:
# ✅ Quick one-time calculations
# ✅ Calling function-returned lambdas immediately
# ✅ Testing lambda logic quickly
# ❌ Don't overuse - can hurt readability
# ❌ If used multiple times, assign to variable instead


# ========================================
# LAMBDA INSIDE FUNCTIONS (CLOSURES)
# ========================================

# Functions can return lambda functions
# The lambda "remembers" variables from the outer function (closure)

def make_multiplier(n):
    """Returns a function that multiplies by n"""
    return lambda x: x * n

# Create specific multiplier functions
double = make_multiplier(2)
triple = make_multiplier(3)
times_ten = make_multiplier(10)

print(double(5))      # 10 (5 * 2)
print(triple(5))      # 15 (5 * 3)
print(times_ten(5))   # 50 (5 * 10)


# More complex example: Building custom validators
def create_range_validator(min_val, max_val):
    """Returns a validator function for a specific range"""
    return lambda x: min_val <= x <= max_val

# Create different validators
is_valid_age = create_range_validator(0, 120)
is_valid_percentage = create_range_validator(0, 100)
is_valid_temperature = create_range_validator(-50, 50)

print(is_valid_age(25))           # True
print(is_valid_age(150))          # False
print(is_valid_percentage(95))    # True
print(is_valid_temperature(60))   # False


# Example: Custom greeting generator
def make_greeter(greeting, punctuation='!'):
    """Returns a greeting function with custom format"""
    return lambda name: f"{greeting}, {name}{punctuation}"

formal_greet = make_greeter("Hello", ".")
casual_greet = make_greeter("Hey")
excited_greet = make_greeter("Hi", "!!!")

print(formal_greet("Dr. Smith"))  # Hello, Dr. Smith.
print(casual_greet("Bob"))        # Hey, Bob!
print(excited_greet("Alice"))     # Hi, Alice!!!


# Example: Math operation factory
def operation_factory(operation_name):
    """Returns appropriate math operation function"""
    operations = {
        'add': lambda x, y: x + y,
        'subtract': lambda x, y: x - y,
        'multiply': lambda x, y: x * y,
        'divide': lambda x, y: x / y if y != 0 else 'Error',
        'power': lambda x, y: x ** y
    }
    return operations.get(operation_name, lambda x, y: 'Invalid operation')

add_func = operation_factory('add')
power_func = operation_factory('power')

print(add_func(10, 5))     # 15
print(power_func(2, 3))    # 8


# Example: Filter factory (dynamic filtering)
def create_filter(criteria):
    """Returns a filter function based on criteria"""
    if criteria == 'even':
        return lambda x: x % 2 == 0
    elif criteria == 'positive':
        return lambda x: x > 0
    elif criteria == 'large':
        return lambda x: x > 100
    else:
        return lambda x: True  # No filter

numbers = [-5, 2, -10, 150, 7, 200, -3]
even_filter = create_filter('even')
positive_filter = create_filter('positive')
large_filter = create_filter('large')

print(list(filter(even_filter, numbers)))      # [2, -10, 150, 200]
print(list(filter(positive_filter, numbers)))  # [2, 150, 7, 200]
print(list(filter(large_filter, numbers)))     # [150, 200]


# Real-world example: Discount calculator generator
def create_discount_calculator(discount_percent, min_purchase=0):
    """Returns a function that calculates price after discount"""
    return lambda price: price * (1 - discount_percent/100) if price >= min_purchase else price

# Different discount tiers
regular_discount = create_discount_calculator(10)
vip_discount = create_discount_calculator(20, min_purchase=100)
premium_discount = create_discount_calculator(30, min_purchase=500)

print(f"Regular: ${regular_discount(50):.2f}")      # $45.00 (10% off)
print(f"VIP (under min): ${vip_discount(80):.2f}")  # $80.00 (no discount)
print(f"VIP (over min): ${vip_discount(150):.2f}")  # $120.00 (20% off)
print(f"Premium: ${premium_discount(600):.2f}")     # $420.00 (30% off)


# ========================================
# LAMBDA LIMITATIONS
# ========================================

# ❌ Can't have multiple statements
# wrong = lambda x: 
#     y = x * 2
#     return y + 5
# SyntaxError!

# ✅ Use regular function for multiple statements
def process(x):
    y = x * 2
    return y + 5

# ❌ Can't have assignments in expression
# wrong = lambda x: (y = x * 2)  # SyntaxError

# ✅ Use walrus operator := (Python 3.8+)
result = lambda x: (y := x * 2, y + 5)[1]
print(result(3))  # 11

# ❌ No docstrings
# square = lambda x: x ** 2
# square.__doc__ = "Squares a number"  # This works but not Pythonic

# ✅ Use regular function with docstring
def square_func(x):
    """Returns the square of x"""
    return x ** 2


# ========================================
# WHEN TO USE LAMBDA
# ========================================

# ✅ USE LAMBDA when:
# - Function is simple (one expression)
# - Used only once (throwaway function)
# - Passed as argument to higher-order functions (map, filter, sorted, etc.)
# - Improves readability by keeping logic inline

# ❌ DON'T USE LAMBDA when:
# - Function is complex (multiple statements)
# - Used multiple times (use def for reusability)
# - Needs a descriptive name for clarity
# - Requires documentation (use docstring)
# - Debugging is difficult (named functions show better tracebacks)


# ========================================
# LAMBDA VS ALTERNATIVES
# ========================================

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Filter even numbers - Lambda
evens_lambda = list(filter(lambda x: x % 2 == 0, numbers))

# Filter even numbers - List comprehension (MORE PYTHONIC)
evens_comprehension = [x for x in numbers if x % 2 == 0]

# Square numbers - Lambda with map
squared_lambda = list(map(lambda x: x ** 2, numbers))

# Square numbers - List comprehension (MORE PYTHONIC)
squared_comprehension = [x ** 2 for x in numbers]

# Recommendation: Prefer list comprehensions over map/filter with lambda
# They're more Pythonic and often more readable!


# ========================================
# KEY CONCEPTS SUMMARY
# ========================================

# Lambda functions:
# - Syntax: lambda parameters: expression
# - Anonymous (no name needed)
# - Single expression only
# - Returns value of expression automatically
# - Can have multiple parameters
# - Often used with map(), filter(), sorted(), reduce()

# Common patterns:
# - sorted(data, key=lambda x: x[1])
# - filter(lambda x: condition, iterable)
# - map(lambda x: transformation, iterable)
# - lambda x: value_if_true if condition else value_if_false


# ========================================
# PRACTICE EXERCISES
# ========================================

# Exercise 1: Filter names starting with 'A'
# names = ['Alice', 'Bob', 'Andrew', 'Charlie', 'Anna']

# Exercise 2: Convert list of Celsius to Fahrenheit
# celsius = [0, 10, 20, 30, 40]
# Formula: F = C * 9/5 + 32

# Exercise 3: Find product of all numbers using reduce
# numbers = [2, 3, 4, 5]

# Exercise 4: Sort list of tuples by second element, then first
# data = [(1, 'z'), (2, 'a'), (1, 'a'), (2, 'z')]


# ========================================
# BEST PRACTICES
# ========================================

# ✅ DO:
# - Keep lambdas short and simple (one line)
# - Use with built-in functions (sorted, map, filter)
# - Use for throwaway functions
# - Consider list comprehensions as alternative

# ❌ DON'T:
# - Assign lambda to variable if function will be reused (use def)
# - Write complex logic in lambda
# - Use lambda if it hurts readability
# - Forget that list comprehensions are often better than map/filter

# Readability comparison:
# ❌ Hard to read: list(map(lambda x: x**2, filter(lambda x: x%2==0, numbers)))
# ✅ Easier: [x**2 for x in numbers if x % 2 == 0]