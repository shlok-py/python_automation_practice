'''
This Program Sends an email "basic email texts"
'''

import smtplib
import ssl
from email.message import EmailMessage

from matplotlib.style import context

subject = "email from python"
body = "This is an email sent from python program!!"
sender = "codnepal173@gmail.com"
receiver = "shlokkoirala19@gmail.com"
password = input("Enter the password")


message = EmailMessage()
message["From"]= sender
message["To"] = receiver
message["Subject"] = subject
# message.set_content(body)
#The above line is an alternative for the followning html code

html = f"""
<html>
<body>
<h1>{subject}</h1>
<p>{body}</p>
</body>
<html>

"""

message.add_alternative(html, subtype = "html")

context = ssl.create_default_context()
print("sending email")
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context= context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, message.as_string())

print("email sent")