# Scrimba Python 101 - Exercise 16: For Loops
#
# Topic: For Loop Iteration and String Formatting
# This exercise demonstrates iterating over lists with for loops,
# collecting user input to extend lists, combining lists, and
# applying string formatting functions to each element.
#
# Key Concepts:
# - for loop iterates over each item in a sequence
# - Loop variable (name) holds current item
# - .append() adds single item to list
# - .extend() adds all items from another list
# - .title() capitalizes first letter of each word
# - .strip() removes leading/trailing whitespace
# - Helper functions for reusable formatting logic
# - Docstrings document function behavior and types

# Initial guest lists with mixed capitalization
names = ['john ClEEse', 'Eric IDLE', 'michael']  # list[str]: First group of guests
names1 = ['graHam chapman', 'TERRY', 'terry jones']  # list[str]: Second group of guests

# Collect additional guests from user input
extra_friend_1 = input(
    "Hey, who more do you want to invite to the party? Enter the name here: ")  # str: Additional guest 1
extra_friend_2 = input("Whoa, one more person to the party? Tell me who: ")  # str: Additional guest 2

# Add extra guests to respective lists
names.append(extra_friend_1)   # Add first extra guest to names
names1.append(extra_friend_2)  # Add second extra guest to names1

# Combine both lists into one
names.extend(names1)  # Add all elements from names1 to names


def format_name(name):
    """ (str) -> str
    
    Return a title formated string
    """
    return name.title()  # Convert to title case (First Letter Uppercase)


# Iterate through all guests and send invitation
for name in names:  # Loop variable 'name' holds each guest name in sequence
    # Format name, strip whitespace, and print personalized invitation
    print(f"{format_name(name).strip()}! You are invited to the party on Friday!")
    # .strip() removes extra spaces that might exist in names
    # format_name() ensures consistent capitalization
