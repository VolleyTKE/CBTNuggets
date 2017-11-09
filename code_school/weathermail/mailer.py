import smtplib
import getpass

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