import weather
import mailer

#read in emails from file
def get_emails():
    emails = {}

    email_file = open('emails2.txt', 'r')

    try:
        for line in email_file:
            (email, name) = line.split(',')
            emails[email] = name.strip()

    except FileNotFoundError as err:
        print(err)

    return emails

#read in schedule from file
def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule


def main():
    emails = get_emails()
    
    schedule = get_schedule()
    
    forecast = weather.get_weather_forecast()
    
    mailer.send_emails(emails, schedule, forecast)


main()
