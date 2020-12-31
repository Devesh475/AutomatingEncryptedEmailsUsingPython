from cryptography.fernet import Fernet

# encryption code
# Get the key from the file
file = open('key.txt', 'rb')
key = file.read()
file.close()


# Encrypt the message
def encrypt_message(message):
    encoded = message.encode()
    f = Fernet(key)
    encrypted = f.encrypt(encoded)
    return encrypted


msg = 'this is my text message'
cipher = encrypt_message(msg)
print(cipher)

