from flag import flag
from key import KEY

def caesar_enc(p,k):
    cipher = ""
    for i in range(len(p)):
        if p[i].isalpha():
            cipher += chr(((ord(p[i]) - 65 + len(k)) % 26) + 65)
        else:
            cipher += p[i]
    return cipher 

def vigenere_enc(p,k):
    cipher = ""
    for i in range(len(p)):
        if p[i].isalpha():
            cipher += chr((ord(p[i]) - 65 + ord(k[i % len(k)]) - 65) % 26 + 65) 
        else:
            cipher += p[i]
    return cipher

def main():
    cipher = caesar_enc(flag, KEY)
    cipher = vigenere_enc(cipher, KEY)

    f = open('out.txt', 'w')
    f.write(cipher.encode().hex())
    f.close()

if __name__ == '__main__':
    main()
