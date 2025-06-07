from email.message import EmailMessage
import ssl
import smtplib



email_sender = 'sender_mail@xyz.com' # Replace sender_mail@xyz.com with the mail you want send email
email_password = 'password' # Password from app password

email_receiver = 'xyz@mail.com' # Receiver's mail

subject = "Holy Crow Erm What the sigma"
body = """
Hit me on my discord 'mediator.av'  
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMPT_SSL('smpt.gmail.com', 465, context = context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender,email_receiver, em.as_string())
