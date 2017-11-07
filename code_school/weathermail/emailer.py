import requests
import smtplib

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

def get_schedule():
    try:
        schedule_file = open('schedule.txt', 'r')
        schedule = schedule_file.read()
    except FileNotFoundError as err:
        print(err)

    return schedule

def get_weather_forecast():
    url = 'http://api.openweathermap.org/data/2.5/weather?zip=63104,us&units=imperial&appid=8917ff3d94488468bf8493d0515f13d2'
    weather_request = requests.get(url)
    weather_json = weather_request.json()
    #print(weather_json)

    description = weather_json['weather'][0]['description']
    print(description)
    temp_min = weather_json['main']['temp_min']
    temp_max = weather_json['main']['temp_max']
    print(temp_min)
    print(temp_max)

    forecast = 'The circus forecast for today is '
    forecast += description + ' with a high of ' + str(int(temp_max))
    forecast += ' and a low of ' + str(int(temp_min))

    return forecast

def send_emails(emails, schedule, forecast):
    #connect to smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')

    #start encryption
    username = user()
    password = secure()
    server.starttls()
    server.login(username, password)

    to_email = 'chris.a.carr@gmail.com'
    test_message = 'test body'
    server.sendmail(username, to_email, test_message)
    quit()

def user():
    user = 'cvg.developer@gmail.com'
    return user

def secure():
    password = input('password:')
    return password

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule,forecast)


main()
