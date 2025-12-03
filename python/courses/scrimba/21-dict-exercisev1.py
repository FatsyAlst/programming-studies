# Scrimba Python 101 - Exercise 21: Dictionary Exercise v1 - Shopping Adventure
#
# Topic: Dictionary Manipulation and Nested Data Structures
# This exercise demonstrates looping through multiple dictionaries,
# filtering dictionary keys, managing a shopping cart with nested lists,
# using .setdefault() for dynamic list creation, and .pop() for item removal.
#
# Key Concepts:
# - Looping through multiple dictionaries in a list
# - List comprehension to filter dictionary keys
# - .setdefault() to create keys with default values
# - .append() to add items to lists stored in dictionary
# - .pop() to remove items from dictionaries
# - while True loop with break for user input
# - .strip() and .lower() for input normalization
# - Dictionary iteration with .items()
# - .join() to format list items as strings

# It's...not really an adventure game...#Ver 1.0

# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get
# the right things to save your village, and probably some good looking girl or boy you want to
# marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!

# The code should allow you to get 1 thing from each store and each item you get should be removed
# from the store inventory, then do same for next store...

# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you
# don't have to pay for stuff or add it up


# Create store dictionaries - each has 'name' key and item:price pairs
freelancers = {
    'name': 'freelancing Shop',  # Store name (not for sale)
    'brian': 70, 'black knight': 20,
    'biccus diccus': 100,
    'grim reaper': 500,
    'minstrel': -15
        }

antiques = {
    'name': 'Antique Shop',
    'french castle': 400,
    'wooden grail': 3,
    'scythe': 150,
    'catapult': 75,
    'german joke': 5
        }

pet_shop = {'name': 'Pet Shop',
    'blue parrot': 10,
    'white rabbit': 5,
    'newt': 2
        }

# Creating an empty cart - will store {store_name: [list of items]}
cart = {}

# Loop through each store dictionary
for store in [freelancers, antiques, pet_shop]:
    # Filter out 'name' key to show only purchasable items
    # Looping directly over dict iterates through keys
    items = [item for item in store if item != 'name']
    
    # Welcome message showing store name and available items
    print(f"Welcome to {store['name'].title()}! Items for same: {items}")
    
    # Inner loop to allow multiple purchases per store
    while True:
        # Get user input, normalize with .strip() and .lower()
        item = input("Enter the item you want to get or type 'done' to finish: ").strip().lower()
        
        if item == 'done':
            break  # Exit store and move to next one
        elif item in items:
            # setdefault creates empty list if store not in cart yet
            # Then immediately append the item to that list
            cart.setdefault(store['name'], []).append(item)
            print(f"{item.capitalize()} purchased!")
        else:
            # Item doesn't exist in this store
            print("Item not found! Try again.")
            continue  # Ask for input again

# Display final purchase summary with ASCII art
print(f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║   ⚔️  VILLAGE SAVED! THE GERMANS HAVE RETREATED! ⚔️        ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝

🛒 YOUR HEROIC PURCHASES:
""")

# Loop through cart dictionary - store name and list of items
for store, items in cart.items():
    # .join() converts list to comma-separated string
    print(f"   📦 From {store}: {', '.join(items)}")

print(f"""
╔════════════════════════════════════════════════════════════╗
║                                                            ║
║  🎉 Today it is all FREE! Have a nice day of mayhem! 🎉    ║
║                                                            ║
║         The village (and that cute person) thank you!      ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
""")


