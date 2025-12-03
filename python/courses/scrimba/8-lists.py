# Scrimba Python 101 - Exercise 8: Lists and Built-in Functions
#
# Topic: List Operations and Aggregate Functions
# This exercise demonstrates list manipulation methods (.append(), .extend())
# and built-in aggregate functions (min(), max(), sum()) for data analysis.
#
# Key Concepts:
# - List initialization and storage
# - .append() adds single element to end of list
# - .extend() adds all elements from another list
# - min() finds smallest value, max() finds largest
# - sum() calculates total of all elements
# - f-string formatting with {value:.2f} for 2 decimal places

# Week 1 and 2 sales data
sales_w1 = [7, 3, 42, 19, 15, 35, 9]  # list[int]: Complete week 1 sales (7 days)
sales_w2 = [12, 4, 26, 10, 7, 28]     # list[int]: Week 2 sales (6 days, missing 1)
sales = []                             # list: Empty list to store combined sales data

# Collect missing data point for week 2
missing_w2_day = int(
    input("How many lemonades did you sell in the last week? Type it here: "))  # int: Day 7 of week 2
sales_w2.append(missing_w2_day)  # Add missing day to week 2 list

# Combine both weeks into single list
sales.extend(sales_w1)  # Add all week 1 elements to sales
sales.extend(sales_w2)  # Add all week 2 elements to sales (now 14 total days)
print(sales)            # Display complete sales data

# Calculate and display statistics
print(f""" At your worst day, you sold {min(sales)} lemonades
At your best day, you sold {max(sales)} lemonades, awesome!
After these two weeks, your total income was ${sum(sales)*1.5:.2f}
""")
# min(sales): Lowest single day sale
# max(sales): Highest single day sale
# sum(sales)*1.5: Total lemonades × $1.50 per lemonade
# :.2f: Format as decimal with 2 places (e.g., 123.45)
