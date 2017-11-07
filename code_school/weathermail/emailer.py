import requests

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
    forecast += description + ' with a high of ' + str(temp_max)
    forecast += ' and a low of ' + str(temp_min)

    print(forecast)

def main():
    emails = get_emails()
    print(emails)

    schedule = get_schedule()
    print(schedule)

    get_weather_forecast()

main()
