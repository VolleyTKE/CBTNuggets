emails = {}

email_file = open('emails2.txt', 'r')

try:
    for line in email_file:
        (email, name) = line.split(',')
        emails[email] = name

except FileNotFoundError as err:
    print(err)

print(emails)
