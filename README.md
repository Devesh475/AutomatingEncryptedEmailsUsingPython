# AutomatingEncryptedEmailsUsingPython
This is a python script used to send emails using voice commands which are encrypted by Advanced Encryption Standard algorithm.

Steps to use the scripts :

Redefine the dictionary of contacts you want to send mails.

Put your email in place of sender email.

Run the script.

Packages required to run the script :

1.speech_recognition 2.pyttsx3 3.smtplib

Encryption.py file is used to create your unique key using a password that is unique for that password.

EncryptMessage.py is the file which has defined functions to encrypt and decrypt the string using the functions encrypt_message() and decrypt_message()

Once the email has been sent the reciever can run the script Decryption.py to decrypt the message by copying the encrypted message and passing it to the called function.

Note : This script can only send emails to gmail accounts.

Note : You need to allow less secure apps for sending the mail using smtp.

Note : The reciever should have the same key to decode the message.
