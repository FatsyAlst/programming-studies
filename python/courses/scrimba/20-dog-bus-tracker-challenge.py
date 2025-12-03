# Scrimba Python 101 - Exercise 20: Dog Bus Tracker Challenge
#
# Topic: Nested Dictionaries and Dictionary Manipulation
# This exercise demonstrates working with nested dictionaries (dictionaries
# containing dictionaries), dynamic key assignment, safe dictionary iteration
# during modification, and complex data structure management.
#
# Key Concepts:
# - Nested dictionaries: dict[key] = {'nested_key': value}
# - .items() returns key-value pairs for iteration
# - .keys() returns dictionary keys
# - max(dict.keys()) finds highest key value
# - Dynamic key assignment with max(bus.keys()) + 1
# - list(dict.items()) creates snapshot to avoid iteration errors
# - del dict[key] removes key-value pair
# - Dictionary access with dict[key]['nested_key']
# - ValueError for custom error handling
# - .capitalize() for name formatting

# 🐾 Dog Bus Tracker — Challenge Steps
#
# 1. Start with a bus dictionary holding current passengers.
#    - Each seat number (1, 2, 3, ...) is a key
#    - Each value is another dictionary with each pet's:
#        • name
#        • breed
#        • pickup time
#        • dropoff time
#
# 2. Print a starting roster showing each pet’s seat, name, and pickup time.
#
# 3. Add one new pet if there’s room on the bus.
#    - Use MAX_SEATS to limit capacity.
#    - Dynamically assign the next seat number.
#    - Print the updated roster showing all pets after pickup.
#
# 4. Ask which pet leaves early.
#    - Remove that pet from the bus.
#    - Print a message saying they’ve headed home.
#
# 5. Print a final roster listing the remaining pets and their dropoff times.

max_seats = 6  # int: Maximum bus capacity

# Nested dictionary structure: seat number -> dog information dictionary
bus = {
    1: {
        'name': 'Max',
        'breed': 'Golden Retriever',
        'pickup': '08:00',
        'dropoff': '17:00'
    },
    2: {
        'name': 'Luna',
        'breed': 'Husky',
        'pickup': '08:15',
        'dropoff': '16:30'
    },
    3: {
        'name': 'Charlie',
        'breed': 'Beagle',
        'pickup': '08:30',
        'dropoff': '17:15'
    },
    4: {
        'name': 'Bella',
        'breed': 'Poodle',
        'pickup': '08:45',
        'dropoff': '16:00'
    }
}

print("=" * 50)
print("🐾 DOG BUS - STARTING ROSTER 🚌")
print("=" * 50)
for seat, dog in bus.items():
    print(f"Seat {seat}: {dog['name']} | Pickup: {dog['pickup']}")
print("=" * 50)

if len(bus) != max_seats:
    print(f"\nWe still have {max_seats - len(bus)} free seats!\n")

while len(bus) != max_seats:
    try:
        dog_infos = input(
            "Please, enter all infos (name | breed | pickup | dropoff) of our new friend: ").strip().split()

        # Validate that user provided exactly 4 pieces of information
        if len(dog_infos) != 4:
            # Raise ValueError with custom message that will be caught by except block
            raise ValueError("Please provide all 4 pieces of information")

        # Dynamically find next available seat number
        # If bus has seats, take max seat number + 1; if empty, start at 1
        # This works even if seats aren't sequential (e.g., after deletions)
        next_seat = max(bus.keys()) + 1 if bus else 1

        bus[next_seat] = {
            'name': dog_infos[0].capitalize(),
            'breed': dog_infos[1].capitalize(),
            'pickup': dog_infos[2],
            'dropoff': dog_infos[3]
        }
    except ValueError as e:
        # 'e' contains the error message - either our custom one or Python's built-in
        print(f"Invalid input: {e}. Try again.")
        continue

print("=" * 50)
print("🐾 DOG BUS - UPDATED STARTING ROSTER 🚎")
print("=" * 50)
for seat, dog in bus.items():
    print(f"Seat {seat}: {dog['name']} | Pickup: {dog['pickup']}")
print("=" * 50)

while True:
    name = input(
        "Does some dog leave early? If yes, type his name (or 'done' to end): ").strip().lower()
    if name == 'done':
        break
    try:
        deleted = False

        # Convert to list to avoid "dictionary changed size during iteration" error
        # This creates a snapshot of bus items before we modify the dictionary
        for seat, dog in list(bus.items()):
            if name == dog['name'].lower():
                del bus[seat]
                deleted = True
                print(f"{name.capitalize()} went to home earlier")
                break  # Stop searching once we found and removed the dog

        # If no dog was found with that name, raise an error
        if deleted is False:
            raise ValueError
    except ValueError:
        print("That's not a valid name or this dog is not in the bus. Try again.")
        continue

print("=" * 50)
print("🐾 DOG BUS - FINAL ROSTER 🚌")
print("=" * 50)
for seat, dog in bus.items():
    print(f"Seat {seat}: {dog['name']} | Dropoff: {dog['dropoff']}")
print("=" * 50)
