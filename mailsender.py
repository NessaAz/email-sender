import email
from email.message import EmailMessage
from re import sub
from passw import password
import ssl, smtplib

mail_sender = 'vanessamwikali@gmail.com'
mail_password = password

mail_receiver = 'ireportermoringa@gmail.com'
subject = 'Welcome to the future of newsletting'
body = '''
feel free to ask about anything
'''

email_message= EmailMessage()
email_message['from'] = mail_sender
email_message['to'] = mail_receiver
email_message['subject'] = subject
email_message.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(mail_sender, mail_password)
    smtp.sendmail(mail_sender, mail_receiver, email_message.as_string())