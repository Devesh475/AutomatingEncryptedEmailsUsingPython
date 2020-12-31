import pyttsx3
import smtplib
import speech_recognition as sr
from encryptMessage import encode_message
from email.message import EmailMessage

listner = sr.Recognizer()



def get_info():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listner.listen(source)
            info = listner.recognize_google(voice)
            return info.lower()
    except:
        pass


engine = pyttsx3.init()

def talk(text):
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[1].id)
    engine.setProperty('rate',150)
    engine.say(text)
    engine.runAndWait()

emailList = {'name1':'example1@gmail.com',
             'name2':'example4@gmail.com',
             'name3':'example3@gmail.com',
             'name4':'example4@gmail.com'}

def send_email(receiver,subject,body):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls()
    server.login('sender@gmail.com','password')
    email = EmailMessage()
    email['From'] = 'sender@gmail.com'
    email['To'] = receiver
    email['Subject'] = encode_message(subject)
    body = encode_message(body)
    email.set_content(body)
    server.send_message(email)

def get_email_info():
    talk('To whom you want to send the mail')
    name = get_info()
    receiver = emailList[name]
    print(receiver)
    talk('what do you want the subject to be')
    subject = get_info()
    print(subject)
    talk('please tell the content of the mail')
    body = get_info()
    print(body)
    send_email(receiver,subject,body)
    talk('Do you want to send another mail')
    ans = get_info()
    if ans == 'yes' or ans == 'yeah':
        get_email_info()

get_email_info()

