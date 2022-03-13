from pwn import *
import time

ROCK = chr(0x270A)
PAPER = chr(0x270B)
SCISSORS = chr(0x270C)
OPTIONS = [ROCK, PAPER, SCISSORS]

def find_computer_choice():
    computer = random.choice(OPTIONS)
    log.info(f"COMPUTER CHOICE: {computer}")
    return computer

def send_choice(r):
    computer = find_computer_choice()
    if computer == ROCK:
        log.info(f"SENDING CHOICE: {PAPER}")
        r.sendline(PAPER.encode())
    elif computer == PAPER:
        log.info(f"SENDING CHOICE: {SCISSORS}")
        r.sendline(SCISSORS.encode())
    elif computer == SCISSORS:
        log.info(f"SENDING CHOICE: {ROCK}")
        r.sendline(ROCK.encode())

def main():
    # Try different offset
    for offset in range(-127, 128):
        host, port = '127.0.0.1', 1337
        r = remote(host, port)

        log.info(f"TRY OFFSET: {offset}")
        print(r.recvuntil(b"o:").decode())

        # Ready to play the game
        log.info("CHOOSING YES")
        r.sendline(b"yes")

        # Set random seed
        seed = int(time.time() + offset)
        random.seed(seed)
        # print(f"[!] Seed: {seed}")
        
        lose_game = False

        for round in range (100):
            print(r.recvuntil(b"round: ").decode())
            send_choice(r)
            result = r.recvline().decode()
            print(result)
            print(r.recvline().decode())
            if "win" not in result:
                lose_game = True
                break

        if lose_game:
            r.close()
        else:
            r.interactive()
            break

if __name__== '__main__':
    main()