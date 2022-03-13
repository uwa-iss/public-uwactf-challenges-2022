from Crypto.Util.number import getPrime, bytes_to_long

nbits = 512

m = bytes_to_long(b"password: ????????????????")

e = 65537
n = getPrime(nbits)

c = pow(m, e, n)

print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")