# Write a program which repeatedly reads numbers until the user enters "done". Onde "done" is entered, print out the total, count and average of the numbers.
# If the user enters other than a number, detect their mistake usint try and except and print an error message and skip to the next number.

total = 0
count = 0
average = None

while True:
    number = input("Enter a number or 'done' to finish: ")
    try:
        number = float(number)
    except:
        if number == 'done':
            if count == 0:
                print("You didn't enter a single number.")
                restart = None
                while restart is None:
                    restart = input("Type 'restart' if you want to go back or 'done' again to finish: ")
                    if restart == 'restart':
                        break
                    elif restart == 'done':
                        quit()
                    else:
                        restart = None
                        print("Sorry, you didn't answered me or typed something wrong. Try again.")
                        continue
                continue
            else:
                break
        else:
            print("Error (you didn't type a number). Please, try entering a number again!")
            continue

    total = total + number
    count = count + 1
    average = total/count

print(f"Total: {total}, Count: {count}, Average: {average}")


