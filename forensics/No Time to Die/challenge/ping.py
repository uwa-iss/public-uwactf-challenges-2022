import os
import random
import time

ip = '45.155.204.161'
ips = ['1.1.1.1','1.0.0.1','8.8.8.8','8.8.4.4','9.9.9.9','149.112.112.112','185.228.168.9','185.228.169.9','76.76.19.19','76.223.122.150','45.155.204.161']
domains = ['google.com','uwa.edu.au','hoyts.com','007.com','microsoft.com','www.w3schools.com','www.cloudns.net','youtube.com','amazon.com','lttstore.com','gchq.github.io','pastebin.com']
urls = ['http://www.google.com/search?q=flag.txt','http://www.google.com/search?q=ISS%7B+Flags','http://gchq.github.io/CyberChef/','http://medium.com/@LindaVivah/learn-how-to-read-binary-in-5-minutes-dac1feb991e','http://www.youtube.com/watch?v=BIhNsAtPbPI','http://www.youtube.com/watch?v=BboMpayJomw','http://pastebin.com/']
binary = "01001001010100110101001101111011010011100011000001011111011101000011000101001101001100110101111101010100001100000101111101101100001100010101011000110011010111110110110101010010010111110100001000110000011011100100010001111101"

for x in range(len(binary)):
    if random.random() >= 0.5:
        domain = random.randint(0,11)
        domain = domains[domain]
        os.system('nslookup {}'.format(domain))
    elif random.random() >= 0.7:
        domain = random.randint(0,11)
        domain = domains[domain]
        os.system('curl https://{}'.format(domain))
    elif random.random() >= 0.5:
        url = random.randint(0,6)
        url = urls[url]
        os.system('curl {}'.format(url))
    if random.random() >= 0.5:
        rndip = random.randint(0,10)
        ipAddr = ips[rndip]
        os.system('ping -n 1 {}'.format(ipAddr))
    elif random.random() >= 0.7:
        rndip = random.randint(0,10)
        ipAddr = ips[rndip]
        os.system('curl ftp://{}'.format(ipAddr))
    elif random.random() >= 0.7:
        rndip = random.randint(0,10)
        ipAddr = ips[rndip]
        os.system('ssh {}'.format(ipAddr))
    if binary[x] == "0":
        ttl = "68"
    else:
        ttl = "69"
    os.system('ping -n 1 -i {} {}'.format(ttl,ip))
    time.sleep(1)