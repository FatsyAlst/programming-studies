# Scrimba Python 101 - Exercise 24: Dictionary Exercise v1.5 - Shopping Adventure
#
# Topic: Dictionary Merging and Inventory Management
# Version 1.5 adds combined inventory reporting before and after purchases.
#
# New Requirements for v1.5:
# - Combine all store inventories into ONE department_store dictionary
# - Print complete inventory BEFORE shopping begins
# - Print complete inventory AFTER all purchases are done
# - This simulates "Big Biz bought all local stores and wants constant reporting"
# 
# SECRET EASTER EGG: One item has a NEGATIVE price (-15 gold). 
# If you "buy" the minstrel, they pay YOU 15 gold instead! This is the "special way
# to make money" - a reference to Monty Python where minstrels are annoying.
#
# Key Concepts:
# - Dictionary comprehension to filter keys
# - .update() to merge multiple dictionaries
# - .pop(key, default) to safely remove items from inventory
# - Before/after state reporting
# - F-string formatting with alignment (:<30, :>6)

# It's...not really an adventure game...#Ver 1.0
# Your village is being attacked by 'a germanic tribe' and you need to run to the stores and get the right things to save your village, and probably some good looking girl or boy you want to marry. All prices in gold pieces excl. VAT... chop chop!! ze germanz are coming!
# The code should allow you to get 1 thing from each store and each item you get should be removed from the store inventory, then do same for next store...
# one way to buy by typing the key 'newt' in an input box...or something
# at end you should print the 'items' you have taken..in this version you don't have to pay for stuff or add it up
# ver 1.2 add ability to exit a store without buying and go to next by typing 'exit', and to exit if a nonexistant item is bought(typed)
# Add purse with 1000 gold pieces and payment for the items during or at end of code and show a message about total cost and how much gold you have left
# ver 1.4 random bug fix, ' browser compatability', refactoring code... basically being lazy ..stop scrolling TikTok/Facebook! ;-)
# Ver 1.5 print inventory before and after purchases as one department_store of stuff(combine inventories from all stores into one...pretend Big Biz bought all the local stores, and want constant reporting for inventory management...)
# as in all games there is a special way to do this that actually makes money and solves the problem...can you find 'them'? Do you know why? May require knowledge of actual python 'lore'


# Create store dictionaries - each has 'name' key and item:price pairs
freelancers = {
    'name': 'freelancing Shop',
    'brian': 70,
    'black knight': 20,
    'biccus diccus': 100,
    'grim reaper': 500,
    'minstrel': -15  # SECRET: Negative price! They pay YOU 15 gold!
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

# Create combined department_store inventory - merge all stores into ONE dictionary
department_store = {}

# Loop through each store and merge items (excluding 'name' key)
for shop in [freelancers, antiques, pet_shop]:
    # Dictionary comprehension: creates {item: price} dict filtering out 'name' key
    # .update() adds all key-value pairs to department_store
    department_store.update({k: v for k, v in shop.items() if k != 'name'})

# Print INITIAL INVENTORY - shows all available items before shopping starts
print("\n" + "="*60)
print("📦 DEPARTMENT STORE - INITIAL INVENTORY 📦".center(60))
print("="*60)
# Loop through all items and display with formatted alignment
for item, price in department_store.items():
    # :<30 = left-align item name in 30-character width
    # :>6 = right-align price in 6-character width
    print(f"  {item.title():<30} {price:>6} gold")
print("="*60 + "\n")

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
        item = input(
            "Enter the item you want to get or type 'exit' to finish: ").strip().lower()

        # Exit condition - user wants to leave current store
        if item == 'exit':
            break  # Exit while loop and move to next store

        # Purchase condition - item exists in current store
        elif item in items:
            items.remove(item)              # Remove from display list (for this store)
            department_store.pop(item, None)  # Remove from combined inventory (for final report)
            paid = shop[item]                # Get price from shop dictionary
            purse -= paid                    # Deduct cost from purse (can be negative!)
            cart[item] = paid                # Add item and price to cart
            print(f"{item.capitalize()} purchased! Paid {paid} gold pieces. You now have {purse} pieces.")

            # Auto-exit if store is now empty (better UX - no need to type 'exit')
            if len(items) == 0:
                print(
                    f"You purchased all the items from {shop['name'].title()}. Heading to the next store.")
                break  # Exit while loop automatically

        # Error condition - item doesn't exist in current store
        else:
            print("Item not found! Try again.")
            continue  # Loop back to ask for input again

# Calculate total cost by summing all prices in cart
total_cost = sum(cart.values())

# Create comma-separated string of purchased items for display
bought_items = ", ".join(list(cart.keys()))

# Print FINAL INVENTORY - shows what's left after all purchases
print("\n" + "="*60)
print("📦 DEPARTMENT STORE - FINAL INVENTORY 📦".center(60))
print("="*60)
# Check if any items remain in inventory
if department_store:
    # Display remaining items with same formatting as initial inventory
    for item, price in department_store.items():
        print(f"  {item.title():<30} {price:>6} gold")
else:
    # All items were purchased - celebrate!
    print("  🎉 ALL ITEMS SOLD OUT! 🎉".center(60))
print("="*60 + "\n")

# Show quest completion summary
print("\n" + "="*50)
print("🏰 QUEST COMPLETE! 🏰".center(50))
print("="*50)
print(f"\n📦 Items purchased: {bought_items}")
print(f"\n💰 Total cost: {total_cost} gold pieces")
print(f"💵 Gold remaining: {purse} gold pieces")
print("\n" + "="*50)
print("May these items save your village! ⚔️".center(50))
print("="*50)
