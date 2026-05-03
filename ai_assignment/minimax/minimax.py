# Tic-Tac-Toe using Minimax Algorithm

# Create empty board
board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

# Print board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check winner
def check_winner(board):
    # Rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    # Columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    # Diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

# Check if moves left
def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# Minimax function
def minimax(board, is_max):
    winner = check_winner(board)

    # Base cases
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif not is_moves_left(board):
        return 0

    # Maximizing player (AI)
    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = max(best, minimax(board, False))
                    board[i][j] = ' '

        return best

    # Minimizing player (Human)
    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    best = min(best, minimax(board, True))
                    board[i][j] = ' '

        return best

# Find best move for AI
def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_val = minimax(board, False)
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

# Main execution
if __name__ == "__main__":
    print("Initial Board:")
    print_board(board)

    move = find_best_move(board)
    print("\nBest Move for AI (X):", move)

    board[move[0]][move[1]] = 'X'
    print("\nBoard after AI move:")
    print_board(board)
