# Scrimba Python 101 - Exercise 17: Phone Number Normalizer Challenge
#
# Topic: String Manipulation and Input Validation
# This exercise demonstrates cleaning and normalizing user input by
# removing unwanted characters, validating format, and reformatting
# to a standard phone number format.
#
# Key Concepts:
# - while loop for input validation with retry logic
# - .strip() removes leading/trailing whitespace
# - .replace() substitutes characters (chain multiple calls)
# - .split() without args breaks string on whitespace into list
# - .join() combines list elements into single string
# - String slicing [start:end] to extract portions
# - len() to validate string length
# - f-string formatting for output template

# 📱 Phone Number Formatter
#
# 1. Ask the user to enter a U.S. phone number in **any format**.
# 2. Use .strip() to remove any leading/trailing spaces.
# 3. Replace common separators (-, (, ), .) with spaces.
# 4. Use .split() to break into chunks, then .join() to merge the digits.
# 5. Check if the cleaned number has **exactly 10 digits**.
# 6. If yes, format it like this: (123) 456-7890
# 7. If not, print an error message: "Please enter exactly 10 digits."

# Input validation loop
formated = False  # bool: Flag to control loop (note: typo should be 'formatted')
while formated is False:  # Continue until valid input received
    number = input("Please, enter your phone number: ")  # str: Raw user input
    
    # Clean the input: remove whitespace and replace separators with spaces
    number = number.strip().replace('-', ' ').replace(',', ' ').replace('.', ' ')
    # Note: Missing replacements for '(' and ')' as mentioned in requirements
    
    number = number.split()  # list[str]: Split on whitespace into chunks
    number = ''.join(number)  # str: Rejoin chunks with no separator (digits only)

    # Validate length
    if len(number) == 10:  # Check if exactly 10 digits
        formated = True  # Exit loop
    else:
        print("Input error! Please, enter exactly 10 digits")  # Error message and retry
        # Note: Line ends with backslash (syntax error if continued on next line)

# Format phone number to standard U.S. format: (XXX) XXX-XXXX
number = f"({number[0:3]}) {number[3:6]}-{number[6:]}"  # String slicing to extract parts
# [0:3] = area code (first 3 digits)
# [3:6] = exchange (next 3 digits)
# [6:] = line number (remaining 4 digits)

print(number)  # Output formatted number
