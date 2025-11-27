# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
# Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None

while True:
    number = input('Enter a number: ')
    try:
        number = int(number) 
    except:
        if number == 'done':
            if largest is None and smallest is None:
                print("You didn't even type a number.")
                restart = None
                while restart is None:
                    restart = input("Type 'restart' if you want to go back or 'done' if you really want to finish.: ")
                    if restart == 'restart':
                        break
                    elif restart == 'done':
                        quit()
                    else:
                        print("Error. You didn't answered me or typed wrong. Try again.")
                        restart = None
                continue
            else:
                break
        else:
            print('Invalid input')
            continue

    if smallest is None:
        smallest = number
    elif number < smallest:
        smallest = number
        
    if largest is None:
        largest = number
    elif number > largest:
        largest = number

print(f"Maximum is {largest}")
print(f"Minimum is {smallest}")