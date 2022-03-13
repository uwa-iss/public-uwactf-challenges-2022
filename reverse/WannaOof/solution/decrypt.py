import os
import base64
from cryptography.fernet import Fernet

def decrypt(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        file_data = file.read()
    decrypted_data = f.decrypt(file_data)
    with open(filename, "wb") as file:
        file.write(decrypted_data)
    os.rename(filename,filename[:-4]+'.pdf')

flag = "ISS{0nLy_fUn_T1m3s_W1th_F3rn3t!}"
flag_bytes = flag.encode('ascii')
key = base64.b64encode(flag_bytes)
for file in os.listdir(os.path.dirname(os.path.abspath(__file__))):
    if file.endswith(".oOf"):
        filename = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        decrypt(filename, key)