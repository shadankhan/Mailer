import smtplib
from email.message import EmailMessage

from email_password import email_1,password_1 # Importing email login credential


email = EmailMessage()
email['from'] = 'Your Name'
email['to'] = 'name@gmail.com'
email['subject'] = 'Welcome to Our Website!'

email.set_content("Hope You are doing great.")

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
	smtp.ehlo()
	smtp.starttls()
	smtp.login(email_1, password_1) 
	smtp.send_message(email)
	print("Done")