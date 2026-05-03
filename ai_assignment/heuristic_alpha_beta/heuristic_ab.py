# Tic-Tac-Toe using Heuristic Alpha-Beta (Depth Limited)

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
]

MAX_DEPTH = 3  # 🔥 depth limit

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != ' ':
        return board[0][2]

    return None

def is_moves_left(board):
    for row in board:
        if ' ' in row:
            return True
    return False

# 🔥 Heuristic Evaluation Function
def evaluate(board):
    winner = check_winner(board)

    if winner == 'X':
        return 10
    elif winner == 'O':
        return -10
    else:
        return 0

# 🔥 Alpha-Beta with Depth Limit
def minimax(board, depth, is_max, alpha, beta):
    score = evaluate(board)

    # Stop if terminal OR depth reached
    if score == 10 or score == -10:
        return score

    if not is_moves_left(board):
        return 0

    if depth == MAX_DEPTH:
        return score  # heuristic used here

    if is_max:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'

                    value = minimax(board, depth + 1, False, alpha, beta)
                    best = max(best, value)

                    board[i][j] = ' '

                    alpha = max(alpha, best)

                    if beta <= alpha:
                        break

        return best

    else:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'

                    value = minimax(board, depth + 1, True, alpha, beta)
                    best = min(best, value)

                    board[i][j] = ' '

                    beta = min(beta, best)

                    if beta <= alpha:
                        break

        return best

def find_best_move(board):
    best_val = -1000
    best_move = (-1, -1)

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'

                move_val = minimax(board, 0, False, -1000, 1000)

                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

if __name__ == "__main__":
    print("Initial Board:")
    print_board(board)

    move = find_best_move(board)
    print("\nBest Move for AI (X):", move)

    board[move[0]][move[1]] = 'X'
    print("\nBoard after AI move:")
    print_board(board)
