# Challenge

**Name:** Positional

**Category:** Crypto

**Difficulty:** Easy  

**Author:** AustinNguyen  

**Flag:** ISS{positionalstego}

**Provided Files:** [crypto_positional.zip](publish/crypto_positional.zip)

## Description

As a new hire in the ASIO, you have been positioned in the postal unit that reads private letters being sent. A recent internal report has highlighted the need to snoop posted letters since criminal organisations have been moving back to **archaic methods** of communication.

You come across a weird letter where two slips of paper fell out. One appeared to be a weird message about information security and the other just had a bunch of numbers on it. 

Could this be some **old** method for hiding a secret message?

## Solution

Every two characters in the key are a single number that can be used to find the character in the subsequent line of the message.  
For example, the first two character in the key "01". We look for the first character in the first line of the message   
The second two character in the key "01" subsequently map to the character in 1st position in the second line.  
Doing the same process for the rest of the message and obtaining the flag