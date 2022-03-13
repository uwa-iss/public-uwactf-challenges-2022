import socketserver as sock
import time, random
from secret import FLAG,OFFSET

banner = r"""
👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏
👏                                                  👏
👏  Welcome to my ✊ ✋ ✌  game                     👏     
👏  My game is pretty simple                        👏
👏  Win me 100 times in a row and get the flag      👏
👏                                                  👏
👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏👏
"""

ROCK = chr(0x270A)
PAPER = chr(0x270B)
SCISSORS = chr(0x270C)
OPTIONS = [ROCK, PAPER, SCISSORS]

# Base class for handling request
class TCPHandler(sock.BaseRequestHandler):
    allow_reuse_address = True
    
    # Connection handler
    def handle(self):
        print(f"[+] Incoming connection: {self.client_address}")
        
        # Set random seed  
        seed = int(time.time()) + OFFSET
        random.seed(seed)
        # print("[+] Seed:", seed)
        
        self.send(banner)
        ready_prompt = f"\nAre you ready? (\033[1mY\033[0m)es or (\033[1mN\033[0m)o: "
        ready = self.receive(prompt=ready_prompt)

        if "y" in ready.lower():
            self.send(string="\n🔥🔥 LET'S START 🔥🔥\n\n")

            # Play 100 round
            for i in range(100):
                try:
                    self.send(f"\033[38;5;226mROUND {i+1}\n")
                    self.play_round(i)
                except:
                    self.request.close()

            # Win 100 round, get flag
            self.send("\n\033[32m[+]\033[0m Wow, you win the game! Here is your flag\n")
            self.send(FLAG)
            self.send("\n")

        else:
            self.send("\033[31m[-]\033[0m Return when you are ready")
            self.request.close()

    # Send data to user
    def send(self, string):
        try:
            self.request.sendall(string.encode())
        except:
            self.request.close()

    # Receive responses from user
    def receive(self, prompt="\033[33m[?]\033[0m Plese enter ✊ ✋ ✌ . What is your choice for this round: "):
        self.send(prompt)
        return self.request.recv(4096).strip().decode()
    
    # Play a single round of rock paper scissors
    def play_round(self, round):
        computer_choice = random.choice(OPTIONS)
             
        start_time = time.time()
        user_response = self.receive()
        
        if (time.time() - start_time) > 2:
            self.send("\033[31m[!]\033[0m You take too long to answer.\n")
            self.send("\033[31m[!]\033[0m See you next time!\n")
            self.request.close()

        elif user_response not in OPTIONS:
            self.send("\033[31m[!]\033[0m Your answer is not valid. You have to choose either ✊ ✋ ✌\n")
            self.send("\033[31m[!]\033[0m See you next time!\n")
            self.request.close()

        else:
            self.check_win(user_response, computer_choice, round)
        
        time.sleep(1)

    # Check if the user choose the win option
    def check_win(self, user, computer, round):
        if user == computer:
            self.send(f"\033[31m[-]\033[0m We draw, I also choose {computer}\n")
            self.send("\033[31m[!]\033[0m See you next time!\n")
            self.request.close()
        elif (user == ROCK and computer == SCISSORS) \
            or (user == PAPER and computer == ROCK) \
            or (user == SCISSORS and computer == PAPER):
            self.send(f"\033[32m[+]\033[0m You win, I choose {computer}\n")
            # Don't send prepare message in final round
            if round < 99:
                self.send("\033[32m[*]\033[0m Prepare for next round\n\n")
        else:
            self.send(f"\033[31m[-]\033[0m You lose, I choose {computer}\n")
            self.send("\033[31m[!]\033[0m See you next time!\n") 
            self.request.close()
    
class ThreadedTCPServer(sock.ThreadingMixIn, sock.TCPServer, sock.DatagramRequestHandler):
    pass

def main():
    host = '0.0.0.0'
    port = 1337

    with sock.TCPServer((host, port), TCPHandler) as server:
        print (f"[*] Server started on port: {port} ")
        
        # Activate the server; this will keep running until you
        # interrupt the program with Ctrl-C
        server.serve_forever()

if __name__== "__main__": 
    main()