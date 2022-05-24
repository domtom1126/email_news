import smtplib
import os

from get_news import getNews

# Email address and password come from env variables
EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()

    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    subject = 'Test email'
    body = getNews()

    msg = f'Subject: {subject}\n\n{body}'

    smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, msg)