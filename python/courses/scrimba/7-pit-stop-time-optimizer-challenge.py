# Scrimba Python 101 - Exercise 7: Pit Stop Time Optimizer Challenge
#
# Topic: User Input, Calculations, Rounding, and Conditional Logic
# This exercise combines multiple concepts: collecting numeric input,
# performing calculations with floats, rounding results, and using
# conditional statements to provide feedback.
#
# Key Concepts:
# - Type casting with float() and int()
# - Percentage calculations
# - round() function with decimal places
# - if statement for conditional output
# - String formatting with f-strings

# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"

# Collect race data from user
race_time_seconds = float(input("Enter the race time (in seconds): "))  # float: Total race duration
pit_stops = int(input("Enter how many pit stops the driver did: "))     # int: Number of pit stops
avg_pit = float(input("Enter the average time of pit stops (in seconds): "))  # float: Average pit stop duration

# Calculate pit stop metrics
total_pit_stop_time = pit_stops * avg_pit  # float: Total time spent in pits
in_pit_percentage = (total_pit_stop_time / race_time_seconds) * 100  # float: Percentage of race time
in_pit_percentage = round(in_pit_percentage, 2)  # float: Rounded to 2 decimal places

# Print results
print("\n--- Pit Stop Summary ---")
print(f"Total pit stop time: {total_pit_stop_time} seconds")
print(f"Percentage of race in pits: {in_pit_percentage}%")

# Conditional feedback based on performance
if in_pit_percentage > 5:
    print("You need a new pit crew. 🛠️")  # Displayed only if pit time exceeds 5% threshold
