#!/usr/bin/env python3

from PIL import Image
from stegano import lsb
import sys
 
def save_image(image):
    image.save("2.png","PNG")

def encode_image(image,msg):
    temp = lsb.hide(image, msg)
    save_image(temp)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: " + sys.argv[0] + "[filename] [message]")
        exit()
    
    try:
        image = Image.open(sys.argv[1])
    except:
        print("Unable to open file")
        exit()

    encode_image(image,sys.argv[2])
