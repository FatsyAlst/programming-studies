# Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
# You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

# From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

# Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.

open_file = False
while open_file is False:
    try:
        file_name = input("Please, enter a valid file name, path or relative path: ")
        open_file = True
    except:
        print("Error. Please, check your answer and try again.")

handle = open(file_name, "r")

hour_frequency = dict()
for line in handle:
    if line.startswith("From "):
        line = line.split()
        time_info = line[5]
        time_info = time_info.split(":")
        hour = time_info[0]
        hour_frequency[hour] = hour_frequency.get(hour, 0) + 1

for h, f in sorted(hour_frequency.items()):
    print(h, f)
