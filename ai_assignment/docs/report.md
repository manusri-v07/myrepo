# AI Assignment Report

## 1. Introduction

This project implements four fundamental Artificial Intelligence search algorithms using the Tic-Tac-Toe game:

* Minimax
* Alpha-Beta Pruning
* Heuristic Alpha-Beta
* Monte Carlo Tree Search (MCTS)

The objective is to compare their working, efficiency, and decision-making capability.

---

## 2. Minimax Algorithm

### Description

Minimax is a recursive algorithm used in decision-making and game theory. It assumes:

* One player (AI) maximizes score
* Opponent minimizes score

### Key Code Snippet

```python
def minimax(board, is_max):
    if is_max:
        best = -1000
        for move in moves:
            best = max(best, minimax(...))
```

### Output

* AI selects an optimal move
* Works correctly for all board states

---

## 3. Alpha-Beta Pruning

### Description

Alpha-Beta pruning improves Minimax by eliminating branches that do not affect the final decision.

### Key Code Snippet

```python
if beta <= alpha:
    break
```

### Advantages

* Faster than Minimax
* Same optimal result

---

## 4. Heuristic Alpha-Beta

### Description

This is a depth-limited version of Alpha-Beta using an evaluation function.

### Key Code Snippet

```python
if depth == MAX_DEPTH:
    return evaluate(board)
```

### Advantages

* Reduces computation time
* Suitable for large problems

### Limitation

* May not always produce optimal result

---

## 5. Monte Carlo Tree Search (MCTS)

### Description

MCTS is a probabilistic algorithm that uses random simulations to determine the best move.

### Steps

1. Selection
2. Expansion
3. Simulation
4. Backpropagation

### Key Code Snippet

```python
def ucb(node):
    return (node.wins / node.visits) + sqrt(...)
```

### Features

* Does not require full tree exploration
* Produces strong moves using simulations

---

## 6. Comparison

| Algorithm            | Accuracy | Speed  | Type          |
| -------------------- | -------- | ------ | ------------- |
| Minimax              | High     | Slow   | Exact         |
| Alpha-Beta           | High     | Faster | Exact         |
| Heuristic Alpha-Beta | Medium   | Fast   | Approximate   |
| MCTS                 | Medium   | Fast   | Probabilistic |

---

## 7. Project Structure

```
ai_assignment/
├── minimax/
├── alpha_beta/
├── heuristic_alpha_beta/
├── mcts/
├── docs/
├── tests/
```

---

## 8. Test Cases

1. Empty board → valid move generated
2. One move left → AI selects last move
3. Winning condition → AI chooses winning move
4. Blocking condition → AI blocks opponent
5. Full board → no moves available

---

## 9. Output

* All algorithms executed successfully
* Correct moves generated in each case
* MCTS produces slightly varying outputs due to randomness

---

## 10. Conclusion

All four algorithms were successfully implemented and tested.

* Minimax guarantees optimal solutions
* Alpha-Beta improves efficiency
* Heuristic Alpha-Beta balances speed and accuracy
* MCTS provides strong approximate solutions using randomness

---

## 11. GitHub Repository

Full source code is available in the GitHub repository submitted along with this report.

