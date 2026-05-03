import random
import math
import copy

class Node:
    def __init__(self, board, player, parent=None):
        self.board = board
        self.player = player
        self.parent = parent
        self.children = []
        self.visits = 0
        self.wins = 0

# Print board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Get all possible moves
def get_moves(board):
    moves = []
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                moves.append((i, j))
    return moves

# Check winner
def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

# Check terminal state
def is_terminal(board):
    return check_winner(board) is not None or len(get_moves(board)) == 0

# Random simulation
def simulate(board, player):
    current = player

    while not is_terminal(board):
        moves = get_moves(board)
        move = random.choice(moves)
        board[move[0]][move[1]] = current
        current = 'O' if current == 'X' else 'X'

    winner = check_winner(board)

    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    return 0

# UCB function (FIXED)
def ucb(node):
    if node.visits == 0:
        return float('inf')

    return (node.wins / node.visits) + math.sqrt(
        2 * math.log(node.parent.visits) / node.visits
    )

# Select best node
def select(node):
    while node.children:
        node = max(node.children, key=ucb)
    return node

# Expand node
def expand(node):
    moves = get_moves(node.board)

    for move in moves:
        new_board = copy.deepcopy(node.board)
        new_board[move[0]][move[1]] = node.player

        child = Node(
            new_board,
            'O' if node.player == 'X' else 'X',
            parent=node
        )
        node.children.append(child)

    if node.children:
        return random.choice(node.children)
    return node

# Backpropagation
def backpropagate(node, result):
    while node:
        node.visits += 1
        node.wins += result
        node = node.parent

# MCTS main function
def mcts(root, iterations=500):
    for _ in range(iterations):

        # Selection
        node = select(root)

        # Expansion
        if not is_terminal(node.board):
            node = expand(node)

        # Simulation
        result = simulate(copy.deepcopy(node.board), node.player)

        # Backpropagation
        backpropagate(node, result)

    # Choose best child
    best_child = max(root.children, key=lambda n: n.visits)
    return best_child

# MAIN
if __name__ == "__main__":
    board = [[' ' for _ in range(3)] for _ in range(3)]
    root = Node(board, 'X')

    print("Initial Board:")
    print_board(board)

    best = mcts(root)

    print("\nBoard after MCTS move:")
    print_board(best.board)
