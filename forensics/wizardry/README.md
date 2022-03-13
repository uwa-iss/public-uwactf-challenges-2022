# Challenge

**Name:** wizardry
**Category:** Forensics
**Difficulty:** Easy
**Author:** Jesse Carter (mowemcfc)
**Flag:** ISS{1t5_s1mpl3_m4g1c!}

## Description

Your friend sent you a cute baby picture, but it's corrupted!

Can you fix it?

## Solution

The key here is in noticing the file extension `.png` and where the file is corrupted.

If you are familiar with [File Signatures (Magic Bytes / Magic Numbers)](https://en.wikipedia.org/wiki/List_of_file_signatures), you would spot that the PNG does not start with the bytes `89 50 4E 47` but instead `DE AD BE EF`. Simply modifying the file with a hex editor of your choice (I used `hexedit`), should allow the file to be opened properly.
