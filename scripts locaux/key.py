import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

# Method to create a key using a password
password = "bigdataproject"  # This is input in the form of a string
password = password.encode()  # Convert to type bytes
# Obtained using a key from os.urandom(16) (type bytes)
salt = b'd=I\xee\t\x9e2\xc08)\x9e\x9f\x9f$\xff\x1f'
kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
    backend=default_backend()
)
key = base64.urlsafe_b64encode(kdf.derive(password)) 
file = open('key.key', 'wb')  # Open the file as wb to write bytes
file.write(key)  # The key is type bytes still
file.close()