from pwn import *
import binascii

RHOST = 'localhost'
RPORT = 4246

TARGET = "admin"

def modify_byte(byte_array, value, index):
    return byte_array[:index] + bytes([value]) + byte_array[index + 1 :]

def main():
    p = remote(RHOST, RPORT)

    r = p.recvuntil(': '.encode(), drop = True)
    iv_hex = p.recvline().decode().strip()
    iv = binascii.unhexlify(iv_hex)
    r = p.recvuntil(': '.encode(), drop = True)
    ct_hex = p.recvline().decode().strip()
    
    # Try to modify the IV value at the specific indexes such that on the
    # final XOR the plaintext changes from 'u=guest' to 'u=admin'
    for index in range(2, 7):
        for test_val in range(1 << 8):
            test_iv_hex = modify_byte(iv, test_val, index).hex()
            p.sendline(test_iv_hex.encode())
            p.sendline(ct_hex.encode())
            p.recvuntil('Welcome '.encode(), drop=True)
            result_name = p.recvline().decode().strip()[:-1]

            p.sendline("Y".encode())
            try:
                if result_name[index-2] == TARGET[index-2]:
                    print("found iv value! current name: ", result_name)
                    iv = binascii.unhexlify(test_iv_hex)
                    break
            except:
                pass

    p.interactive()

if __name__ == "__main__":
    main()