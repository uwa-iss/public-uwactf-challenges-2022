# Challenge

**Name:** I am the Admin

**Category:** Crypto

**Difficulty:** Medium

**Author:** Alex Brown (ghostccamm)

**Flag:** `ISS{w4iT_tH3_iV_c4N_B_u53d_t0_m4nIpvL4t3_tH3_pL41nT3xT?!?!?!}`

**Provided Files:** [app.py](publish/app.py)

## Description

We are currently testing out a new cryptographic method for authentication and have started a test server for our bug bounty program. The goal of the bug bounty is to try and find a method to forge the encrypted body to say that you are the `admin` user. If you are able to do this we will give you a nice flag that will allow you to claim a prize!

*Can you manipulate the encrypted body to change the plaintext from `u=guest` to `u=admin`?*

## Solution

There are three factors with this application that enable an attacker to rewrite the plaintext into a different value.

1) CBC mode is used using AES.
2) The initial vector (IV) is provided to the user and it can be manipulated.
3) The server responds with the username that is decrypted which needs to be changed.

Looking at how CBC mode works for decryption, the first ciphertext block is decrypted using AES then **XORed with the IV**. However, XOR is a bitwise operation. For an example, if you have the following values `a = 0xaa` and `b = 0xbb` then `a ^ b = 0x11` (all values are in hex). If `a` was modified to `a=0xfa` then only the first byte is modified (`a ^ b = 0x41`).

Because of this and the three points stated above, you can modify values of the IV to try and find a different byte to put into the IV that maps to the desired character.

The first step you want to do is find a new IV byte at index 2 that will modify the plaintext from `u=guest` to `u=auest`. You can do this by testing all possible values for a byte until the application responds back that your name is `auest`. Once you have found your desired character, you incrementally modify bytes in the IV until the plaintext becomes `u=admin`.

The solution code [here](solution/sol.py) uses this method for modifying the plaintext.