**Name:** Licensed to Kill

**Category:** Reverse Engineering

**Difficulty:** Medium

**Author:** Alex Brown (ghostccamm)

**Flag:** `ISS{OO7_l1C3n5eD_133keD!!!}`

**Provided:** [licensedtokill](provided/licensedtokill)

## Description

We were able to receive a leaked version of **007's License to Kill Verification Software** from the recent MI6 data breach.

Could you reverse engineer 007's **license to kill key** and retrieve the flag from the verification software?

## Solution

First let's load `licensedtokill` in `ghidra` and analyse it. Below is the main function below.

```c
undefined8 main(void)

{
  int iVar1;
  long in_FS_OFFSET;
  undefined8 local_88;
  undefined8 local_80;
  undefined8 local_78;
  undefined8 local_70;
  undefined8 local_68;
  undefined local_58 [32];
  undefined local_38 [40];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  banner();
  printf("\x1b[1;32mLicense Key: ");
  get_license_key(local_58,0x1b);
  puts("\x1b[0m");
  iVar1 = validate_format(local_58,0x1b,&local_88,5);
  if (iVar1 != 0) {
    puts("\x1b[1;31mINVALID LICENSE!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  iVar1 = validate_part_a(local_88);
  if (iVar1 != 0) {
    puts("\x1b[1;31mYOU ARE NOT LICENSED TO KILL!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  iVar1 = validate_part_b(local_80);
  if (iVar1 != 0) {
    puts("\x1b[1;31mYOU ARE NOT LICENSED TO KILL!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  iVar1 = validate_part_c(local_78);
  if (iVar1 != 0) {
    puts("\x1b[1;31mYOU ARE NOT LICENSED TO KILL!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  iVar1 = validate_part_d(local_70);
  if (iVar1 != 0) {
    puts("\x1b[1;31mYOU ARE NOT LICENSED TO KILL!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  iVar1 = validate_part_e(local_58,0x17,local_68);
  if (iVar1 != 0) {
    puts("\x1b[1;31mYOU ARE NOT LICENSED TO KILL!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
  }
  xor(&DAT_001024bb,local_58,local_38,0x1c);
  puts("\x1b[1;32mYOU ARE LICENSED TO KILL 007!");
  printf("\x1b[0;34mFlag: \x1b[1;35m%s\n",local_38);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

There a several functions that check that the license key is valid and it is 007's.

*validation functions*
```c
validate_format(local_58,0x1b,&local_88,5)
validate_part_a(local_88)
validate_part_b(local_80)
validate_part_c(local_78)
validate_part_d(local_70)
validate_part_e(local_58,0x17,local_68)
```

If the key is valid, then the license key is xored with data compiled into the program to get the flag.

```c
xor(&DAT_001024bb,local_58,local_38,0x1c);
puts("\x1b[1;32mYOU ARE LICENSED TO KILL 007!");
printf("\x1b[0;34mFlag: \x1b[1;35m%s\n",local_38);
```

The data at the address `&DAT_001024bb` is below, which is probably the flag encrypted using XOR with the license key.

```
\x00\x1a\x1a\x4d\x62\x05\x7b\x11\x37\x09\x59\x06\x3b\x7b\x24\x64\x1e\x13\x10\x3f\x06\x42\x69\x10\x12\x12\x4a\x00
```

Next let's analyse when the license key is read from STDIN. Below is the code in `main` where the license key is read using `get_license_key`.

```c
printf("\x1b[1;32mLicense Key: ");
get_license_key(local_58,0x1b);
```

```c
void get_license_key(void *param_1,int param_2)

{
  fread(param_1,1,(long)param_2,stdin);
  *(undefined *)((long)param_1 + (long)param_2) = 0;
  return;
}
```

This means that `local_58` stores the license key that we provide.

The process of reverse engineering the license key is to reverse engineer each validation function step by step.

**validate_format analysis**

In `main`

```c
iVar1 = validate_format(local_58,0x1b,&local_88,5);
if (iVar1 != 0) {
    puts("\x1b[1;31mINVALID LICENSE!\x1b[0m");
                    /* WARNING: Subroutine does not return */
    exit(1);
}
```

We can see that `validate_format(local_58,0x1b,&local_88,5)` takes in the license key (`local_58`), the length of the license key `0x1b == 27`, the address of `local_88` and the integer `5`.

Below is the decompiled code for `validate_format`.

```c
bool validate_format(long param_1,undefined8 param_2,long *param_3,int param_4)

