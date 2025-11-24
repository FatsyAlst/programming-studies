# Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages. 
# The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
# The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
# After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.

open_file = False
while open_file is False:
    try:
        file_name = input("Please, enter a valid file name, file path or relative path: ")
        handle = open(file_name, "r")
        open_file = True
    except:
        print("Sorry, there was an error. Check your input and try again!")

counts = dict()
for line in handle:
    if line.startswith('From '):
        line = line.split()
        counts[line[1]] = counts.get(line[1], 0) + 1

user_with_more_sent_emails = None
sent_numbers = None
for user, email_sents in counts.items():
    if user_with_more_sent_emails is None and sent_numbers is None:
        user_with_more_sent_emails = user
        sent_numbers = email_sents
    elif email_sents > sent_numbers:
        user_with_more_sent_emails = user
        sent_numbers = email_sents

print(user_with_more_sent_emails, sent_numbers)
