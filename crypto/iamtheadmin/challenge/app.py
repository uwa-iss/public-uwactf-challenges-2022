#!/usr/bin/env python3
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import binascii

# You will need to create a seperate flag.py file with a temporary FLAG constant.
# Example
# flag.py
# ```
# FLAG=FAKE{flag_for_testing}
# ```
from flag import FLAG

BLOCKSIZE = 16

def generate_body(key: bytes) -> dict:
    """
        Generate the encrypted body to give to users
    """
    pt = 'u=guest'
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv = iv)
    ct_hex = cipher.encrypt(pad(pt.encode(), block_size=BLOCKSIZE)).hex()

    return {"iv_hex" : iv.hex(), "ct_hex" : ct_hex}

def check_body(ct_hex: str, iv_hex: str, key: bytes) -> str:
    try:
        cipher = AES.new(key, AES.MODE_CBC, iv = binascii.unhexlify(iv_hex))
        pt_padded = cipher.decrypt(binascii.unhexlify(ct_hex))
        pt = unpad(pt_padded, block_size=BLOCKSIZE).decode()
    except Exception:
        return """
Welcome guest!
Unfortunately you are NOT the admin so no flag for you!
    """

    if pt == "u=admin":
        return """
🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳
🥳          Welcome Admin!        🥳
🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳🎉🥳

FLAG: {flag}
        """.format(flag = FLAG)
    name = pt[2:]
    return """
Welcome {name}!
Unfortunately you are NOT the admin so no flag for you!
    """.format(name = name)

def loop(key: bytes):
    while True:
        print("YOUR INITIAL VECTOR: ", end="")
        user_iv_hex = input()
        print("YOU ENCRYPTED BODY: ", end="")
        user_ct_hex = input()

        print(check_body(user_ct_hex, user_iv_hex, key))

        print("Continue? Y/N: ", end="")
        c = input()
        if not c == 'Y':
            break

def main():
    key = get_random_bytes(BLOCKSIZE)
    gen_iv_ct = generate_body(key)
    iv_hex = gen_iv_ct['iv_hex']
    ct_hex = gen_iv_ct['ct_hex']

    print("""
💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻
💻    Welcome to our Bug Bounty!  💻
💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻💻
    """)

    print("Here is some encrypted text for you!", end="\n\n")
    print("INTIAL VECTOR:", iv_hex)
    print("ENCRYPTED BODY:", ct_hex)
    
    print("""
Try modifying the encrypted text we gave you
and see if you can login as the admin!
    """)

    loop(key)

if __name__ == "__main__":
    main()
