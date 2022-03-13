# Challenge

**Name:** Oracle Web Token

**Category:** crypto

**Difficulty:** Hard

**Author:** Alex Brown (ghostccamm)

**Flag:** `ISS{oR4cL3s_pR3d1Ct3d_tH15_sT4nDaReD_w0vLd_f4Il}`

**Provided Files:** [owt.py](publish/owt.py)

## Description

JSON Web Tokens (JWT) are a widely used standard for securely sharing information between two parties. However, it is insecure for sharing data where you do not want the recipient to read the data. 

Therefore, we are proposing the **Oracle Web Token** standard that uses modern military encryption for sharing JSON tokens securely. You can try it out and test the security using our demo API that stores a hidden flag inside the OWT token. If you can find a way to read the flag we will offer you a big prize!

Can you read the encrypted flag that is stored inside the OWT token that is created by the demo API?

## Solution

The name of the challenge **Oracle Web Token** strongly hints that demo API is vulnerable to a **Padding Oracle Attack**. This is further verified by checking `owt.py` that **CBC mode** is used  and the API responds with a padding error if there is invalid padding.

A **CBC padding oracle attack** uses the error message of invalid padding to discern:

1) The length of the original plaintext.
2) Retrieve the plaintext byte by byte by looking for the invalid padding errors.

It isn't in the scope of this writeup to fully explain how to exploit the vulnerability, since it is somewhat complicated. The reader is recommended to [watch this great YouTube video](https://www.youtube.com/watch?v=aH4DENMN_O4) and refer to the [solution code here](solution/exploit.py).

Exploting the padding oracle vulnerability reveals that the plaintext of the OWT token is below.

```json
{"flag": "ISS{oR4cL3s_pR3d1Ct3d_tH15_sT4nDaReD_w0vLd_f4Il}"}
```