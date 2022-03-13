from Crypto.Util.number import getPrime, bytes_to_long, long_to_bytes

flag = b"ISS{?????????????????????????}"
text = b"The first rule of UISS: no non tech memes in the memes channel"
def efficientPrimes(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    i = getPrime(bits)
    n1 = p*i
    n2 = i*q
    return(n1,n2)
e = 65537
bits = 2048
n1,n2 = efficientPrimes(bits)
m1 = bytes_to_long(text)
m2 = bytes_to_long(flag)
c1 = pow(m1, e, n1)
c2 = pow(m2, e, n2)
print(f"n1 = {n1}")
print(f"n2 = {n2}")
print(f"e = {e}")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
