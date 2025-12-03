# Scrimba Python 101 - Exercise 6: String Formatting Methods
#
# Topic: String Concatenation vs F-Strings
# This exercise compares traditional string concatenation using the + operator
# with modern f-string formatting (Python 3.6+).
#
# Key Concepts:
# - String concatenation with + operator
# - F-strings (formatted string literals) with f'...'
# - String methods: .capitalize() and .lower()
# - F-strings are more readable and efficient than concatenation

# Original data in uppercase
name = 'TERRY'  # str: Name to be formatted
color = 'RED'   # str: Color to be formatted

# Method 1: Traditional concatenation with + operator
msg = '[' + name.capitalize() + '] loves the color ' + color.lower() + '!'
# Result: "[Terry] loves the color red!"

# Method 2: F-string formatting (modern, preferred approach)
msg1 = f'[{name.capitalize()}] loves the color {color.lower()}!'
# Result: "[Terry] loves the color red!" (same output, cleaner syntax)

print(msg)   # Output using concatenation
print(msg1)  # Output using f-string

# Note: Both produce identical output, but f-strings are:
# - More readable (no multiple + operators)
# - Faster (optimized by Python)
# - Easier to maintain (expressions inside {})

