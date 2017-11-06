emails = []

email_file = open('emails.txt', 'r')
try:
    for line in email_file:
        emails.append(line.strip())
except FileNotFoundError as err:
    print(err)
print(emails)
