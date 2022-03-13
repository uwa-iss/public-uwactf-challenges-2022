# Challenge

**Name:** babyheap

**Category:** pwn

**Difficulty:** Easy  

**Author:** mowemcfc  

**Flag:** ISS{1337_h34p_h4ck3r?!?!}

## Description

Can you bypass authentication?

## Solution

This is a basic heap overflow challenge with all protections enabled.

The key to solving this challenge is understanding how the `admin` and `student` structs are allocated on the heap.

> You may want to read about [Heaps and Chunks](https://azeria-labs.com/heap-exploitation-part-2-glibc-heap-free-bins/) to further understand this, but that is not necessary.

Basically, as both `admin` and `student` structs are allocated with the same size, they will exist sequentially in heap memory in that order.

This means that if we were able to write past the boundary of the `student->username` , we could modify the values stored in `student->isadmin`.

It just so happens that this is the case.

```c
typedef struct struc {
    int isadmin;
    char name[16];
} user;

...

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
```

`scanf` will read any arbitrarily-sized amount of data passed into it. Thus, we can provide 28 bytes of junk followed by a single `1` byte, and bypass the authentication check.
