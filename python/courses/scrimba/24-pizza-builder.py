#  🍕 Pizza Builder — Challenge Steps
#
# 1. Define a Pizza class that stores:
#    - size, crust type, and a list of toppings
# 2. Add a method to add a new topping
# 3. Add a method to remove a topping if it exists
# 4. Add a method to print pizza details:
#    - size, crust, and all toppings (or “No toppings yet!”)
# 5. Create a pizza object, customize it, and print the summary

class Pizza:
    """
    A Pizza class that stores size, crust type, and toppings.
    Allows customization by adding/removing toppings and printing details.
    """
    
    def __init__(self, size, crust_type, toppings = None):
        """
        Initialize a Pizza object.
        
        Parameters:
        - size (str): The size of the pizza (e.g., "Small", "Medium", "Large")
        - crust_type (str): The crust type (e.g., "Thin", "Thick", "Stuffed")
        - toppings (list, optional): List of topping strings. Defaults to empty list if None.
        
        Notes:
        - All inputs are cleaned (.strip()) and capitalized for consistency
        - Uses list comprehension to process each topping if provided
        """
        # Clean and capitalize size and crust type for consistency
        self.size = size.strip().capitalize()
        self.crust_type = crust_type.strip().capitalize()
        # If toppings provided, clean and capitalize each one; otherwise start with empty list
        self.toppings = [topping.strip().capitalize() for topping in toppings] if toppings is not None else []

    def new_topping(self, topping):
        """
        Add a new topping to the pizza.
        
        Parameters:
        - topping (str): The topping to add (e.g., "Pepperoni", "Mushrooms")
        """
        self.toppings.append(topping)
    
    def remove_topping(self, topping):
        """
        Remove a topping from the pizza if it exists.
        
        Parameters:
        - topping (str): The topping to remove
        
        Note: Will raise ValueError if topping doesn't exist in the list
        """
        self.toppings.remove(topping)
    
    def print_details(self):
        """
        Print a formatted summary of the pizza's details.
        
        Displays:
        - Size
        - Crust type
        - All toppings (comma-separated) or "No toppings selected" if empty
        """
        print(f"""====== PIZZA DETAILS ======
Size: {self.size}
Crust type: {self.crust_type}
{f"Toppings: {', '.join(self.toppings)}" if self.toppings else "No toppings selected"}
              """)


# Create two pizza instances
pizza1 = Pizza("Large", "Thin")  # Empty pizza (no toppings yet)
pizza2 = Pizza("Large", "Thin", ["pepperoni"])  # Pizza with initial topping

# Test pizza2: print initial state, add topping, print again
pizza2.print_details()
pizza2.new_topping("Mushrooms")
pizza2.print_details()


# ========================================
# To the me of the future when I get back here again:
# ========================================
# 
# 🎯 CHALLENGES TO IMPROVE THIS CODE:
#
# 1. **Add input validation to new_topping()**
#    - Format the topping with .strip().capitalize() before adding
#    - Check if topping already exists (avoid duplicates)
#    - Return a message like "Topping already on pizza!" if duplicate
#
# 2. **Improve remove_topping() error handling**
#    - Format the topping with .strip().capitalize() before removing
#    - Use 'if topping in self.toppings' to check existence first
#    - Print friendly message instead of crashing with ValueError
#
# 3. **Add a price calculator method**
#    - Base price by size: Small=$8, Medium=$10, Large=$12, Extra Large=$15
#    - Each topping costs $1.50
#    - Premium toppings (pepperoni, bacon, chicken) cost $2.00
#    - Return total price as formatted string: "$14.50"
#
# 4. **Add a __str__() or __repr__() method**
#    - Make print(pizza2) work without calling .print_details()
#    - Return formatted string instead of printing directly
#
# 5. **Create class-level constants**
#    - VALID_SIZES = ["Small", "Medium", "Large", "Extra Large"]
#    - VALID_CRUSTS = ["Thin", "Thick", "Stuffed", "Pan"]
#    - Validate inputs against these in __init__()
#
# 6. **Add a reset() method**
#    - Clear all toppings from the pizza
#    - Useful for "starting over" without creating new object
#
# 7. **Bonus: Add a copy() method**
#    - Create a duplicate pizza with same attributes
#    - Test: pizza3 = pizza2.copy()
#    - Hint: Look into copy.deepcopy() or manual creation
#
# Good luck, future me! 🍕
