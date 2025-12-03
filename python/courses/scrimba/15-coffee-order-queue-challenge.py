# Scrimba Python 101 - Exercise 15: Coffee Order Queue Challenge
#
# Topic: Infinite Loops with Break and State Management
# This exercise demonstrates using 'while True' for infinite loops,
# the 'break' statement to exit, state tracking with variables,
# and handling multiple input scenarios with conditionals.
#
# Key Concepts:
# - while True creates infinite loop (must use break to exit)
# - break statement exits loop immediately
# - continue statement skips to next iteration
# - State management with counter and accumulator variables
# - .lower() and .strip() for input normalization
# - Chaining string methods: (string.lower()).strip()
# - Conditional output based on singular/plural

# ☕ Coffee Order Queue Challenge
# 1. Set up two variables: one for total price, one for drink count
# 2. Start a while True loop
# 3. Ask for the customer's name
# 4. If the name is "done", break the loop
# 5. Ask for their drink order
# 6. If it's "latte", add 3.50 to total and +1 to drink count
#    If it's "americano", add 3.00 to total and +1 to drink count
#    If it's "espresso", add 2.50 to total and +1 to drink count
# 7. If it's not one of those drinks, print a warning and continue
# 8. After the loop, print total number of drinks and total pricet

print("""
╔════════════════════════════════════════╗
║                                     ║
║     ☕  COFFEE ORDER QUEUE ☕       ║
║                                     ║
║      Welcome! Place your order!     ║
║                                     ║
╔════════════════════════════════════════╝
""")

# Initialize counters and state
drinks = 0     # int: Counter for number of drinks ordered
total = 0      # float: Accumulator for total price
name = None    # str or None: Customer name, None indicates not collected yet

while True:  # Infinite loop - must use break to exit
    if name is None:  # First iteration - collect name
        name = input("Enter your name: ")
    else:  # Subsequent iterations - collect drink orders
        drink = input("Type the drink you want: ")
        
        # Normalize input: lowercase and remove whitespace
        if (drink.lower()).strip() == 'done':
            break  # Exit loop when customer is done ordering
        elif (drink.lower()).strip() == 'latte':
            drinks += 1
            total += 3.50  # Latte costs $3.50
        elif (drink.lower()).strip() == 'americano':
            drinks += 1
            total += 3  # Americano costs $3.00
        elif (drink.lower()).strip() == 'espresso':
            drinks += 1
            total += 2.50  # Espresso costs $2.50
        else:  # Invalid drink name
            print(
                f'"{drink}" is not a valid drink on our menu or you typed it wrong! Try again.')
            # Loop continues without incrementing counters

# Display final order summary
if total == 1:  # Check for single drink (should check drinks == 1 instead)
    print(f"Okay, {name}! Your ordered drink costs ${total:.2f}")
else:  # Multiple drinks or no drinks
    print(
        f"Great, {name}! You ordered {drinks} drinks. The total is {total:.2f}")
    # Note: Missing $ sign in total formatting
