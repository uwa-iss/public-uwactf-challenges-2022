# Challenge

**Name:** Substitutions

**Category:** Crypto  

**Difficulty:** Easy  

**Author:** AustinNguyen  

**Flag:** ISS{CLASSIC_CIPHERS_ARE_NOT_SAFE}

**Provided Files:** [crypto_substitutions.zip](publish/crypto_substitutions.zip)

## Description

ROT13 is not the only substitution ciphers. Let's try some of the others.

## Solution

### Encryption process

The first round of encryption use Caesar Cipher to encrypt the message with the key is the length of our given key - which is 11.  
So we do ROT11 here - shift letter to the right.  
For example, for the string **ISS**, doing encryption results in ciphertext **TDD**

The second encryption uses Vigenre Cipher with the input is the ciphertext from the first round and our key.   
Vingrere cipher also shifts the letter in the original message as Caesar but different for each letter depending on the key we use.  
With the given key **SUPERSECRET** and the text **TDD**, we shift each letter of the text with the value of the corresponding letter in the key to retrieve the ciphertext, i.e. T with S, D with U, L with P and so on.  
The output ciphertext is **LXS**

The final ciphertext after two rounds of encryption is written to the outfile in hex format.

### Decryption process

We first decode the output text from hex to string format and do two rounds of ciphers as in the encryption process.  
For the first round, we decrypt the ciphertext using Vigenere Cipher with the same process as the encryption but shift the letter to the left this time.  
Then, we decrypt the output text from the first round using Caesar Cipher and retrieve the flag
The solution code can be found in the solution directory.
