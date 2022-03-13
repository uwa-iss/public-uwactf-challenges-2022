#include <stdio.h>
#include <stdlib.h>

unsigned long target;

unsigned long read_num(void) {
    char buf[32];
    unsigned long ret;
    read(0,buf,31);
    ret = strtoul(buf, 0, 0);

    return ret;
}

int main(void)
{
    char* notes[4];
    uint notecount = 0;
    int option;

    long max_alloc;

    unsigned long note_size;
    char* note_ptr;


    setvbuf(stdout, 0, 2, 0);
    puts("\n=============");
    puts("Hi, and welcome to my house!");
    printf("A gift for you: %p\n", puts);
    note_ptr = malloc(140);
    printf("And another: %p\n", note_ptr + 0x10);
    puts("Feel free to leave a note if you enjoyed your stay!");
    free(note_ptr);
    puts("=============\n");


    puts("1. View notes");
    puts("2. Add note");
    puts("3. Exit\n");

    while(1) {
        printf("> ");
        option = read_num();

        if (option == 2) {
            if (notecount < 4) {
                printf("Size: ");
                note_size = read_num();
                note_ptr = (char*)malloc(note_size);
                notes[notecount] = note_ptr;

                printf("Message: ");
                max_alloc = malloc_usable_size(notes[notecount]);
                read(0, notes[notecount], max_alloc+8);

                notecount++;
                puts("\nNote added!");
            } else {
                puts("Too many notes! Exiting");
                abort();
            }
        } else if (option == 1) {
            for(int i = 0; i < notecount; i++) {
                printf("Note %d:\n", i);
                printf("%s\n", notes[i]);
            }
        } else if (option == 3) {
            puts("Bye!");
            exit(0);
        }
    }

}