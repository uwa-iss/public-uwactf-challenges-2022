#!/usr/bin/python3

import random, time, multiprocessing, sys, select
from socket import timeout

BLACK_SQUARE = chr(0x2b1b)
WHITE_SQUARE = chr(0x2b1c)
KNIGHT = chr(0x1f40e)
FLAG = chr(0x1f3c1)

banner = f"""
***********************************************************************
***********************************************************************
*                                                                     *
*   DO YOU KNOW HOW TO MOVE THE KNIGHT ON THE CHESS BOARD?            *   
*   After doing 100 questions, I'm sure you will know how to do it    *       
*   Find the sequence of moves of 🐎 to capture the 🏁                *
*   You only have a maximum of 10 moves for each question             *
*   Good luck!                                                        *   
*                                                                     * 
***********************************************************************
***********************************************************************
"""

board = [
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
    ["","","","","","","",""],
]

row_map = {
        0: "8",
        1: "7",
        2: "6",
        3: "5",
        4: "4",
        5: "3",
        6: "2",
        7: "1", 
}

col_map = {
        0: "a",
        1: "b",
        2: "c",
        3: "d",
        4: "e",
        5: "f",
        6: "g",
        7: "h",     
}

row_map_inv = {
        "8": 0,
        "7": 1,
        "6": 2,
        "5": 3,
        "4": 4,
        "3": 5,
        "2": 6,
        "1": 7, 
}

col_map_inv = {
        "a": 0 ,
        "b": 1 ,
        "c": 2 ,
        "d": 3 ,
        "e": 4 ,
        "f": 5 ,
        "g": 6 ,
        "h": 7 ,     
}

# Initialize the chess board
def generate_basic_board():
    for row in range(8):
        for col in range(8):
            if ( col % 2 == 0 and row % 2 == 0 ) or ( col % 2 == 1 and row % 2 == 1 ):
                # print(WHITE_SQUARE, end = '')
                board[row][col] = WHITE_SQUARE
            else: 
                # print(BLACK_SQUARE, end = '')
                board[row][col] = BLACK_SQUARE

# Initialize knight position
def init_knight_pos():
    random.seed(time.time())
    row = random.randint(2,5)
    col = random.randint(2,5)
    board[row][col] = KNIGHT
    return (row,col)

# Initialize king position on the poard
def init_king_pos(knight_pos):
    while True:
        legal_pos = True
        random.seed(time.time())
        row = random.choice([0,1,2,5,6,7])
        col = random.choice([0,1,2,5,6,7])

        if knight_pos == (row, col):
            legal_pos = False
        else:
            possible_moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
            # Check if the knight can reach the king in one move
            # If yes, then randomize a new king posiition
            for move in possible_moves:
            # print(f"move vertical {move[0]}, move horizontal {move[1]}")
                new_pos_x = knight_pos[0] + move[0]
                new_pos_y = knight_pos[1] + move[1]
                new_pos = (new_pos_x, new_pos_y)
                if new_pos_x in range(0,8) and new_pos_y in range(0,8) and new_pos == (row,col):
                    legal_pos = False
                    break
        
        # Break condition
        if legal_pos:
            break
    board[row][col] = FLAG
    return (row,col)

# Print the board
def print_board():
    # Print the col index

    print (end = '  ')
    for i in range(8):
        print(chr(i+97), end = ' ')
    print()

    for row in range(8):
        # Print the row index
        print (8 - row, end = ' ')

        for col in range(8):
            if board[row][col] == KNIGHT or board[row][col] == FLAG:
                print(board[row][col], end='')
            else:
                print(board[row][col], end='')
        print()


# Print example on how to answer the problem
def print_example():

    generate_basic_board()
    board[0][0] = FLAG
    board[2][2] = KNIGHT
    knight_pos = (2,2)
    king_pos = (0,0)
    
    print("\033[1;38;5;83m[*] EXAMPLE QUESTION:\033[0m")
    print_board()
    path = solve(knight_pos, king_pos)
    print()
    print(f"\033[1;38;5;83m[*] SAMPLE SOLUTION:\033[0m {path}")
    print("\033[1;38;5;83m[*] NOTES:\033[0m") 
    print("1. There are different solutions. All are accepted")
    print("2. The answer must be in the same format as the sample solution")
    print()

# --------------------------------------------------------------------

