# Challenge

**Name:** outside

**Category:** pwn

**Difficulty:** Medium  

**Author:** mowemcfc  

**Flag:** ISS{5up3r_574ck_fr4m35}  

## Description

We've included a stack canary on our `hello` function, surely hackers can't shell us now!

## Solution

The return address of the `welcome` function is checked. If it has been changed, the binary aborts.

```c
if (__builtin_return_address(0) != RETADDR) { // Compare return address (after read) to the saved one. 
    abort();
}
```

```shell
> readelf -s challenge/outside | grep win
    36: 0000000000401196    23 FUNC    GLOBAL DEFAULT   15 win
```

To circumvent this during a buffer overflow, the original return address, which is static due to the binary being non-PIE (Position Independent Executable), is placed as-is in the correct place.

We can then control RIP of the stack frame **above** that of `welcome`, which is `main`, and return to `win`.

A slight caveat is that we first jump to a `RET` instruction before jumping to `win` in order to avoid an Ubuntu-specific SEGFAULT issues.