{
  char *pcVar1;
  bool bVar2;
  int local_14;
  
  *param_3 = param_1;
  for (local_14 = 1; local_14 < param_4; local_14 = local_14 + 1) {
    pcVar1 = strchr((char *)(param_3[(long)local_14 + -1] + 1),0x2d);
    param_3[local_14] = (long)(pcVar1 + 1);
  }
  if (param_3[1] - *param_3 == 5) {
    if (param_3[2] - param_3[1] == 6) {
      if (param_3[4] - param_3[3] == 6) {
        bVar2 = (*param_3 + 0x1b) - param_3[4] != 4;
      }
      else {
        bVar2 = true;
      }
    }
    else {
      bVar2 = true;
    }
  }
  else {
    bVar2 = true;
  }
  return bVar2;
}
```

Firstly, we can see that the value at the the address `param3` (`local_88` from `main`) is set to the start of the license key (`param_1`). Secondly, we can see there is a `for` loop that loops 5 times (`param_4 == 5` from `main`) where `strchr` is called and sets a value in `param_3`.

Reading the documentation for `strchr`, it returns a pointer to the location of the first occurence of a character. In this case the character is `-` (`0x2d` in hex).

However, `param_3[local_14] = (long)(pcVar1 + 1);` stores the address after the `-` character.

Putting it all together, there are 5 parts of the license key that are seperated by `-` characters.

The next part of the code checks if each of the parts that, where the pointers are stored in `param_3` are of a specific length. It is important to note that the `-` would be included in this comparison except for the last part.

Finally, this means that the license key is of the format.

```
AAAA-BBBBB-CCCCC-DDDDD-EEEE
```

We can then verify is this is a valid format since the program prints if it isn't.

```
$ ./licensedtokill

...

=--------------------------------------------------------------------=

      Welcome to Agent 007's License to Kill validation program!
     If you are 007 then input your license key to verify you are
                           LICENSED TO KILL

=--------------------------------------------------------------------=

License Key: AAAA-BBBBB-CCCCC-DDDDD-EEEE

YOU ARE NOT LICENSED TO KILL!
```

Now we just need to reverse engineer the functions validating the 5 parts of the license key.

**validate_part_a**

Below is the decompiled code for `validate_part_a`

```c
bool validate_part_a(long param_1)

{
  char cVar1;
  int local_14;
  int local_10;
  int local_c;
  
  local_14 = 1;
  local_10 = 0;
  local_c = 0;
  while( true ) {
    if (2 < local_c) {
      return local_14 != 0x5ef99 || local_10 + *(char *)(param_1 + 3) != 0x111;
    }
    cVar1 = *(char *)(param_1 + local_c);
    if ((cVar1 < 'A') || ('Z' < cVar1)) break;
    local_14 = cVar1 * local_14;
    local_10 = local_10 + cVar1;
    local_c = local_c + 1;
  }
  return true;
}
```

It loops 3 times (looks weird but that is how it looks when decompiled) iterating over the first three characters (`cVar1 = *(char *)(param_1 + local_c);`). For each loop, it checks if the character is a uppercase letter (`if ((cVar1 < 'A') || ('Z' < cVar1)) break;`), multiplies the value with `local_14` and is then added to `local_10`.

After the third loop, it returns `local_14 != 0x5ef99 || local_10 + *(char *)(param_1 + 3) != 0x111`. 

For `local_14 != 0x5ef99` it means that the multiplication of the first three characters (`local_14`) needs to equal `0x5ef99`, which is `389017` in decimal. Checking for common divisors of `389017`, the only number that is within the range of `(cVar1 < 'A') || ('Z' < cVar1)` is `73` (https://www.hackmath.net/en/calculator/divisors?n=389017&submit=Calculate), implying that the first 3 characters are `I`.

`local_10 + *(char *)(param_1 + 3) != 0x111` means that the sum of all of the characters in the first part need to equal `0x111`. Since we already know that the first 3 characters are `III` it means that `0x111-3*'I' = 54 = '6'` is the last character.

Therefore, part a is `III6`. We can verify that it is correct by using `gdb` and placing a breakpoint at `validate_b`. If the breakpoint is reached then we have the correct first part of the license key.

```
gdb-peda$ b validate_part_b
Breakpoint 1 at 0x148b
gdb-peda$ r
Starting program: /home/alex/Desktop/UISS/alex-ctf-2022/reverse/licensedtokill/solution/licensedtokill 

=--------------------------------------------------------------------=

     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777

=--------------------------------------------------------------------=

      Welcome to Agent 007's License to Kill validation program!
     If you are 007 then input your license key to verify you are
                           LICENSED TO KILL

=--------------------------------------------------------------------=

License Key: III6-BBBBB-CCCCC-DDDDD-EEEE

