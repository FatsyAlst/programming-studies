# n = None

# while n is None:
#     n = input("Enter the integer value of 'n': ")
#     try:
#         n = int(n)
#     except:
#         print("Enter a valid value for n. It must be an integer. Try again.")
#         n = None
#         continue

n = int(input())

if n % 2 != 0:
    print('Weird')
else:
    if 2 <= n <= 5:
        print('Not Weird')
    elif 6 <= n <= 20:
        print('Weird')
    elif n >= 20:
        print('Not weird')
        
