# Challenge

**Name:** Exif

**Category:** Forensics

**Difficulty:** Easy  

**Author:** AustinNguyen  

**Flag:** ISS{M3t4d4T4_1s_1mp0rt4nt}  

## Description

Our logo image has a black flag, as you can see. It even has a hidden flag inside its data. Can you find the hidden flag?

## Solution

The challenge includes a logo image of UISS. 

The name of the challenge is the hint that suggests us to check for the EXIF data of the image.  

Run the ```exiftool``` command on the image as

    exiftool logo.png

to view metadata of the image

And the flag should be seen.

