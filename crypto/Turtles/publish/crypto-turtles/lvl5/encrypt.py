from Crypto.Util.number import getPrime, bytes_to_long

nbits = 1024

p = getPrime(nbits)
q = getPrime(nbits)
n = p*q

m = bytes_to_long(b"password: ???????????????????????")
r = getPrime(nbits//(2**7))

e = 3

c1 = pow(m+0, e, n)
c2 = pow(m+r, e, n)

print(f"n: {n}")
print(f"e: {e}")
print(f"c1: {c1}")
print(f"c2: {c2}")