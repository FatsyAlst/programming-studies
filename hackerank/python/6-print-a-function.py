# Without using any string methods, try to print the following

# "123...n"

# Note that "..." represents the consecutive values in between.

n = input()

ns = int(n)

if ns == 1:
    print(ns)
if ns != 1:
    for i in range(1, ns + 1):
        print(i, end="")