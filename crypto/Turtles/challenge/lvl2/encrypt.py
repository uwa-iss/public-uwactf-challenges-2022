from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes, inverse
from math import gcd

nbits = 1024

p = getPrime(nbits)
q = getPrime(nbits)
n = p*q

e1 = getPrime(nbits//(2**7))
e2 = getPrime(nbits//(2**7))

m = bytes_to_long(b"password: ????????????????")

c1 = pow(m, e1, n)
c2 = pow(m, e2, n)

print(f"n: {n}")
print(f"e1: {e1}")
print(f"e2: {e2}")
print(f"c1: {c1}")
print(f"c2: {c2}")