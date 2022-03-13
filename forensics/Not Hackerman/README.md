# Challenge

**Name:** Not Hackerman  
**Category:** Forensics  
**Difficulty:** Easy  
**Author:** Chris Fitzsimons (Fitzy)  
**Flag:** ISS{W0W_F1l3S_cAn_b3_H1dD3n}  

## Description

Hidden in plain sight, Not a Hackerman. Right? I thought I found something, but the Hackerman is **hiding** so many secrets!  
There is just something I am not seeing...  

## Solution

Steghide has been used to imbed a txt file into an image.  
The password used with steghide edited into the corner of the image "fsociety".  
Find the password in the corner of the image (or guess it) and use steghide to extract the hidden message.  

steghide extract -p fsociety -sf NotHackerman.jpg  
