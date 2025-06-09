def make_board(width, height):
    b = []
    for row in range(0,height):
        b.append([" "] * width)
    return b

def add_token(col, player, board):
    if board[0][col] != " ":
        return
    for row in range(1, len(board)):
        if board[row][col] != " ":
            board[row -1][col] = player
            return
    board[row][col] = player

def winner_horizontal(b):
    for row in range(0,len(b)):
        for col in range(0,len(b[row]) - 3):
            if b[row][col] == " ":
                continue
            if(b[row][col] == b[row][col + 1] and
               b[row][col] == b[row][col + 2] and
               b[row][col] == b[row][col + 3]):
                return b[row][col]
    return " "

def winner_vertical(b):
    for row in range(0,len(b) - 3):
        for col in range(0,len(b[row])):
            if b[row][col] == " ":
                continue
            if(b[row][col] == b[row + 1][col] and
               b[row][col] == b[row + 2][col] and
               b[row][col] == b[row + 3][col]):
                return b[row][col]
    return " "

# Diagonal to the right
def winner_diagonal1(b):
    for row in range(0,len(b) - 3):
        for col in range(0,len(b[row]) - 3):
            if b[row][col] == " ":
                continue
            if(b[row][col] == b[row + 1][col + 1] and
               b[row][col] == b[row + 2][col + 2] and
               b[row][col] == b[row + 3][col + 3]):
                return b[row][col]
    return " "

# Diagonal to the left
def winner_diagonal2(b):
    for row in range(0,len(b) - 3):
        for col in range(3,len(b[row])):
            if b[row][col] == " ":
                continue
            if(b[row][col] == b[row + 1][col - 1] and
               b[row][col] == b[row + 2][col - 2] and
               b[row][col] == b[row + 3][col - 3]):
                return b[row][col]
    return " "
                
def check_winner(board):
    for check in [winner_horizontal, winner_vertical, winner_diagonal1, winner_diagonal2]:
        winner = check(board)
        if winner != " ":
            return winner
    return None

def print_board(board):
    for row in board:
        print("| " + " | ".join(row) + " |")  # Adds spacing for readability
    print(" " + "---" * len(board[0]))  # Adds a separator line

def play_game():
    game_board = make_board(7, 6)
    players = ["X", "O"]  # You can change to "G" and "B" if you want
    turn = 0
    
    while True:
        print_board(game_board)
        player = players[turn % 2]
        col = int(input(f"Player {player}, choose a column (0-6): "))

        # Validate input
        if col < 0 or col >= len(game_board[0]) or game_board[0][col] != " ":
            print("Invalid move! Try again.")
            continue

        # Add token
        add_token(col, player, game_board)

        # Check for a winner
        winner = check_winner(game_board)
        if winner:
            print_board(game_board)
            print(f"Player {winner} wins!")
            break

        # Check for a draw
        if all(game_board[0][c] != " " for c in range(len(game_board[0]))):
            print_board(game_board)
            print("It's a draw!")
            break

        turn += 1

play_game()


