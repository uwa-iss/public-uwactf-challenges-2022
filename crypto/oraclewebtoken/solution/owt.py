from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from base64 import urlsafe_b64encode, urlsafe_b64decode

import json, os

class OWTException(Exception):

    def __init__(self, message):
        super().__init__(message)

def base64_decode(e: bytes) -> bytes:
    miss_pad = len(e) % 4
    e = e + b'='*(4-miss_pad)
    d = urlsafe_b64decode(e)
    return d

def base64_encode(d: bytes) -> bytes:
    e = urlsafe_b64encode(d)
    e = e.strip(b'=')
    return e

def create_token(data_dict: dict, key: bytes, block_size = 32) -> str:
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)

    try:
        pt = json.dumps(data_dict).encode('utf-8')
    except Exception:
        raise OWTException("Error parsing input data")

    ct = base64_encode(cipher.encrypt(pad(pt, block_size, style='pkcs7'))).decode('utf-8')
    header = base64_encode(json.dumps({"iv":base64_encode(iv).decode('utf-8')}).encode('utf-8')).decode('utf-8')
    return '{header}.{body}'.format(header = header, body = ct)

def decrypt_token(token: str, key: bytes, block_size = 32) -> str:
    try:
        token_lst = token.split('.')
        header = json.loads(base64_decode(token_lst[0].encode('utf-8')).decode('utf-8'))
        body = base64_decode(token_lst[1].encode('utf-8'))
        iv = base64_decode(header['iv'].encode('utf-8'))
    except Exception:
        raise OWTException("Malformed OWT!")

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    try:
        pt_padded = cipher.decrypt(body)
    except Exception:
        raise OWTException("Could not decrypt the body!")

    try:
        pt = unpad(pt_padded, block_size, style='pkcs7')
    except Exception:
        raise OWTException("Invalid padding!")

    try:
        return json.loads(pt)
    except Exception:
        raise OWTException("Could not parse body as a JSON!")
