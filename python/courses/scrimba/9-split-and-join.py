
# Scrimba Python 101 - Exercise 9: Split and Join
#
# Topic: String Parsing with .replace() and .split()
# This exercise demonstrates parsing a delimited string with multiple separators,
# normalizing delimiters, and converting the result into a list.
#
# Key Concepts:
# - .replace() substitutes characters in a string
# - for loop with range(len()) to iterate by index
# - String membership check with 'in' operator
# - .split() without arguments splits on any whitespace
# - Strings are immutable, so reassignment is needed

# CSV-like string with mixed delimiters (commas, colons, semicolons)
csv = 'Eric,John,Michael,Terry,Graham:TerryG;Brian'
friends_list = ['Exercise: fill me with names']
# From the list above fill a list(friends_list) properly
# with the names of all the friends. One per "slot"
# you may need to run same command several times
# use print() statements to work your way through the exercise

# Normalize all delimiters to spaces by replacing each one
for ch in range(len(csv)):  # Iterate through each character index
    if csv[ch] in ":;,":    # Check if character is a delimiter
        csv = csv.replace(csv[ch], ' ')  # Replace delimiter with space
        # Note: .replace() replaces ALL occurrences, not just at index ch

print(csv)  # Output: 'Eric John Michael Terry Graham TerryG Brian'

# Split normalized string into list of names
friends_list = csv.split()  # .split() with no args splits on whitespace
print(friends_list)         # Output: ['Eric', 'John', 'Michael', 'Terry', 'Graham', 'TerryG', 'Brian']
