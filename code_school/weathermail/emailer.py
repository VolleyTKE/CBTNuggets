import requests
import smtplib
import getpass

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

    username = user()
    password = secure_password()

    #start encryption
    server.starttls()

    #login
    server.login(username, password)

	#for testing
    #to_email = 'chris.a.carr@gmail.com'
    #test_message = 'Subject: Welcome to the circus:\n' + 'test body'

    #send to entire email list
    for to_email, name in emails.items():
	    message = 'Subject: Welcome to the circus!\n'
	    message += 'Hi, ' + name + '\n\n' + 'We are reaching out to you with exciting news!\n\n'
	    message += forecast + '\n\n'
	    message += 'The Schedule is:\n' + schedule
	    server.sendmail(username, to_email, message)
		
    quit()

#username function
def user():
    user = 'cvg.developer@gmail.com'
    return user

#password, never save in script or plan text
def secure_password():
    password = getpass.getpass("Password: ")
    return password

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    forecast = get_weather_forecast()
    print(forecast)

    send_emails(emails, schedule, forecast)


main()
