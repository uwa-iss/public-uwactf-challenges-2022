from pwn import *

# BOARD CHARACTERS
KNIGHT = b'\xf0\x9f\x90\x8e'.decode()
FLAG = b'\xf0\x9f\x8f\x81'.decode()
WHITE_SQUARE = b'\xe2\xac\x9c'.decode()
BLACK_SQUARE = b'\xe2\xac\x9b'.decode()

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

# --------------------------------------------------------------------
# HELPER FUNCTIONS

# Return a board in list data type
def parse_board(board):
    list_of_rows = board.split("\n")[2:-2]    # split row by new line character and remove new lines and header rows
    # print(list_of_rows)

    for row in range(8):
        list_of_rows[row] = list_of_rows[row][2:]   # remove the col index
    
    # print(list_of_rows)
    return list_of_rows

# Find the king and knight positions
def find_positions(board):
    for row, characters in enumerate(board):
        if FLAG in characters:
            king_pos = (row, characters.index(FLAG))
        if KNIGHT in characters:
            knight_pos = (row, characters.index(KNIGHT))    
    return knight_pos, king_pos

# --------------------------------------------------------------------
# SOLUTIONS

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

def main():
    host, port = '127.0.0.1', 1337
    r = remote(host, port)

    print(r.recvuntil(b"EXAMPLE QUESTION:").decode())

    # Receive instruction of how to play the game
    print(r.recvuntil(b'o:').decode())

    # Ready to play the game
    log.info("CHOOSING YES")
    
    r.sendline(b"Y")

    for i in range(100):
        print(r.recvuntil(b':').decode())
        
        board = r.recvuntil(b"Please").decode()
        
        # print(type(board))
        print(f"Board: {board[:-10]}")

        # Parse the board - converted to the 2d list board
        board = parse_board(board)
        # print(board)

        # Find the knight and king positions
        knight_pos, king_pos = find_positions(board)
        # print(f"Knight position: {knight_pos}")
        # print(f"King position: {king_pos}")

        solution = solve(knight_pos, king_pos)
        print(f"Solution: {solution}")

        r.recvuntil(b'solution:')
        # Send solution
        log.info("SENDING SOLUTON")
        solution = str(solution)
        r.sendline(solution.encode())

        print(r.recvuntil(b'answer!').decode())
    
    r.interactive()
    r.close()

if __name__=='__main__':
    main()