# Scrimba Python 101 - Exercise 13: Conditional Optimization
#
# Topic: Refactoring Conditionals and Logic Flow
# This exercise demonstrates identifying and fixing conditional logic issues,
# specifically the bug where 'if' should be 'elif' for proper branching.
#
# Key Concepts:
# - if vs elif: 'if' starts new condition, 'elif' continues same conditional chain
# - Multiple 'if' statements all execute independently
# - elif only executes if previous conditions were False
# - Membership testing with 'in' operator for multiple values
# - Bug in original: First 'if' should be 'elif' to prevent overwriting days variable

def num_days(month):
    """Returns the number of days in a given month.
    
    Parameters:
        month (str): Three-letter lowercase month abbreviation
        
    Note: Original code has a bug - the second 'if' should be 'elif'
    Without elif, 'apr' matches both first and second conditions,
    overwriting days from 31 to 30.
    """

    if month in ['jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec']:
        days = 31  # Months with 31 days
    if month in ['apr', 'jun', 'sep', 'nov']:  # BUG: Should be 'elif' not 'if'
        days = 30  # Months with 30 days
    elif month == 'feb':
        days = 28  # February (not accounting for leap years)

    print('number of days in', month, 'is', str(days))


num_days('oct')
# optimize/shorten the code in the function
# try to reduce the number of conditionals

# Bug explanation:
# The second 'if' should be 'elif' because using 'if' creates independent checks.
# This means if month='apr', it would set days=31 (first if), then immediately
# overwrite to days=30 (second if). Using 'elif' ensures only one branch executes.
