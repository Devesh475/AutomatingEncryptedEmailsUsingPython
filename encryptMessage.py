from cryptography.fernet import Fernet

# encryption code
# Get the key from the file
file = open('key.txt', 'rb')
keyforEncryption = file.read()
file.close()


# Encrypt the message
def encode_message(message):
    encoded = message.encode()
    f = Fernet(keyforEncryption)
    encrypted = f.encrypt(encoded)
    return encrypted


# decryption code
# Get the key from the file
file = open('key.txt', 'rb')
keyforDecryption = file.read()
file.close()


# Decrypt the message
def decrypt_message(encrypted):
    f2 = Fernet(keyforDecryption)
    decrypted = f2.decrypt(encrypted)
    message = decrypted.decode()
    return message


msg = 'this is my text message'
cipher = encode_message(msg)
print(cipher)
print(decrypt_message(cipher))
