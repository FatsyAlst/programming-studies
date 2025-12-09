# ===================================
# TIMEIT MODULE & PERFORMANCE OPTIMIZATION
# ===================================
# Comprehensive guide to measuring and optimizing Python code performance

import timeit

# ===================================
# 1. INTRODUCTION TO PERFORMANCE
# ===================================

# Performance optimization is about making code run faster
# Key concepts:
# - Time complexity: How execution time grows with input size
# - Space complexity: How memory usage grows with input size
# - Benchmarking: Measuring actual execution time
# - Profiling: Finding bottlenecks in code

# Common performance improvements:
# - Better algorithms (O(n²) → O(n log n) → O(n))
# - Built-in functions (usually written in C, faster than Python loops)
# - List comprehensions (faster than explicit loops)
# - Early termination (break when answer is found)
# - Avoiding repeated calculations


# ===================================
# 2. THE TIMEIT MODULE
# ===================================

# timeit is Python's built-in module for measuring execution time
# More accurate than manual timing with time.time()
# Why? It:
# - Runs code multiple times to get average
# - Disables garbage collection during timing
# - Provides consistent, reproducible results

# Basic syntax:
# timeit.timeit(stmt, setup='', globals=None, number=1000000)
# 
# Parameters:
# - stmt: The code to time (as string or callable)
# - setup: Code to run once before timing (imports, setup)
# - globals: Namespace for variables/functions
# - number: How many times to execute (default: 1,000,000)


# ===================================
# 3. EXAMPLE: SIEVE OF ERATOSTHENES
# ===================================

# Problem: Find all prime numbers from 1 to 150
# A prime number is only divisible by 1 and itself

print('Performance and Timeit module')
print('Finding primes from 1 to 150 - Three different approaches\n')


# ===================================
# APPROACH 1: NAIVE LIST COMPREHENSION
# ===================================
# Checks every number and tests divisibility by all numbers below it
# Time complexity: O(n³) - Very slow!

def test1():
    """
    Naive approach with unnecessary check for x == 1
    - Iterates from 1 to 150
    - For each x, checks divisibility by all y from 2 to x-1
    - Uses nested list comprehensions with any()
    - Excludes 1 manually
    """
    result = [x for x in range(1, 151) if not any(
        [x % y == 0 for y in range(2, x)]) and not x == 1]
    return 1  # Return value to ensure function executes

# Issues with test1():
# - Starts from 1 instead of 2 (1 is not prime by definition)
# - Checks every divisor up to x-1 (inefficient)
# - Nested any() with list comprehension is slow


# ===================================
# APPROACH 2: IMPROVED LIST COMPREHENSION
# ===================================
# Similar to test1 but starts from 2 (skipping 1)
# Time complexity: Still O(n³) - Still slow!

def test2():
    """
    Slightly improved version of test1
    - Starts from 2 (skipping 1 entirely)
    - Still checks all divisors from 2 to x-1
    - Uses nested list comprehension with any()
    """
    result = [x for x in range(2, 151) if not any([x % y == 0 for y in range(2, x)])]
    return 1

# Improvement over test1:
# - Eliminates unnecessary check for x == 1
# - Slightly cleaner logic
# But still inefficient: checks all divisors


# ===================================
# APPROACH 3: OPTIMIZED ALGORITHM
# ===================================
# Only checks divisors up to √n (major optimization!)
# Time complexity: O(n√n) - Much faster!

def test3():
    """
    Optimized prime finding algorithm
    - Only checks divisors up to √possiblePrime
    - Uses early termination (break when divisor found)
    - Traditional for loops instead of comprehensions
    
    Key insight: If n is divisible by x, then n = x * y
    One of x or y must be ≤ √n, so we only need to check up to √n
    """
    # Initialize a list to store primes
    primes = []
    
    for possiblePrime in range(2, 151):
        # Assume number is prime until shown it is not
        isPrime = True
        
        # Only check divisors up to √possiblePrime
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                # Found a divisor - not prime
                isPrime = False
                break  # Early termination - no need to check more
        
        if isPrime:
            primes.append(possiblePrime)
    
    # print(primes)  # Uncomment to see the actual primes
    return 1

# Why test3 is faster:
# 1. √n optimization: Checks far fewer divisors
#    - For 149: checks 2-12 instead of 2-148
# 2. Early termination: Breaks immediately when divisor found
# 3. Better algorithm design


# ===================================
# 4. BENCHMARKING THE FUNCTIONS
# ===================================

print("Timing each approach (10 iterations):\n")

# Test 1: Naive approach with x == 1 check
time1 = timeit.timeit('test1()', globals=globals(), number=10)
print(f"test1() - Naive with x==1 check: {time1:.6f} seconds")

# Test 2: Slightly improved (starts from 2)
time2 = timeit.timeit('test2()', globals=globals(), number=10)
print(f"test2() - Starts from 2:         {time2:.6f} seconds")

