#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define LICENSE_KEY_SIZE 27
#define LICENSE_PARTS_SIZE 5

void xor(char *input, char *key, char *result, int len) {
    for (int i=0; i < len; i++) {
        result[i] = input[i] ^ key[i];
    }
}

void get_license_key(char *buf, int len) {
    fread(buf, sizeof(char), len, stdin);
    buf[len] = '\0';
}

int validate_format(char *license_key, int license_key_size, char **parts, int total_parts) {
    char *part_ptr;
    parts[0] = license_key;

    for(int i=1; i < total_parts; i++) {
        part_ptr = strchr(parts[i-1]+1, '-')+1;
        parts[i] = part_ptr;
    }

    // One more since there is no '-' at the start of the license key
    if (parts[1] - parts[0] != 5) {
        return 1;
    }

    if (parts[2] - parts[1] != 6) {
        return 1;
    }

    if (parts[4] - parts[3] != 6) {
        return 1;
    }

    return parts[0] + LICENSE_KEY_SIZE - parts[4] != 4;
}

int validate_part_a(char *part_a) {
    char c;
    int mult_total = 1;
    int sum_total = 0;
    for (int i=0; i < 3; i++) {
        c = part_a[i];
        if (c < 'A' || c > 'Z') {
            return 1;
        }
        mult_total *= c;
        sum_total += c;
    }

    sum_total += part_a[3];

    if (mult_total != 389017) {
        return 1;
    }

    return sum_total != 273;
}

int validate_part_b(char *part_b) {
    char c;
    char prev_c = part_b[0];
    if (prev_c != 'J') {
        return 1;
    }

    for (int i=1; i < 4; i++) {
        c = part_b[i];
        if (c < 'A' || c > 'Z') {
            return 1;
        }

        if (c != prev_c + 2) {
            return 1;
        }
        prev_c = c;
    }

    c = part_b[4];
    return c != '9';
}

int validate_part_c(char *part_c) {
    unsigned long long c;
    unsigned long long x = 0;
    for (int i=0; i < 4; i++) {
        c = part_c[i];
        if (c < 'A' || c > 'Z') {
            return 1;
        }
        x |= c << i*8;
    }

    c = part_c[4];
    x |= c << 32;
    return x != 224752783193ULL;
}

int validate_part_d(char *part_d) {
    char result[5];
    char *key = "\x1c\x0a\x12\x77\x7b";
    xor(part_d, key, result, 5);
    return strncmp(result, "KEEEK", 5);
}

int validate_part_e(char *license_key, int key_size, char *part_e) {
    int e = atoi(part_e);
    int sum_key = 0;

    for (int i=0; i< key_size; i++) {
        sum_key += license_key[i];
    }

    sum_key -= 215;
    return e != sum_key;
}

void banner() {
    printf("\n\033[0;34m=--------------------------------------------------------------------=\n\n");
    printf("\033[1;32m     0000             0000        7777777777777777/========___________\n");
    printf("\033[1;32m   00000000         00000000      7777^^^^^^^7777/ || ||   ___________\n");
    printf("\033[1;32m  000    000       000    000     777       7777/=========//\n");
    printf("\033[1;32m 000      000     000      000             7777// ((     //\n");
    printf("\033[1;32m0000      0000   0000      0000           7777//   \\   //\n");
    printf("\033[1;32m0000      0000   0000      0000          7777//========//\n");
    printf("\033[1;32m0000      0000   0000      0000         7777\n");
    printf("\033[1;32m0000      0000   0000      0000        7777\n");
    printf("\033[1;32m 000      000     000      000        7777\n");
    printf("\033[1;32m  000    000       000    000       77777\n");
    printf("\033[1;32m   00000000         00000000       7777777\n");
    printf("\033[1;32m     0000             0000        777777777\n");
    printf("\n\033[0;34m=--------------------------------------------------------------------=\033[0m\n\n");
    printf("\033[0;36m      Welcome to \033[1;35mAgent 007's\033[1;31m License to Kill\033[0;36m validation program!\n");
    printf("\033[0;36m     If you are \033[1;35m007\033[0;36m then input your license key to verify you are\n");
    printf("\033[1;31m                           LICENSED TO KILL\n");
    printf("\n\033[0;34m=--------------------------------------------------------------------=\033[0m\n\n");
}

int main() {
    banner();
    char *flag_enc = "\x00\x1a\x1a\x4d\x62\x05\x7b\x11\x3c\x08\x6e\x6a\x21\x7a\x31\x70\x72\x66\x7c\x64\x59\x55\x69\x10\x12\x12\x4a";
    char license_key[LICENSE_KEY_SIZE+1];
    char *license_parts[LICENSE_PARTS_SIZE];
    printf("\033[1;32mLicense Key: ");
    get_license_key(license_key, LICENSE_KEY_SIZE);
    printf("\033[0m\n");
    if (validate_format(license_key, LICENSE_KEY_SIZE, license_parts, LICENSE_PARTS_SIZE)) {
        printf("\033[1;31mINVALID LICENSE!\033[0m\n");
        exit(1);
    }

    if (validate_part_a(license_parts[0])) {
        printf("\033[1;31mYOU ARE NOT LICENSED TO KILL!\033[0m\n");
        exit(1);
    }

    if (validate_part_b(license_parts[1])) {
        printf("\033[1;31mYOU ARE NOT LICENSED TO KILL!\033[0m\n");
        exit(1);
    }

    if (validate_part_c(license_parts[2])) {
        printf("\033[1;31mYOU ARE NOT LICENSED TO KILL!\033[0m\n");
        exit(1);
    }

    if (validate_part_d(license_parts[3])) {
        printf("\033[1;31mYOU ARE NOT LICENSED TO KILL!\033[0m\n");
        exit(1);
    }

    if (validate_part_e(license_key, LICENSE_KEY_SIZE-4, license_parts[4])) {
        printf("\033[1;31mYOU ARE NOT LICENSED TO KILL!\033[0m\n");
        exit(1);
    }

    char flag[LICENSE_KEY_SIZE+1];
    xor(flag_enc, license_key, flag, LICENSE_KEY_SIZE+1);
    printf("\033[1;32mYOU ARE LICENSED TO KILL 007!\n");
    printf("\033[0;34mFlag: \033[1;35m%s\n", flag);
}