from cryptography.fernet import Fernet

# Get the key from the file
file = open('key.txt', 'rb')
key = file.read()
file.close()


# Decrypt the message
def decrypt_message(encrypted):
    f2 = Fernet(key)
    decrypted = f2.decrypt(encrypted)
    message = decrypted.decode()
    return message

# msg = b'gAAAAABf7fzjKZItslv9Cwm6B7XaM-33dc4h9n9T58zLR-RL6f5PRbwS3ubW-u_mJPjqt84ab_N21OLHFzasMUseRIO1L0hFmEUEr0TXQcRFPeLbPoraghI='
# print(decrypt_message(msg))