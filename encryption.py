import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# create your own password to generate your own unique key
password_provided = "MyPasswordForProtecting"
password = password_provided.encode()  # convert to bytes

salt = b'\xea \x91oT\xc5\xdf\xcc\xb2\xe16\xe9\xba\xeaY\x16'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password))

file = open('Key.txt', 'w')
file.write(str(key.decode('utf-8')))
file.close()
