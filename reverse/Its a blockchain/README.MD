# Challenge

**Name:** It's a blockchain

**Category:** Rev

**Difficulty:** Hard

**Author:** q3st1on

**Flag:** `ISS{buy_a_man_eat_fish_he_day_teach_fish_man_to_a_lifetime}`

**Provided Files:** [rev-blockchain.zip](publish/rev-blockchain.zip)  

## Description

People have been pirating previous versions of RoboBradan quote generator :(
To protect all my hard work from these eveil software pirates, I've used state
of the art blockchain secuirty in my liscensing system. No one wil get past my
licence requirements now. 

## Solution


#### TLDR
This is a block chaining challenge (think `CBC` without the cipher). Once people realise
what the code does, they will see that the program uses a hardcoded IV and from there they
can just decode the flag from the values in the licence array as shown in the [solve script](solution/solve.py).

#### Decompilation
For this challenge we get given a compiled c++ binary. C++ being notoriously annoying to reverse I decided to take the easy road and used IDA & Hexrays decompiler to get decompiled code and work from there. [The output of the decompiler](solution/decomp.cpp), while better than reading assembly, was far from readable. Containing such cursed things as:

```c++
std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, "Enter your licence key: ");
```
Instead of the far more sane
```c++
std::cout << "Enter your licence key: ";
```
or the entirely reasonable:
```c++
__int64 __fastcall pad(__int64 a1, __int64 a2, __int64 a3)
{
  char v5; // [rsp+26h] [rbp-8Ah] BYREF
  char v6; // [rsp+27h] [rbp-89h] BYREF
  int v7; // [rsp+28h] [rbp-88h]
  int v8; // [rsp+2Ch] [rbp-84h]
  char v9[32]; // [rsp+30h] [rbp-80h] BYREF
  char v10[32]; // [rsp+50h] [rbp-60h] BYREF
  char v11[40]; // [rsp+70h] [rbp-40h] BYREF
  unsigned __int64 v12; // [rsp+98h] [rbp-18h]

  v12 = __readfsqword(0x28u);
  v7 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(a2, a2);
  v8 = a3 - v7 % a3;
  std::allocator<char>::allocator(&v6);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string<std::allocator<char>>(
    v11,
    a3,
    48LL,
    &v6);
  std::allocator<char>::allocator(&v5);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string<std::allocator<char>>(
    v9,
    v8,
    48LL,
    &v5);
  std::operator+<char,std::char_traits<char>,std::allocator<char>>(v10, a2, v9);
  std::operator+<char,std::char_traits<char>,std::allocator<char>>(a1, v10, v11);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v10);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v9);
  std::allocator<char>::~allocator(&v5);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v11);
  std::allocator<char>::~allocator(&v6);
  return a1;
}
```
Instead of
```c++
std::string __fastcall pad(std::string in, int blocksize) {
  inlen = in.length();
  val = blocksize - inlen % blocksize;
  std::string nullblock(blocksize, '0');
  std::string pad(val, '0');
  std::string out = in + pad + nullblock
  return out;
}
```

So the first thing to do was to clean up some sections of the code.

### Cleaning up the decompiler output
My goal was to avoid as much work as possible, so I only [cleaned the code up](solution/cleaneddecomp.cpp) enough to get a good guess of what it was doing. My primary focus was cleaning up the loops, conditional statements, and user input/program output code. This turned out to be far easier than I thought.

#### Input/Output code

One of the worst things that decompilation had done was turn simple IO code into multi line abominations, as such that was the first thing I fixed. Following the concept of KISS I mainly just guessed what the code was doing, not bothering to properly make sure I was correct. While not recomended practice, I am lazy and it made the process quicker.

The first thing I fixed was where the program asks for the licence key. The decompiled code for that was:

```c++
std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, "Enter your licence key: ");
v3 = v44;
std::operator>><char,std::char_traits<char>,std::allocator<char>>((std::istream *)&std::cin);
```
From a quick look as to where `v3` and `v44` where used elsewhere in the code I was able to rewrite that as follows:
```c++
std::cout << "Enter your licence key: ");
wtf = in;
std::cin >> in;
```
As you can tell from the variable naming, `v3` was a mystery to me and as such was names `wtf`, `v44` on the other hand was easily identifiable as the variable that the user supplied value was stored in. (NOTE: later realised that `wtf` is just irrelevant for the purposes of understanding the code so just deleted it)

Next I cleaned up the final section of the code from:
```
if ( v32 )
{
  v21 = std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, "Licence Approved!!!");
  v22 = (std::ostream *)std::ostream::operator<<(v21, std::endl<char,std::char_traits<char>>);
  v23 = std::operator<<<std::char_traits<char>>(v22, "You can now use your legitimately aqquired");
  v24 = (std::ostream *)std::ostream::operator<<(v23, std::endl<char,std::char_traits<char>>);
  v25 = std::operator<<<std::char_traits<char>>(v24, "copy of the RoboBradan quote generator :)");
  v26 = (std::ostream *)std::ostream::operator<<(v25, std::endl<char,std::char_traits<char>>);
  v27 = std::operator<<<std::char_traits<char>>(v26, "block chaining is the same as blockchain... right?");
}
else
{
  v27 = std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, "No piracy allowed! Buy a licence!");
}
std::ostream::operator<<(v27, std::endl<char,std::char_traits<char>>);
```
to:
```c++
if ( pass )
{
  std::cout << "Licence Approved!!!" << std::endl;
  std::cout << "You can now use your legitimately aqquired" << std::endl;
  std::cout << "copy of the RoboBradan quote generator :)" << std::endl;
  std::cout << "block chaining is the same as blockchain... right?" << std::endl;
}
else
{
  std:: cout << "No piracy allowed! Buy a licence!" << std::endl;
}
```
Having cleaned up the IO code i moved on to loops

#### Loops
When looking at the loops I noticed 2 main issues:
1. For loops had no condition (`for ( j = 0; ; ++j )`)
2. There where these weird lumps of string related code:
```c++
v11 = j;
v12 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
if ( v11 >= v12 / v39 )
  break;
```
I quickly realised that these were interconnected as the code
```c++
std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
```
was likely getting the length of the `std::string` variable `v45` and was equivelant to
```c++
v45.length()
```

From this I was able to see that the if statement 
```c++
if ( v11 >= v12 / v39 )
  break;
```
was checking if the iterator value `j` was greater than or equal to the length of `v45` divided by `v39` as as such the for loop was actually:
```c++
for ( j = 0; j >= inint.length() / blocksize; ++j )
```
Cleaning up the rest of the loops in a similar manner, I then moved on to conditional statements.

#### Conditional Statements

This was pretty simple, just went through and simplified all the code in if/else statements till it made some kind of sense. Very tedious so I wont go through it here, I just googled stuff I didn't know and guessed what things should do and was able to simplify most conditional statements from abominations such as:
```c++
if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3) <= 0x3FF ) {
  v39 = 32LL;
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v50, v45);
  pad(v49, v50, 32LL);
  v3 = v49;
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(v45, v49);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v49);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
  v38 = 0xABE6821B0A0365E9LL;
}
```
to the slightly more sane:
```c++
if ( inint.length() <= 1024 ) {
  blocksize = 32;
  inint = pad(inint, 32);
  iv = 12386730877772850665;
}
```
### Working out what this does
The biggest hints for this challenge come from the name and the output you got upon recieving a correct flag. The challenge is called `It's a blockchain` and it prints out `block chaining is the same as blockchain... right?`. From this we can guess that the challenge uses at least some variant of [CBC](https://en.wikipedia.org/wiki/Block_cipher_mode_of_operation#Cipher_block_chaining_(CBC)) (Cipher Block Chaining). Given we have not found an encryption or decryption function here, The logical assumption is that the code must do succesive block XORing as is used in CBC encryption. The CBC encryption process is depicted bellow:

![CBC Encryption](https://upload.wikimedia.org/wikipedia/commons/d/d3/Cbc_encryption.png)

From this, we know that to decode the stored copy of the encoded flag, we must find what IV (Initialization Vector) would have been used to encrypt it, and then we can decrypt it as follows:
```python
prev = iv
plaintext = []
for i in ciphertext:
	res = i ^ prev
	prev = res
	plaintext.append(res)
```
When we look in the decompiled code we can find:
```c++
encFlag[0] = 7393415227443049;
encFlag[1] = 8077192723678156;
encFlag[2] = 4101310444290190;
encFlag[3] = 8090446768978805;
encFlag[4] = 4118192954888783;
encFlag[5] = 2719978387027670;
encFlag[6] = 3869257800022688;
encFlag[7] = 12514449250651222;
encFlag[8] = 13720115820361887;
encFlag[9] = 14458697086363679;
encFlag[10] = 14458697086363679;
```
telling us that the encoding of the padded flag resulted in 10, 16 digit blocks. When we look further into the decompiled code we can find that the `iv` used for 16 digit blocks is `140512244688361`. Using this, we can write a script to recover the flag:

```python
iv = 140512244688361
ciphertext = [7393415227443049, 8077192723678156, 4101310444290190, 8090446768978805, 4118192954888783, 2719978387027670, 3869257800022688, 12514449250651222, 13720115820361887, 14458697086363679, 14458697086363679]

prev = iv
plaintext = []
for i in ciphertext:
	res = i ^ prev
	prev = i
	plaintext.append(res)

for i in range(0, len(plaintext)): plaintext[i]=str(plaintext[i])
plaintext = "".join(plaintext)
print(plaintext)
```
The output being:
```python
73838312398117121959795109971109510197116951021051151049510410195100971219511610197991049510210511510495109971109511611195979510810510210111610510910112500000000
```
The issue we now face is seperating that huge string into the individual ascii codes to convert them to characters. The monkey way to do this is manually, but the smart (and easier) way is to just check if the start value is 1, if it is, then take the next 3 digits as the character code, if not, take the next 2. with this implemented we get the following:

```python
iv = 140512244688361
ciphertext = [7393415227443049, 8077192723678156, 4101310444290190, 8090446768978805, 4118192954888783, 2719978387027670, 3869257800022688, 12514449250651222, 13720115820361887, 14458697086363679, 14458697086363679]

prev = iv
plaintext = []
for i in ciphertext:
	res = i ^ prev
	prev = i
	plaintext.append(res)

for i in range(0, len(plaintext)): plaintext[i]=str(plaintext[i])
plaintext = "".join(plaintext)

i = 0
while i < len(plaintext):
    if plaintext[i] == "1":
        print(chr(int(plaintext[i:i+3])),end="")

        i += 3
    else:
        print(chr(int(plaintext[i:i+2])), end="")
        i += 2
print()
```
From this we get the flag `ISS{buy_a_man_eat_fish_he_day_teach_fish_man_to_a_lifetime}`