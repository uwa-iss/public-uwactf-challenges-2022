from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse
from random import getrandbits

m = bytes_to_long(b'password: ????????????????')
nbits = 128

def RSA():
    p = int(getPrime(1024))
    q = int(getPrime(1024))
    n = int(p*q)
    phi = int((p-1)*(q-1))
    while True:
        d = int(getPrime(256))
        e = int(inverse(d, phi))
        if e.bit_length() == n.bit_length():
            break
    return n, e, p, q

n, e, p, q = RSA()

c = pow(m, e, n)

print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")