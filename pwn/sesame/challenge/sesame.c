#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

void jump() {
    asm("jmp *%esp");
}

void init() {
    // Disable buffering.
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);
    setvbuf(stdout, NULL, _IONBF, 0);
}

void vuln() {
    char buf[32];

    printf("Here's a shellcode! Do you know what to do with it?\n\\x31\\xc0\\x99\\x50\\x68\\x2f\\x2f\\x73\\x68\\x68\\x2f\\x62\\x69\\x6e\\x89\\xe3\\x50\\x53\\x89\\xe1\\xb0\\x0b\\xcd\\x80\nInput: ");

    gets(buf);

    return;
}

void main() {
    init();
    vuln();

    return;
}