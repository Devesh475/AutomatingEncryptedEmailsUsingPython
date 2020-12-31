from email.message import EmailMessage
from encryptMessage import encrypt_message
import smtplib


def send_email(receiver, subject, body):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login('sender@gmail.com', 'password')
    email = EmailMessage()
    email['From'] = 'sender@gmail.com'
    email['To'] = receiver
    email['Subject'] = encrypt_message(subject)
    body = encrypt_message(body)
    email.set_content(body)
    server.send_message(email)


receiver = input('To whom you want to send the mail')
subject = input('what do you want the subject to be')
body = input('please tell the content of the mail')

send_email(receiver, subject, body)
sendMore = input('Do you want to send another mail')
