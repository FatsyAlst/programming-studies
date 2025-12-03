# Scrimba Python 101 - Exercise 5: String Slicing and Methods
#
# Topic: String Slicing, Reversal, and String Methods
# This exercise demonstrates string manipulation using slicing notation,
# the .title() method for capitalization, and combining operations.
#
# Key Concepts:
# - String slicing with [start:stop:step]
# - [::-1] reverses a string (step of -1)
# - .title() capitalizes first letter of each word
# - Method chaining (applying multiple methods in sequence)

# Basic string variable
msg = 'welcome to Python 101: Strings'  # str: Original message

print(msg)  # Output: welcome to Python 101: Strings

# Create and transform string
new_str = '1 welcome ring to tyler'  # str: String with mixed case
new_str = new_str.title()  # str: Apply title case - "1 Welcome Ring To Tyler"
print(new_str)

# Reverse string and apply title case in one expression
# [::-1] reverses the string, then .title() capitalizes each word
print(new_str[::-1].title())  # Output: "Relyt Ot Gnir Emoclew 1" (reversed and title-cased)
# Note: .title() applied after reversal, so capitalization is based on reversed string