# Test 3: Optimized with √n limit
time3 = timeit.timeit('test3()', globals=globals(), number=10)
print(f"test3() - Optimized √n approach:  {time3:.6f} seconds")

# Calculate speedup
print(f"\nSpeedup factor (test1 vs test3): {time1/time3:.2f}x faster")
print(f"Speedup factor (test2 vs test3): {time2/time3:.2f}x faster")


# ===================================
# 5. UNDERSTANDING TIMEIT PARAMETERS
# ===================================

# Example: Different ways to use timeit

# Method 1: Timing a string statement
result1 = timeit.timeit('sum(range(100))', number=10000)
print(f"\nsum(range(100)) × 10,000: {result1:.6f} seconds")

# Method 2: Timing a function call (need globals)
def my_function():
    return sum(range(100))

result2 = timeit.timeit('my_function()', globals=globals(), number=10000)
print(f"my_function() × 10,000: {result2:.6f} seconds")

# Method 3: Timing a lambda
result3 = timeit.timeit(lambda: sum(range(100)), number=10000)
print(f"lambda × 10,000: {result3:.6f} seconds")

# Method 4: With setup code
setup = "data = list(range(1000))"
stmt = "sum(data)"
result4 = timeit.timeit(stmt, setup=setup, number=10000)
print(f"sum(data) with setup × 10,000: {result4:.6f} seconds")


# ===================================
# 6. PERFORMANCE COMPARISON EXAMPLES
# ===================================

print("\n=== Performance Comparisons ===\n")

# Example 1: List comprehension vs for loop
def using_for_loop():
    result = []
    for i in range(1000):
        result.append(i ** 2)
    return result

def using_comprehension():
    return [i ** 2 for i in range(1000)]

time_loop = timeit.timeit('using_for_loop()', globals=globals(), number=1000)
time_comp = timeit.timeit('using_comprehension()', globals=globals(), number=1000)

print(f"For loop:          {time_loop:.6f} seconds")
print(f"Comprehension:     {time_comp:.6f} seconds")
print(f"Comprehension is {time_loop/time_comp:.2f}x faster\n")


# Example 2: String concatenation methods
def concat_with_plus():
    result = ""
    for i in range(100):
        result += str(i)
    return result

def concat_with_join():
    return "".join(str(i) for i in range(100))

time_plus = timeit.timeit('concat_with_plus()', globals=globals(), number=1000)
time_join = timeit.timeit('concat_with_join()', globals=globals(), number=1000)

print(f"String + operator: {time_plus:.6f} seconds")
print(f"str.join() method: {time_join:.6f} seconds")
print(f"join() is {time_plus/time_join:.2f}x faster\n")


# Example 3: Membership testing - list vs set
def test_in_list():
    data = list(range(1000))
    return 999 in data

def test_in_set():
    data = set(range(1000))
    return 999 in data

time_list = timeit.timeit('test_in_list()', globals=globals(), number=10000)
time_set = timeit.timeit('test_in_set()', globals=globals(), number=10000)

print(f"Search in list:    {time_list:.6f} seconds")
print(f"Search in set:     {time_set:.6f} seconds")
print(f"Set is {time_list/time_set:.2f}x faster\n")


# ===================================
# 7. COMMON PERFORMANCE PATTERNS
# ===================================

print("=== Performance Best Practices ===\n")

# 1. Use built-in functions (implemented in C)
# Fast: sum([1, 2, 3, 4, 5])
# Slow: manually adding in a loop

# 2. Use list comprehensions over loops
# Fast: [x**2 for x in range(100)]
# Slow: for loop with append()

# 3. Use generators for large datasets
# Fast: (x**2 for x in range(1000000))  # Generator
# Slow: [x**2 for x in range(1000000)]  # List (uses more memory)

# 4. Use sets for membership testing
# Fast: x in {1, 2, 3, 4, 5}  # O(1) average
# Slow: x in [1, 2, 3, 4, 5]  # O(n)

# 5. Use str.join() for string concatenation
# Fast: "".join(string_list)
# Slow: result += string (in a loop)

# 6. Avoid repeated function calls
# Fast: length = len(data); for i in range(length)
# Slow: for i in range(len(data))  # len() called every iteration

# 7. Use local variables (faster than global)
# Fast: local_var = global_var; use local_var in loop
# Slow: use global_var directly in loop

# 8. Use early termination
# Fast: break when condition met
# Slow: check entire range even after finding answer


# ===================================
# 8. TIME COMPLEXITY REFERENCE
# ===================================

print("=== Time Complexity (Big O Notation) ===\n")

# O(1) - Constant: Same time regardless of input size
# Example: Accessing list element by index, dict lookup

# O(log n) - Logarithmic: Doubles input, adds one step
# Example: Binary search, balanced tree operations

# O(n) - Linear: Time grows proportionally with input
# Example: Linear search, iterating through list

# O(n log n) - Log-linear: Efficient sorting algorithms
# Example: Merge sort, quicksort (average case)

