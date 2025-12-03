# Scrimba Python 101 - Exercise 12: If-Elif-Else Statements
#
# Topic: Conditional Logic and Branching
# This exercise demonstrates conditional statements using if-elif-else,
# checking membership with 'in' operator, and handling multiple execution paths.
#
# Key Concepts:
# - if statement for primary condition
# - elif (else if) for alternative conditions
# - else as fallback when no conditions match
# - Nested conditionals (if inside elif)
# - Membership testing with 'in' operator
# - .strip() removes whitespace from input
# - Docstrings for function documentation

# Create a calculator which handles +,-,*,/ and outputs answer based on the mode/ operator used
# Hint: use 3 separate inputs
# Bonus: Extend functionality with extra mode so it also does celsius to fahrenheit conversion
# formula is: temp in C*9/5 + 32 = temp in f

def calculator():
    """A simple calculator that handles +, -, *, / operations
    and also converts Celsius to Fahrenheit.
    """

    # Get inputs
    print("Calculator - Available operands: +, -, *, /, c2f")
    operation = input("Enter operator: ").strip()  # .strip() removes leading/trailing whitespace

    # Special case: Temperature conversion
    if operation == 'c2f':
        temp_c = float(
            input("Enter the temperature you want to convert to fahrenheit: "))  # float: Celsius temperature
        temp_f = temp_c * 9 / 5 + 32  # float: Fahrenheit result (C * 9/5 + 32)
        print(f"{temp_c}°C is equivalent to {temp_f}°F")

    # Standard math operations
    elif operation in ['+', '-', '*', '/']:  # Check if operator is in valid list
        num_1 = float(input('Enter first number: '))   # float: First operand
        num_2 = float(input('Enter second number: '))  # float: Second operand

        # Nested conditionals for each operation
        if operation == '+':
            result = num_1 + num_2  # Addition
            print(f"{num_1} + {num_2} = {result}")

        elif operation == '-':
            result = num_1 - num_2  # Subtraction
            print(f"{num_1} - {num_2} = {result}")

        elif operation == '*':
            result = num_1 * num_2  # Multiplication
            print(f"{num_1} * {num_2} = {result}")

        else:  # Must be division since we validated operation earlier
            result = num_1 / num_2  # Division
            print(f"{num_1} / {num_2} = {result}")
            # Note: Could add zero division error handling

    # Error handling for invalid operations
    else:
        print("Error: Invalid operator!")


# Execute calculator function
calculator()
