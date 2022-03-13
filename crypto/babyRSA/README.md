# Challenge

**Name:** babyRSA

**Category:** Crypto

**Difficulty:** Easy

**Author:** q3st1on

**Flag:** `ISS{th3_i_st4nds_f0r_ins3cur3}`

**Provided Files:** [crypto-babyRSA.zip](publish/crypto-babyRSA.zip)  

## Description

Generating big primes is hard, so I made it quicker.
Why make 2 for each message, when you can make less??

## Solution

Because `n1` and `n2` share the factor `i`, you can factorize them
using the math library's `gcd()` function. Then divide `n1` and `n2`
by the result to find the remaining primes `p` and `q`.

```
i = gcd(n1, n2)
p = n1//i
q = n2//i
```
from there it is just standard RSA decryption as shown in the [solve script](solution/solve.py).