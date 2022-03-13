#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void target()
{
    system("/bin/bash");
}

void handler() {
    printf("Timeout.\n");
    exit(1);
}

void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
    signal(SIGALRM, handler);
    alarm(30);
}

typedef struct struc {
    int isadmin;
    char name[16];
} user;

int main(int argc, char **argv)
{
    setup();
    
    user *admin, *student;
    char buffer[64];

    printf("\n");

    admin = malloc(sizeof(user));
    student = malloc(sizeof(user));
    
    admin->isadmin = 1;
    student->isadmin = 0;

    printf("Enter the name of the admin: ");
    scanf("%s", buffer);
    strcpy(admin->name, buffer);
     
    printf("Enter the name of the user: ");
    scanf("%s", buffer);
    strcpy(student->name, buffer);

    if (student->isadmin == 1) {
        printf("Welcome, admin.\n");
        target();
    } else {
        printf("Welcome, and goodbye, student. \n");
    }

    return 0;
}
