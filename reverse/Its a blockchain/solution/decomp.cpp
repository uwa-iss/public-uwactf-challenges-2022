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

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *v3; // rsi
  char *v4; // rax
  __int64 v5; // rax
  unsigned __int64 v6; // rax
  unsigned __int64 v7; // rbx
  void *v8; // rsp
  __int64 v9; // r12
  __int64 *v10; // r13
  unsigned __int64 v11; // r12
  unsigned __int64 v12; // rax
  unsigned __int64 v13; // rax
  void *v14; // rsp
  __int64 v15; // rax
  __int64 v16; // rax
  unsigned __int64 v17; // r12
  unsigned __int64 v18; // rax
  unsigned __int64 v19; // r12
  unsigned __int64 v20; // rax
  __int64 v21; // rax
  std::ostream *v22; // rax
  __int64 v23; // rax
  std::ostream *v24; // rax
  __int64 v25; // rax
  std::ostream *v26; // rax
  __int64 v27; // rax
  __int64 *n; // rbx
  __int64 v30[7]; // [rsp+0h] [rbp-1F0h] BYREF
  int i; // [rsp+3Ch] [rbp-1B4h]
  int v32; // [rsp+40h] [rbp-1B0h]
  int j; // [rsp+44h] [rbp-1ACh]
  int k; // [rsp+48h] [rbp-1A8h]
  int m; // [rsp+4Ch] [rbp-1A4h]
  char v36[8]; // [rsp+50h] [rbp-1A0h] BYREF
  __int64 v37; // [rsp+58h] [rbp-198h]
  __int64 v38; // [rsp+60h] [rbp-190h]
  unsigned __int64 v39; // [rsp+68h] [rbp-188h]
  unsigned __int64 v40; // [rsp+70h] [rbp-180h]
  __int64 *v41; // [rsp+78h] [rbp-178h]
  unsigned __int64 v42; // [rsp+80h] [rbp-170h]
  __int64 *v43; // [rsp+88h] [rbp-168h]
  char v44[32]; // [rsp+90h] [rbp-160h] BYREF
  char v45[32]; // [rsp+B0h] [rbp-140h] BYREF
  char v46[32]; // [rsp+D0h] [rbp-120h] BYREF
  char v47[32]; // [rsp+F0h] [rbp-100h] BYREF
  char v48[32]; // [rsp+110h] [rbp-E0h] BYREF
  char v49[32]; // [rsp+130h] [rbp-C0h] BYREF
  char v50[32]; // [rsp+150h] [rbp-A0h] BYREF
  __int64 v51[16]; // [rsp+170h] [rbp-80h]

  v51[11] = __readfsqword(0x28u);
  header();
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v44, argv);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v45, argv);
  v37 = 0LL;
  v51[0] = 0x1A4445A04F0769LL;
  v51[1] = 0x1CB229FB13C3CCLL;
  v51[2] = 0xE921EC025408ELL;
  v51[3] = 0x1CBE37EDBD3B75LL;
  v51[4] = 0xEA1798431524FLL;
  v51[5] = 0x9A9CE518E36D6LL;
  v51[6] = 0xDBF11C8B6FAA0LL;
  v51[7] = 0x2C75D346250C56LL;
  v51[8] = 0x30BE5F65BFF89FLL;
  v51[9] = 0x335E1BBFBF681FLL;
  v51[10] = 0x335E1BBFBF681FLL;
  v32 = 1;
  std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, "Enter your licence key: ");
  v3 = v44;
  std::operator>><char,std::char_traits<char>,std::allocator<char>>((std::istream *)&std::cin);
  for ( i = 0;
        i < (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(
                                v44,
                                v3);
        ++i )
  {
    v4 = (char *)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator[](v44, i);
    std::__cxx11::to_string((std::__cxx11 *)v50, *v4);
    v3 = v50;
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator+=(v45, v50);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
  }
  if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3) > 7 )
  {
    if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3) > 0x1F )
    {
      if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(
                               v45,
                               v3) > 0x7F )
      {
        if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(
                                 v45,
                                 v3) > 0xFF )
        {
          if ( (unsigned __int64)std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(
                                   v45,
                                   v3) <= 0x3FF )
          {
            v39 = 32LL;
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v50, v45);
            pad(v49, v50, 32LL);
            v3 = v49;
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(v45, v49);
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v49);
            std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
            v38 = 0xABE6821B0A0365E9LL;
          }
        }
        else
        {
          v39 = 16LL;
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v50, v45);
          pad(v48, v50, 16LL);
          v3 = v48;
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(v45, v48);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v48);
          std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
          v38 = 0x7FCB8E6E65E9LL;
        }
      }
      else
      {
        v39 = 8LL;
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v50, v45);
        pad(v47, v50, 8LL);
        v3 = v47;
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(v45, v47);
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v47);
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
        v38 = 4145700LL;
      }
    }
    else
    {
      v39 = 4LL;
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v50, v45);
      pad(v46, v50, 4LL);
      v3 = v46;
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(v45, v46);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v46);
      std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
      v38 = 1956LL;
    }
  }
  else
  {
    v5 = std::operator<<<std::char_traits<char>>((std::ostream *)&std::cout, aKeyIsToShort);
    v3 = (char *)std::endl<char,std::char_traits<char>>;
    std::ostream::operator<<(v5, std::endl<char,std::char_traits<char>>);
  }
  v6 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
  v7 = v6 / v39;
  v40 = v6 / v39 - 1;
  v30[4] = v6 / v39;
  v30[5] = 0LL;
  v8 = alloca(16 * ((32 * (v6 / v39) + 15) / 0x10));
  v41 = v30;
  v9 = v40;
  v10 = v30;
  while ( v9 >= 0 )
  {
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v10, v3);
    v10 += 4;
    --v9;
  }
  for ( j = 0; ; ++j )
  {
    v11 = j;
    v12 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
    if ( v11 >= v12 / v39 )
      break;
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::substr(v50, v45, v39 * j, v39);
    v3 = v50;
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::operator=(&v41[4 * j], v50);
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v50);
  }
  v13 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
  v42 = v13 / v39 - 1;
  v30[2] = v13 / v39;
  v30[3] = 0LL;
  v30[0] = v13 / v39;
  v30[1] = 0LL;
  v14 = alloca(16 * ((8 * (v13 / v39) + 15) / 0x10));
  v43 = v30;
  for ( k = 0; ; ++k )
  {
    v17 = k;
    v18 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
    if ( v17 >= v18 / v39 )
      break;
    v3 = v36;
    if ( v37 )
    {
      v16 = std::__cxx11::stol(&v41[4 * k], v36, 10LL);
      v37 ^= v16;
      v43[k] = v37;
    }
    else
    {
      v15 = std::__cxx11::stol(&v41[4 * k], v36, 10LL);
      v37 = v38 ^ v15;
      v43[k] = v38 ^ v15;
    }
  }
  for ( m = 0; ; ++m )
  {
    v19 = m;
    v20 = std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::length(v45, v3);
    if ( v19 >= v20 / v39 )
      break;
    if ( v43[m] != v51[m] )
      v32 = 0;
  }
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
  for ( n = &v41[4 * v7];
        v41 != n;
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(n) )
  {
    n -= 4;
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v45);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(v44);
  return 0;
}