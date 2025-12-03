# Scrimba Python 101 - Exercise 11: Functions with Parameters and Defaults
#
# Topic: Function Definition, Parameters, and Default Values
# This exercise demonstrates creating functions with multiple parameters,
# using default values for optional parameters, and string formatting.
#
# Key Concepts:
# - def keyword to define functions
# - Positional parameters (name, age, color)
# - Default parameter values (age=28, color='red')
# - Parameters with defaults must come after required parameters
# - .capitalize() for proper name formatting
# - .lower() for consistent color formatting
# - Type conversion with str() for concatenation

def greeting(name, age=28, color='red'):
    # Greets user with 'name' from 'input box' and 'age', if available, default age is used
    # Parameters:
    #   name (str): User's name (required)
    #   age (int): User's age (optional, defaults to 28)
    #   color (str): Favorite color (optional, defaults to 'red')
    
    print('Hello ' + name + ', you are ' + str(age) + '!')  # Basic concatenation
    print(f'Hello {name.capitalize()}, you will be {age + 1} years old next birthday')  # F-string with calculations
    print(f"We hear you like the color {color.lower()}!")  # F-string with method call


# Collect user inputs
name = input('Enter your name: ')          # str: User's name
age = int(input('Enter your age: '))       # int: User's age (converted from string)
color = input('Enter your favorite color: ')  # str: Favorite color

# Call function with all three arguments
greeting(name, age, color)

# Exercise requirements (completed):
# 1. Add new print statement - on a new line
#    which says 'We hear you like the color xxx! xxx is a string with color
# 2. extend the function with another  input parameter 'color', that defaults to 'red'
# 3. Capture the color via an input box as variable:color
# 4. Change the 'You are xx!' text to say 'you will be xx+1 years old next birthday
#  adding 1 to the age
# 5. Capitalize first letter of the 'name', and rest are small caps
# 6. Favorite color should be in lowercase
