import smtplib, ssl
import csv

        

sender_email = 'domtom1126@gmail.com'
receiver_email = 'domtom1126@gmail.com'
message = 'blank message'

# port = 465
# password = "dev_E11!ps!s"

# context = ssl. create_default_context()

# with smtplib.SMTP_SSL('smtp.gmail.com', port, context=context) as server:
#     server.connect()
#     server.login(sender_email, password)
#     server.sendmail(sender_email, receiver_email, message)
#     server.quit()
smtp_server = 'smtp.gmail.com'
port = 587

password = 'ggl_E11!ps!s'

context = ssl.create_default_context()

try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
except Exception as e:
            print(e)
finally:
            server.quit()