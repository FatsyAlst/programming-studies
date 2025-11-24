# For all non-negative integers i < n² print i² (n is the input)

set_number = False
while set_number is False:
    try:
        number = int(input())
        set_number = True
    except:
        print("Error. Only integeres are alowed. Try again.")

for n in range(number): # gera uma lista que vai de 0 até n-1
    print((n)**2)