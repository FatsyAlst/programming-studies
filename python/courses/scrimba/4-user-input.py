# Scrimba Python 101 - Exercise 4: User Input and Type Conversion
#
# Topic: input() function, Type Casting, and String Formatting
# This exercise introduces user input collection, converting strings to numbers,
# performing calculations with user data, and formatting output with f-strings.
#
# Requirements:
# - Take user's name as input
# - Take distance in kilometers as input
# - Convert km to miles (1 mile = 1.609 km)
# - Greet user and display both values
# - Use correct data types for calculations
# - Bonus: Capitalize the user's name

# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

# Collect user input
name = input('Hello, what\'s your name?\n')  # str: User's name (escaped apostrophe with \')

# Convert string input to integer for calculation
distance = int(
    input("And what distance in kilometers would you like to convert to miles?\n"))  # int: Distance in km

# Calculate conversion (note: formula appears reversed - multiplying by 1.609 converts miles to km, not km to miles)
# Correct formula should be: distance / 1.609
converted_distance = distance * 1.609  # float: Result of calculation

# Display results using f-string with multi-line formatting
print(f"""Hello, {name.capitalize()}!
{distance} km is equal to {converted_distance} miles.
""")