# Map the position to the coordinate on the board
def map_coordinate(path):
    sol = []
    for move in path:
        sol.append( (row_map_inv[move[1]] ,col_map_inv[move[0]]) )
    return sol

# Check if the user answer is correct
def check_answer(user_input, knight_pos, king_pos):
    try:
        # Convert user input to list of moves in coordinate format
        path = user_input.replace(" ", "")
        path = [path[i:i+2] for i in range(0, len(path), 2)] 
        path = map_coordinate(path)
        # print(f"Map coordinate: {path}")

        # Check if less than 10 moves
        if len(path) > 11:
            return False

        # Check the knight and king position
        if path[0] != knight_pos or path[-1] != king_pos:
            return False

        possible_moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]

        # Check if every move is legal
        while len(path) > 1:
            current_pos = path.pop(0)
            next_pos = path[0]          
            move_made = (next_pos[0] - current_pos[0], next_pos[1] - current_pos[1])
            # print(f"Move made: {move_made}")
            if move_made not in possible_moves:
                return False        

        return True

    except:
        return False

def check_timeout():
    start = time.time()      
    user_input = input()
    if (time.time() - start) < 2:
        return user_input
    else: 
        return None

# --------------------------------------------------------------------

# Map the coordinate to the position on the board
def map_position(path):
    sol = ""
    for move in path:
        sol += ( col_map[move[1]] + row_map[move[0]] + " " )
    return sol

# Backtracing to find the sequence of moves
def backtrace(parent, knight_pos, king_pos):
    path = [king_pos]   
    # Backtrack from king position to knight position
    while path[-1] != knight_pos:
        parent_pos = parent[path[-1]]
        path.append(parent_pos)    
    path.reverse()
    path = map_position(path)   
    return path

# Solution to the problem
def solve(knight_pos, king_pos):
    # Queue of next position to explore
    queue = [knight_pos]
    # Keep tracked of visited square - avoid looping
    visited = [knight_pos]
    # Parent dictionary used for backtracking
    parent = {}
    
    # List of all possible moves of the knight
    possible_moves = [(-2,1), (-1,2), (1,2), (2,1), (2,-1), (1,-2), (-1,-2), (-2,-1)]
    
    while queue:
        knight_current = queue.pop(0)        
        # Check if the knight get to the king position
        if knight_current == king_pos:
            return backtrace(parent, knight_pos, king_pos)
        # Check every possible move to find the king position
        for move in possible_moves:
            # print(f"move vertical {move[0]}, move horizontal {move[1]}")
            new_pos_x = knight_current[0] + move[0]
            new_pos_y = knight_current[1] + move[1]
            new_pos = (new_pos_x, new_pos_y)
            if new_pos_x in range(0,8) and new_pos_y in range(0,8) and new_pos not in queue and new_pos not in visited:
                    queue.append(new_pos)
                    visited.append(new_pos)     
                    parent[new_pos] = knight_current  # store parent position for backtracking
                    
# --------------------------------------------------------------------

# Main  
def main():
    print(f"\033[38;5;82m {banner}")
    print_example()
    print(f"Are you ready? (\033[1mY\033[0m)es or (\033[1mN\033[0m)o:")
    
    user_input = input()

    # Start the game
    if "y" in user_input.lower():
        print ("\033[1;38;5;83m🔥🔥 LET'S START 🔥🔥\n")

        # 100 questions
        for i in range(100):
            generate_basic_board()
            knight_pos = init_knight_pos()
            king_pos = init_king_pos(knight_pos)
            
            # Print question
            print(f"Question {i + 1}:")
            print_board()
            print()
            print("[*] Please provide the solution:")

            # Time out input checking 
            user_input = check_timeout()
            if not user_input:
                print("[-] You take too long to answer. Good luck next time!")
                exit()     
        
            if not check_answer(user_input, knight_pos, king_pos):
                print("[-] Incorrect answer. Good luck next time!")
                exit()
            else:
                print("[+] Correct answer! \n")
            
            time.sleep(1)

        print("[+] Congratulations, you have mastered the skill of moving the knight!")
        print("[+] Here is your flag: FAKE{ActualFlagIsOnChallengeInstance}")

    # User not ready, exit
    else:
        print("[-] Return when you are ready")
        exit()

if __name__=='__main__':
    main()