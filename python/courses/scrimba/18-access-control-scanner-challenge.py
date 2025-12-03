# Scrimba Python 101 - Exercise 18: Access Control Scanner Challenge
#
# Topic: Sets, Lists, and Advanced Input Validation
# This exercise demonstrates using sets for membership checking,
# lists for categorization, nested validation loops, exception handling,
# and the any() function with generator expressions.
#
# Key Concepts:
# - Sets for O(1) membership checking (fast lookup)
# - Lists for ordered, mutable collections
# - Nested while loops (outer for names, inner for badge validation)
# - try-except for error handling
# - any() with generator expression to check conditions
# - .isdigit() checks if all characters are numeric
# - sorted() returns alphabetically sorted list
# - continue skips to next loop iteration
# - break exits loop completely

# 🛂 Access Control Scanner Challenge
#
# 1. Create a set of revoked badge numbers.
# 2. Create two empty lists: "approved" and "denied".
# 3. Start a loop to collect visitor info:
#    - Ask for the visitor's name (or type "done" to finish).
#    - If the name is "done", exit the loop.
#    - Otherwise, ask for their badge number.
#    - Check if the badge is revoked:
#        • If revoked: add the name to "denied" and display "ACCESS DENIED".
#        • If not: add the name to "approved" and display "ACCESS GRANTED".
# 4. Print the final "Access Summary" for "✅ Approved Visitors" & "⛔️ Denied Visitors":
#    - Sort both lists alphabetically.
#    - Display the total number of approved and denied visitors.

# Set of revoked badge numbers (set for fast lookup)
revoked_badges = {1047, 2156, 3089, 4521, 5678, 6234, 7890, 8421, 9105, 1234}

# Lists to categorize visitors
approved = []  # list[str]: Visitors granted access
denied = []    # list[str]: Visitors denied access

while True:  # Main loop for collecting visitor information

    # Getting the name input and checking if it's 'done'
    name = input("Enter visitor's name (or type 'done' to finish): ").strip()
    
    # Validate name doesn't contain digits
    if any(char.isdigit() for char in name):  # any() returns True if any character is a digit
        print("Please, enter a valid name!")
        continue  # Skip to next iteration
    elif name.lower() == 'done':
        break  # Exit main loop

    # Getting the badge input and checking if it's a valid numeric sequence of four digits
    valid_badge = False  # bool: Flag for nested validation loop
    while valid_badge is False:  # Inner loop for badge validation
        try:
            badge_str = input("Please, enter your badge number: ").strip()
            
            # Validate badge format: must be digits and exactly 4 characters
            if not badge_str.isdigit() or len(badge_str) > 4:
                raise ValueError("Badge must be 4 digits")  # Trigger exception for invalid format
            
            badge = int(badge_str)  # int: Convert validated string to integer
            valid_badge = True  # Exit validation loop
        except ValueError:
            print("Error! Enter 4-digit numeric sequence. Try again.")
            continue  # Retry badge input

    # Checking if it's a revoked badge and granting or denying access
    if badge in revoked_badges:  # O(1) set membership check
        denied.append(name)  # Add to denied list
        print("ACCESS DENIED ⛔️")
    else:
        approved.append(name)  # Add to approved list
        print("ACCESS GRANTED ✅")

# Print final access summary with sorted lists
print(f"""
{'='*50}
           ACCESS SUMMARY
{'='*50}

✅ APPROVED VISITORS:
{sorted(approved)}

⛔ DENIED VISITORS:
{sorted(denied)}

{'='*50}
Total Approved: {len(approved)} | Total Denied: {len(denied)}
{'='*50}
""")
# sorted() returns new sorted list without modifying original
# len() counts number of elements in each list