# O(n²) - Quadratic: Nested loops over same data
# Example: Bubble sort, nested iteration

# O(n³) - Cubic: Triple nested loops
# Example: test1() and test2() prime finding

# O(2ⁿ) - Exponential: Doubles with each input increase
# Example: Recursive fibonacci without memoization

# O(n!) - Factorial: Extremely slow
# Example: Generating all permutations


# ===================================
# 9. USING TIMEIT FROM COMMAND LINE
# ===================================

# You can also use timeit from terminal:
# python -m timeit "sum(range(100))"
# python -m timeit -n 1000 -r 5 "sum(range(100))"
# 
# -n: number of executions per repeat
# -r: number of repeats (takes best time)
# -s: setup statement


# ===================================
# 10. PRACTICAL EXAMPLE: OPTIMIZING CODE
# ===================================

print("\n=== Optimization Example: Finding Duplicates ===\n")

# Problem: Find duplicate numbers in a list

# Slow approach: O(n²)
def find_duplicates_slow(numbers):
    duplicates = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] == numbers[j] and numbers[i] not in duplicates:
                duplicates.append(numbers[i])
    return duplicates

# Fast approach: O(n)
def find_duplicates_fast(numbers):
    seen = set()
    duplicates = set()
    for num in numbers:
        if num in seen:
            duplicates.add(num)
        seen.add(num)
    return list(duplicates)

test_data = list(range(100)) * 2  # [0-99, 0-99]

time_slow = timeit.timeit(
    'find_duplicates_slow(test_data)', 
    globals=globals(), 
    number=100
)
time_fast = timeit.timeit(
    'find_duplicates_fast(test_data)', 
    globals=globals(), 
    number=100
)

print(f"Slow approach (O(n²)): {time_slow:.6f} seconds")
print(f"Fast approach (O(n)):  {time_fast:.6f} seconds")
print(f"Speedup: {time_slow/time_fast:.2f}x faster")


# ===================================
# COMMON USE CASES FOR TIMEIT
# ===================================

# 1. Comparing algorithm implementations
# 2. Benchmarking different data structures
# 3. Testing optimization ideas
# 4. Finding bottlenecks in code
# 5. Validating performance improvements
# 6. Making data-driven decisions about code
# 7. Performance regression testing


# ===================================
# BEST PRACTICES
# ===================================

# 1. Use timeit for micro-benchmarking
#    - Small code snippets
#    - Comparing alternatives
#    - Don't time I/O operations (unreliable)

# 2. Run enough iterations
#    - Fast code: number=1000000
#    - Slow code: number=10 or 100
#    - Get consistent, reproducible results

# 3. Use globals=globals()
#    - When timing function calls
#    - Gives access to current namespace

# 4. Focus on algorithm first
#    - Better algorithm > micro-optimizations
#    - O(n) vs O(n²) matters more than small tweaks

# 5. Profile before optimizing
#    - Don't guess where slowdowns are
#    - Use cProfile for larger programs
#    - "Premature optimization is the root of all evil"

# 6. Consider readability
#    - Optimize only when needed
#    - Readable code > slightly faster code
#    - Unless performance is critical


# ===================================
# COMMON MISTAKES
# ===================================

# 1. Not using globals parameter
# ❌ timeit.timeit('my_function()')  # NameError!
# ✅ timeit.timeit('my_function()', globals=globals())

# 2. Including setup in timing
# ❌ Timing imports or data generation
# ✅ Put setup code in setup parameter

# 3. Too few iterations
# ❌ number=1  # Unreliable timing
# ✅ number=1000 or more (depends on code speed)

# 4. Comparing apples to oranges
# ❌ Different inputs, different environments
# ✅ Same data, same machine, consistent conditions

# 5. Optimizing wrong thing
# ❌ Optimizing code that runs once
# ✅ Optimize bottlenecks in loops/repeated code

# 6. Ignoring memory usage
# ❌ Only looking at speed
# ✅ Consider memory too (space complexity)


# ===================================
# PRACTICE EXERCISES
# ===================================

# Exercise 1: Fibonacci Comparison
# Compare recursive, iterative, and memoized fibonacci implementations
# Time each for calculating fib(30)

# Exercise 2: Sorting Benchmarks
# Compare list.sort(), sorted(), and bubble sort implementation
# Test with different list sizes (100, 1000, 10000)

# Exercise 3: String Search
# Compare "substring" in string vs string.find() vs re.search()
# Which is fastest for finding patterns?

# Exercise 4: Dictionary vs List
# Build both structures with 1000 items
# Time lookup operations - measure the difference

# Exercise 5: Optimize Your Code
# Take any previous exercise you've done
# Time it, then optimize it, and compare results

# Exercise 6: Generator vs List
# Create generator and list for same data (1 million items)
# Time: sum(), max(), and iterating through all items

# Exercise 7: Custom Optimization
# Write a function to find all pairs that sum to target
# Create naive O(n²) and optimized O(n) versions
# Benchmark the difference