[----------------------------------registers-----------------------------------]
RAX: 0x7fffffffdd85 ("BBBBB-CCCCC-DDDDD-EEEE")
RBX: 0x555555555940 (<__libc_csu_init>:	endbr64)
RCX: 0x12 
RDX: 0x14d1 
RSI: 0x2d ('-')
RDI: 0x7fffffffdd85 ("BBBBB-CCCCC-DDDDD-EEEE")
RBP: 0x7fffffffddd0 --> 0x0 
RSP: 0x7fffffffdd38 --> 0x555555555845 (<main+202>:	test   eax,eax)
RIP: 0x55555555548b (<validate_part_b>:	endbr64)
R8 : 0x5 
R9 : 0x7c ('|')
R10: 0x5555555564d7 --> 0x4c6d32333b315b1b 
R11: 0x246 
R12: 0x555555555140 (<_start>:	endbr64)
R13: 0x7fffffffdec0 --> 0x1 
R14: 0x0 
R15: 0x0
EFLAGS: 0x246 (carry PARITY adjust ZERO sign trap INTERRUPT direction overflow)
[-------------------------------------code-------------------------------------]
   0x555555555486 <validate_part_a+146>:	movzx  eax,al
   0x555555555489 <validate_part_a+149>:	pop    rbp
   0x55555555548a <validate_part_a+150>:	ret    
=> 0x55555555548b <validate_part_b>:	endbr64 
   0x55555555548f <validate_part_b+4>:	push   rbp
   0x555555555490 <validate_part_b+5>:	mov    rbp,rsp
   0x555555555493 <validate_part_b+8>:	mov    QWORD PTR [rbp-0x18],rdi
   0x555555555497 <validate_part_b+12>:	mov    rax,QWORD PTR [rbp-0x18]
[------------------------------------stack-------------------------------------]
0000| 0x7fffffffdd38 --> 0x555555555845 (<main+202>:	test   eax,eax)
0008| 0x7fffffffdd40 --> 0x0 
0016| 0x7fffffffdd48 --> 0x5555555564bb --> 0x117b05624d1a1a00 
0024| 0x7fffffffdd50 --> 0x7fffffffdd80 ("III6-BBBBB-CCCCC-DDDDD-EEEE")
0032| 0x7fffffffdd58 --> 0x7fffffffdd85 ("BBBBB-CCCCC-DDDDD-EEEE")
0040| 0x7fffffffdd60 --> 0x7fffffffdd8b ("CCCCC-DDDDD-EEEE")
0048| 0x7fffffffdd68 --> 0x7fffffffdd91 ("DDDDD-EEEE")
0056| 0x7fffffffdd70 --> 0x7fffffffdd97 --> 0x55550045454545 ('EEEE')
[------------------------------------------------------------------------------]
Legend: code, data, rodata, value

Breakpoint 1, 0x000055555555548b in validate_part_b ()

```

License key so far: `III6-BBBBB-CCCCC-DDDDD-EEEE`

**`validate_part_b` analysis**

```c
bool validate_part_b(char *param_1)

{
  char cVar1;
  bool bVar2;
  char local_e;
  int local_c;
  
  if (*param_1 == 'J') {
    local_e = *param_1;
    for (local_c = 1; local_c < 4; local_c = local_c + 1) {
      cVar1 = param_1[local_c];
      if ((cVar1 < 'A') || ('Z' < cVar1)) {
        return true;
      }
      if ((int)cVar1 != local_e + 2) {
        return true;
      }
      local_e = cVar1;
    }
    bVar2 = param_1[4] != '9';
  }
  else {
    bVar2 = true;
  }
  return bVar2;
}
```

For part b, we can see the second part needs to start with `'J'` (`if (*param_1 == 'J')`) and the last character is `'9'` (`bVar2 = param_1[4] != '9';`). From 'J', the required character increments by 2 

```c
if ((int)cVar1 != local_e + 2) {
  return true;
}
local_e = cVar1;
```

Therfore, part b is `JLNP9`.

License key: `III6-JLNP9-CCCCC-DDDDD-EEEE`

**`validate_part_c` analysis**

```c
bool validate_part_c(long param_1)

