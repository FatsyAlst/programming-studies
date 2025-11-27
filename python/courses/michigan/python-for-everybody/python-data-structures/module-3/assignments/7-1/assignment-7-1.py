# Write a program that prompts for a file name, then opens that file and reads through the file, and print the contents of the file in upper case. 
# Use the file words.txt to produce the output below.

# You can download the sample data at http: //www.py4e.com/code3/words.txt

file_name = input('Enter file name: ')

try:
    handle = open(file_name, "r")
except:
    print("Error, you didn't entered a valid file name.")
    quit()

for line in handle:
    line = line.strip()
    line = line.upper()
    print(line)

# text = handle.read()
# UPPER = text.upper()

# print(UPPER)

handle.close()