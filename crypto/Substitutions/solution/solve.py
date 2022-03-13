out = open('../challenge/out.txt','r').read()
KEY = 'SUPERSECRET'

def caesar_dec(ct,k):
    pt = ""
    for i in range(len(ct)):
        if ct[i].isalpha():
            pt += chr(((ord(ct[i]) - 65 - len(k)) % 26) + 65)
        else:
            pt += ct[i]
    return pt 

def vigenere_dec(ct, k):
    pt = ""
    for i in range(len(ct)):

        if ct[i].isalpha():
            pt += chr( ((ord(ct[i]) - 65) - (ord(k[i % len(k)]) - 65)) % 26 + 65)
        else:
            pt += ct[i]
    return pt

ct = bytes.fromhex(out).decode()

# print(ct)
pt = vigenere_dec(ct,KEY)

# print(pt)

flag = caesar_dec(pt, KEY)
print(flag)