# This script will encrypt all files with .pdf in its directory
# I know this script is bad so deal with it ...

import os
import base64
from cryptography.fernet import Fernet

def encrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filename, "wb") as file:
        file.write(encrypted_data)
    os.rename(filename,filename[:-4]+'.oOf')

flag = "ISS{0nLy_fUn_T1m3s_W1th_F3rn3t!}"
flag_bytes = flag.encode('ascii')
key = base64.b64encode(flag_bytes)
for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if file.endswith(".pdf"):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        print('Encrypting:',filename)
        encrypt(filename, key)

print('''              __ 
             / _|
  ___   ___ | |_ 
 / _ \ / _ \|  _|
| (_) | (_) | |  
 \___/ \___/|_|  
 
 Your PDF's are now MINE! hahaha ...''')