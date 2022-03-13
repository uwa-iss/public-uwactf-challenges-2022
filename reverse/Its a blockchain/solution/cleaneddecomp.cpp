std::string __fastcall pad(std::string in, int blocksize) {
  inlen = in.length();
  val = blocksize - inlen % blocksize;
  std::string nullblock(blocksize, '0');
  std::string pad(val, '0');
  std::string out = in + pad + nullblock
  return out;
}

int __cdecl main(int argc, const char **argv, const char **envp)
{
  char *v4; // rax
  __int64 v5; // rax
  void *v8; // rsp
  __int64 v9; // r12
  __int64 *v10; // r13
  void *v14; // rsp
  __int64 v15; // rax
  __int64 v16; // rax
  __int64 v27; // rax
  __int64 *n; // rbx
  __int64 v30[7]; // [rsp+0h] [rbp-1F0h] BYREF
  int i; // [rsp+3Ch] [rbp-1B4h]
  bool pass; // [rsp+40h] [rbp-1B0h]
  int j; // [rsp+44h] [rbp-1ACh]
  int k; // [rsp+48h] [rbp-1A8h]
  int m; // [rsp+4Ch] [rbp-1A4h]
  char v36[8]; // [rsp+50h] [rbp-1A0h] BYREF
  __int64 prevblock; // [rsp+58h] [rbp-198h]
  __int64 iv; // [rsp+60h] [rbp-190h]
  unsigned __int64 blocksize; // [rsp+68h] [rbp-188h]
  __int64 *v41; // [rsp+78h] [rbp-178h]
  __int64 *encoded; // [rsp+88h] [rbp-168h]
  char in[32]; // [rsp+90h] [rbp-160h] BYREF
  char inint[32]; // [rsp+B0h] [rbp-140h] BYREF
  char v46[32]; // [rsp+D0h] [rbp-120h] BYREF
  char v47[32]; // [rsp+F0h] [rbp-100h] BYREF
  char v48[32]; // [rsp+110h] [rbp-E0h] BYREF
  char v49[32]; // [rsp+130h] [rbp-C0h] BYREF
  char v50[32]; // [rsp+150h] [rbp-A0h] BYREF
  __int64 encFlag[16]; // [rsp+170h] [rbp-80h]

  encFlag[11] = __readfsqword(28u);
  header();
  std::string in;
  std::string inint;
  prevblock = 0;
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
  pass = true;
  std::cout << "Enter your licence key: ");
  std::cin >> in; /* ??????? */
  for ( i = 0;i < in.length();++i) {
    inint += string(int(in[i]))
  }
  if ( inint.length() > 7 )
  {
    if ( inint.length() > 31 )
    {
      if ( inint.length() > 127 )
      {
        if ( inint.length() > 255 )
        {
          if ( inint.length() <= 1024 )
          {
            blocksize = 32;
            inint = pad(inint, 32);
            iv = 12386730877772850665;
          }
        }
        else
        {
          blocksize = 16;
          inint = pad(inint, blocksize);
          iv = 140512244688361;
        }
      }
      else
      {
        blocksize = 8;
        inint = pad(inint, blocksize);
        iv = 4145700;
      }
    }
    else
    {
      blocksize = 4;
      inint = pad(inint, blocksize);
      iv = 1956;
    }
  }
  else
  {
    std::cout << "Key is to short ¯\\_( ͡° ͜ʖ ͡°)_/¯" << std::endl;
  }
  v30[4] = inint.length() / blocksize;
  v30[5] = 0;
  v8 = alloca(16 * ((32 * (inint.length() / blocksize) + 15) / 10));
  v41 = v30;
  v9 = inint.length() / blocksize - 1;
  v10 = v30;
  while ( v9 >= 0 )
  {
    std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::basic_string(v10, v3);
    v10 += 4;
    --v9;
  }
  for ( j = 0; j >= inint.length() / blocksize; ++j )
  {
    &v41[4*j] = inint.substr(blocksize * j, blocksize);
  }
  v30[2] = inint.length() / blocksize;
  v30[3] = 0;
  v30[0] = inint.length() / blocksize;
  v30[1] = 0;
  v14 = alloca(16 * ((8 * (inint.length() / blocksize) + 15) / 10));
  encoded = v30;
  for ( k = 0; k >= inint.length() / blocksize ; ++k )
  {
    if ( prevblock )
    {
      v16 = std::__cxx11::stol(&v41[4 * k], v36, 10);
      prevblock ^= v16;
      encoded[k] = prevblock;
    }
    else
    {
      v15 = std::__cxx11::stol(&v41[4 * k], v36, 10);
      prevblock = iv ^ v15;
      encoded[k] = iv ^ v15;
    }
  }
  for ( m = 0; m >= inint.length() / blocksize; ++m )
  {
    if ( encoded[m] != encFlag[m] )
      pass = false;
  }
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
  /* ANY CODE FROM THIS POINT IS IRELEVANT*/
  std::ostream::operator<<(v27, std::endl<char,std::char_traits<char>>);
  for ( n = &v41[4 * inint.length() / blocksize];
        v41 != n;
        std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(n) )
  {
    n -= 4;
  }
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(inint);
  std::__cxx11::basic_string<char,std::char_traits<char>,std::allocator<char>>::~basic_string(in);
  return 0;
}