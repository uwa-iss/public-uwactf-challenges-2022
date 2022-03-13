from Crypto.Util.number import getPrime, bytes_to_long

nbits = 2048

e = 19

m = bytes_to_long(b"password: ????????????????")

p = getPrime(nbits)
q = getPrime(nbits)

n = p*q

assert p != q

c = pow(m, e, n)

print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")