{
  ulong uVar1;
  int local_1c;
  ulong local_18;
  
  local_18 = 0;
  local_1c = 0;
  while( true ) {
    if (3 < local_1c) {
      return (local_18 | (long)*(char *)(param_1 + 4) << 0x20) != 0x34544f4f59;
    }
    uVar1 = (ulong)*(char *)(param_1 + local_1c);
    if ((uVar1 < 0x41) || (0x5a < uVar1)) break;
    local_18 = local_18 | uVar1 << ((byte)(local_1c << 3) & 0x3f);
    local_1c = local_1c + 1;
  }
  return true;
}
```

- Loops 4 times.
- Only uppercase letters for the for the first loops

```c
uVar1 = (ulong)*(char *)(param_1 + local_1c);
if ((uVar1 < 0x41) || (0x5a < uVar1)) break;
```

- `((byte)(local_1c << 3) & 0x3f)` is incrementing by `8` for each loop
```python
>>> (0 << 3) & 0x3f
0
>>> (1 << 3) & 0x3f
8
>>> (2 << 3) & 0x3f
16
>>> (3 << 3) & 0x3f
24
```

- Since `((byte)(local_1c << 3) & 0x3f)` is incrementing by 8, `local_18 = local_18 | uVar1 << ((byte)(local_1c << 3) & 0x3f)` is setting the value of a byte in the `ulong`.

```python
>>> hex(0 | ord('A') << ((0 << 3) & 0x3f))
'0x41'
>>> hex(0 | ord('A') << ((1 << 3) & 0x3f))
'0x4100'
>>> hex(0 | ord('A') << ((2 << 3) & 0x3f))
'0x410000'
>>> hex(0 | ord('A') << ((3 << 3) & 0x3f))
'0x41000000'
```

- `local_18 | (long)*(char *)(param_1 + 4) << 0x20)` is setting the last byte

```python
>>> hex((0 | ord('A') << ((3 << 3) & 0x3f)) | ord('B') << 0x20)
'0x4241000000'
```

Therefore, `return (local_18 | (long)*(char *)(param_1 + 4) << 0x20) != 0x34544f4f59` indicates that `0x34544f4f59` is the hex for characters in part_c in reverse order.

```python
>>> ''.join([chr(0x59), chr(0x4f), chr(0x4f), chr(0x54), chr(0x34)])
'YOOT4'
```

License key: `III6-JLNP9-YOOT4-DDDDD-EEEE`

**`validate_part_d` analysis**

```c
void validate_part_d(undefined8 param_1)

{
  long in_FS_OFFSET;
  char local_15 [5];
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  xor(param_1,&DAT_00102008,local_15,5);
  strncmp(local_15,"KEEEK",5);
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return;
}
```

This part is quite easier than the other sections. We can see the part e is XORed with a string provided in the program (`xor(param_1,&DAT_00102008,local_15,5);`). The result of this xor needs to equal `"KEEEK`. `&DAT_00102008` is `\x1c\x0a\x12\x77\x7b\x00`. Reversing the XOR using CyberChef we can retrieve the original part e is `WOW20`.

License key: `III6-JLNP9-YOOT4-WOW20-EEEE`


**`validate_part_e` analysis**

```c
bool validate_part_e(long param_1,int param_2,char *param_3)

{
  int iVar1;
  int local_14;
  int local_10;
  
  iVar1 = atoi(param_3);
  local_14 = 0;
  for (local_10 = 0; local_10 < param_2; local_10 = local_10 + 1) {
    local_14 = local_14 + *(char *)(param_1 + local_10);
  }
  return iVar1 != local_14 + -0xd7;
}
```

From `main`

```c
iVar1 = validate_part_e(local_58,0x17,local_68);
```

This means that `validate_part_e` sums up all of the characters excluding the last part, then substracts `0xd7` from the sum. This is then compared with part e as an integer.

Summing up the license key and subtracting `0xd7` we get the number `1337`.

```python
>>> sum([ord(x) for x in "III6-JLNP9-YOOT4-WOW20-"])-0xd7
1337
```

License key: `III6-JLNP9-YOOT4-WOW20-1337`

We can then check to see if we now have the right license key.

```
$ ./licensedtokill 

=--------------------------------------------------------------------=

     0000             0000        7777777777777777/========___________
   00000000         00000000      7777^^^^^^^7777/ || ||   ___________
  000    000       000    000     777       7777/=========//
 000      000     000      000             7777// ((     //
0000      0000   0000      0000           7777//   \   //
0000      0000   0000      0000          7777//========//
0000      0000   0000      0000         7777
0000      0000   0000      0000        7777
 000      000     000      000        7777
  000    000       000    000       77777
   00000000         00000000       7777777
     0000             0000        777777777

=--------------------------------------------------------------------=

      Welcome to Agent 007's License to Kill validation program!
     If you are 007 then input your license key to verify you are
                           LICENSED TO KILL

=--------------------------------------------------------------------=

License Key: III6-JLNP9-YOOT4-WOW20-1337

YOU ARE LICENSED TO KILL 007!
Flag: ISS{OO7_l1C3n5eD_133keD!!!}
```