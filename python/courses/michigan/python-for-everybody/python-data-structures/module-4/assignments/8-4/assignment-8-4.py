# TODO
# Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() method. 
# The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
# When the program completes, sort and print the resulting words in python sort() order as shown in the desired output.

# You can download the sample data at http://www.py4e.com/code3/romeo.txt

# ========================================
# THE .SPLIT() METHOD - EXPLANATION
# ========================================
# The .split() method breaks a string into a list of substrings
# based on a specified separator (delimiter).
#
# SYNTAX: string.split(separator, maxsplit)
#
# PARAMETERS:
# - separator (optional): The delimiter where splits occur.
#                        Default is any whitespace (spaces, tabs, newlines).
# - maxsplit (optional): Maximum number of splits to perform.
#                       Default is -1 (all occurrences).
#
# RETURN VALUE: A new list containing the split substrings.
#
#

open_file = False

while open_file is False:
    try:
        file_name = input('Enter file name: ')
        handle = open(file_name, "r")
        open_file = True
    except:
        print("You didn't entered a valid file name or typed it wrong! Try again.")

words = list()
for line in handle:
    line = line.split()
    for word in line:
        if not word in words: words.append(word)

words.sort()

print(words)