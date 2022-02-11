import cryptography
from cryptography.fernet import Fernet, InvalidToken
import os

def decrypt(file):
    # Open the file as wb to read bytes
    # The key will be type bytes
    keyfile = open('key.key', 'rb')  
    key = keyfile.read()  
    keyfile.close()

    #Reading encrypted file
    with open(file,'rb') as f:
        dataToDecrypt = f.read()

    # Decryption of the file
    fernet = Fernet(key)
    try:
        decrypted = fernet.decrypt(dataToDecrypt) 
        #Writing decrypted file
        with open('decrypted.decrypted','wb') as f:
            f.write(decrypted)

    except InvalidToken as e:
        print("Invalid Key - Unsuccessfully decrypted")