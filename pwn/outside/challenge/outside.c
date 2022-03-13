#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void* RETADDR;

void win() {
    system("/bin/sh");
}

void welcome() {
    int idx;
    char buf[64];

    RETADDR = __builtin_return_address(0); // Save return address before reading into buffer
    gets(buf);
    idx = strcspn(buf, "\r\n");
    buf[idx] = '\0';
    
    if (__builtin_return_address(0) != RETADDR) { // Compare return address (after read) to the saved one. 
        abort();
    }
    return;
}

void main() {
    welcome();
    return;
}