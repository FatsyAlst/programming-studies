# Scrimba Python 101 - Exercise 19: Loyalty Points Engine Challenge
#
# Topic: Functions, Floor Division, and Conditional Logic
# This exercise demonstrates creating helper functions for business logic,
# using floor division to calculate points, implementing tier systems
# with conditionals, and accumulating values in a loop.
#
# Key Concepts:
# - Function definition with parameters and return values
# - Floor division (//) returns integer quotient (no decimals)
# - Accumulator pattern: incrementing totals in a loop
# - Conditional branching for tier classification
# - for loop to iterate over purchase list
# - += operator for accumulation
# - f-string formatting with :.2f for currency

# ☕️ Loyalty Points Engine Challenge
#
# RULES:
# • Each whole dollar spent earns 3 points
# • Tiers:
#     < 100 pts   →  Bronze
#     100-499 pts → Silver
#     ≥ 500 pts   →  Gold
#
# STEPS:
# 1. Define earn_points(price) → returns points for one purchase
# 2. Define tier_label(points) → returns "Bronze" / "Silver" / "Gold"
# 3. Given the hard-coded list `purchases`,
#    loop through it, call earn_points() for each amount,
#    and add the result to total_points.
# 4. After the loop, call tier_label(total_points)
# 5. Print 'Loyalty Summary':
#       • Total dollars spent
#       • Total points earned
#       • Final tier

# Initialize tracking variables
total_points = 0  # int: Accumulator for loyalty points
purchases = [12.50, 34.20, 299.99]  # list[float]: Purchase history in dollars


def earn_points(price):
    """Calculate loyalty points for a single purchase.
    
    Parameters:
        price (float): Dollar amount of purchase
        
    Returns:
        float: Points earned (3 points per whole dollar)
    """
    earned_pts = price // 1 * 3  # Floor division: get whole dollars, multiply by 3
    # Example: $12.50 // 1 = 12.0, then 12.0 * 3 = 36.0 points
    return earned_pts


def tier_label(points):
    """Determine loyalty tier based on total points.
    
    Parameters:
        points (int/float): Total accumulated points
        
    Returns:
        str: Tier name ("Bronze", "Silver", or "Gold")
    """
    if total_points < 100:  # Note: Uses global variable instead of parameter
        return 'Bronze'
    elif 100 <= total_points <= 499:  # Silver range: 100 to 499
        return 'Silver'
    elif total_points >= 500:  # Gold tier: 500 or more
        return 'Gold'


# Calculate totals by iterating through purchases
total_spent = 0  # float: Accumulator for total money spent
for purchase in purchases:  # Loop through each purchase amount
    total_points += earn_points(purchase)  # Add earned points to total
    total_spent += purchase  # Add purchase amount to total spent

# Display loyalty summary
print(f"""Total dollars spent: ${total_spent:.2f}
Total points earned: {total_points}
Final tier: {tier_label(total_points)}
""")
# :.2f formats float to 2 decimal places for currency display
# int() could be used on total_points if decimal points are not desired
