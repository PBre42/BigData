import cryptography
from cryptography.fernet import Fernet, InvalidToken
import os

def encrypt(file):
    # We are using symetric cyptography
    # So we have to store the key in a file
    # Open the file as wb to read bytes
    # The key will be type bytes
    keyfile = open('key.key', 'rb')  
    key = keyfile.read()  
    keyfile.close()

    #Reading file to encrypt
    with open(file,'rb')as f:
        dataToEncrypt = f.read()

    # Encryption of the file using Fernet class
    # An implementation of AES

    fernet = Fernet(key)
    encrypted = fernet.encrypt(dataToEncrypt)

    # Writing the file
    with open('data.encrypted','wb') as f:
        f.write(encrypted)
