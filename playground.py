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

drinks = 0
total = 0
name = None

while True:
    if name is None:
        name = input("Enter your name: ")
    else:
        drink = input("Type the drink you want: ")
        if (drink.lower()).strip() == 'done':
            break
        elif (drink.lower()).strip() == 'latte':
            drinks += 1
            total += 3.50
        elif (drink.lower()).strip() == 'americano':
            drinks += 1
            total += 3
        elif (drink.lower()).strip() == 'espresso':
            drinks += 1
            total += 2.50
        else:
            print(
                f'"{drink}" is not a valid drink on our menu or you typed it wrong! Try again.')

if total == 1:
    print(f"Okay, {name}! Your ordered drink costs ${total:.2f}")
else:
    print(
        f"Great, {name}! You ordered {drinks} drinks. The total is {total:.2f}")
