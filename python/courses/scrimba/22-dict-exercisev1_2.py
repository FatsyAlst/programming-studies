# Scrimba Python 101 - Exercise 22: Dictionary Exercise v1.2 - Shopping Adventure
#
# Topic: Dictionary Manipulation with Advanced Features
# Version 1.2 adds exit functionality, payment system with purse, and inventory management.
#
# New Requirements for v1.2:
# - Add ability to exit a store without buying by typing 'exit'
# - Exit if a non-existent item is attempted
# - Add purse with 1000 gold pieces
# - Track and deduct payment for items
# - Show total cost and remaining gold
#
# Key Concepts:
# - .pop() to remove items and get their price
# - Financial tracking with running totals
# - Multiple exit conditions in loops
# - Error handling for invalid items

# It's...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get
# the right things to save your village, and probably some good looking girl or boy you want to
# marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!

# The code should allow you to get 1 thing from each store and each item you get should be removed
# from the store inventory, then do same for next store...

# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for
# stuff or add it up

# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit
# if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a
# message about total cost and how much gold you have left


# Create store dictionaries - each has 'name' key and item:price pairs
freelancers = {
    'name': 'freelancing Shop',
    'brian': 70,
    'black knight': 20,
    'biccus diccus': 100,
    'grim reaper': 500,
    'minstrel': -15  # Note: Negative price - they pay YOU! (hint for v1.5)
}

antiques = {
    'name': 'Antique Shop',
    'french castle': 400,
    'wooden grail': 3,
    'scythe': 150,
    'catapult': 75,
    'german joke': 5
}

pet_shop = {
    'name': 'Pet Shop',
    'blue parrot': 10,
    'white rabbit': 5,
    'newt': 2
}

# Purse with 1000 gold pieces
purse = 1000

# Create an empty shopping cart - will store {item: price}
cart = {}

# Loop through each store in sequence
for shop in (freelancers, antiques, pet_shop):
    # Create list of available items (filter out 'name' key using list comprehension)
    items = [item for item in shop if item != 'name']
    
    # Welcome message showing store name and available items
    print(f"Welcome to {shop['name'].title()}! Items for sale: {items}")

    # Shopping loop - allows multiple purchases per store
    while True:
        # Get user input, normalize with .strip() (remove spaces) and .lower() (case-insensitive)
        item = input("Enter the item you want to get or type 'exit' to finish: ").strip().lower()

        # Exit condition - user wants to leave current store
        if item == 'exit':
            break  # Exit while loop and move to next store
        
        # Purchase condition - item exists in current store
        elif item in items:
            items.remove(item)              # Remove from display list
            paid = shop[item]                # Get price from shop dictionary
            purse -= paid                    # Deduct cost from purse
            cart[item] = shop[item]          # Add item and price to cart
            print(f"{item.capitalize()} purchased! Paid {paid} gold pieces. You now have {purse} pieces.")
            
            # Auto-exit if store is now empty (better UX - no need to type 'exit')
            if len(items) == 0:
                print(f"You purchased all the items from {shop['name'].title()}. Heading to the next store.")
                break  # Exit while loop automatically
        
        # Error condition - item doesn't exist in current store
        else:
            print("Item not found! Try again.")
            continue  # Loop back to ask for input again

# Calculate total cost by summing all prices in cart
total_cost = sum(cart.values())

# Create comma-separated string of purchased items for display
bought_items = ", ".join(list(cart.keys()))

# Show remaining gold in purse
print("\n" + "="*50)
print("🏰 QUEST COMPLETE! 🏰".center(50))
print("="*50)
print(f"\n📦 Items purchased: {bought_items}")
print(f"\n💰 Total cost: {total_cost} gold pieces")
print(f"💵 Gold remaining: {purse} gold pieces")
print("\n" + "="*50)
print("May these items save your village! ⚔️".center(50))
print("="*50)
