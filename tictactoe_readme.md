# 🎮 Intelligent Tic-Tac-Toe AI

An unbeatable Tic-Tac-Toe AI implementation using the Minimax algorithm with Alpha-Beta pruning optimization. This project demonstrates advanced artificial intelligence concepts and game theory principles.

## 🚀 Features

- **Unbeatable AI**: Guarantees optimal play - the AI will never lose
- **Minimax Algorithm**: Complete game tree traversal for perfect decision making
- **Alpha-Beta Pruning**: Performance optimization reducing computational complexity
- **Interactive GUI**: Clean PyGame interface for seamless gameplay
- **Perfect Game Logic**: Comprehensive win detection and move validation
- **Immutable State Management**: Proper board state handling during recursive analysis

## 🧠 Algorithm Overview

### Minimax Algorithm
The AI uses the Minimax algorithm to evaluate all possible future game states and select the move that maximizes its chance of winning while minimizing the opponent's chance. The algorithm:

- Recursively explores the complete game tree
- Assigns utility values: +1 (AI wins), -1 (player wins), 0 (tie)
- Selects moves that lead to the best possible outcome

### Alpha-Beta Pruning
To optimize performance, I implemented Alpha-Beta pruning which:
- Eliminates unnecessary branches in the search tree
- Maintains the same optimal results with significantly reduced computation
- Improves response time, especially in early game states

## 🛠️ Technical Implementation

### Core Functions Implemented
- `player()` - Determines whose turn it is
- `actions()` - Returns all possible moves
- `result()` - Generates new board state from a move
- `winner()` - Detects win conditions
- `terminal()` - Checks if game is over
- `utility()` - Calculates board value
- `minimax()` - Main AI decision-making function with Alpha-Beta pruning

### Key Technical Concepts
- **Game Theory**: Mathematical modeling of strategic decision-making
- **Recursive Problem Solving**: Breaking down complex decisions into smaller subproblems
- **State Space Search**: Systematic exploration of all possible game states
- **Optimization**: Algorithm efficiency improvements through pruning

## 🎯 Installation & Usage

### Prerequisites
- Python 3.12 or higher
- pip package manager

### Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/tictactoe-ai.git
cd tictactoe-ai
```

2. Install required dependencies:
```bash
pip3 install -r requirements.txt
```

3. Run the game:
```bash
python runner.py
```

## 🎮 How to Play

1. Launch the game using the command above
2. Click on any empty cell to make your move
3. The AI will automatically make its move
4. Try to beat the AI (spoiler: you can't! 😄)
5. The game will detect wins, losses, and ties automatically

## 📊 Performance Analysis

- **Time Complexity**: O(b^d) where b is branching factor and d is depth
- **Space Complexity**: O(d) for the recursion stack
- **Optimization**: Alpha-Beta pruning reduces average time complexity significantly
- **Game Tree Size**: Up to 255,168 possible game states in Tic-Tac-Toe

## 🏗️ Project Structure

```
tictactoe-ai/
├── runner.py          # PyGame GUI implementation
├── tictactoe.py       # Core game logic and AI
├── requirements.txt   # Python dependencies
├── README.md         # This file
└── OpenSans-Regular.ttf  # Font file for GUI
```

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- **Artificial Intelligence**: Classic AI algorithms and game-playing strategies
- **Algorithm Design**: Implementing and optimizing recursive algorithms
- **Game Theory**: Mathematical modeling of competitive scenarios
- **Python Programming**: Advanced concepts including deep copying and recursion
- **Software Engineering**: Clean, modular code architecture
- **Performance Optimization**: Algorithm efficiency improvements

## 🔍 Code Highlights

### Minimax with Alpha-Beta Pruning
```python
def minimax(board, alpha=float('-inf'), beta=float('inf')):
    """
    Returns the optimal action for the current player using Minimax
    with Alpha-Beta pruning for improved performance.
    """
    if terminal(board):
        return None
    
    current_player = player(board)
    
    if current_player == X:
        # Maximizing player
        max_eval = float('-inf')
        best_action = None
        
        for action in actions(board):
            eval_score = min_value(result(board, action), alpha, beta)
            if eval_score > max_eval:
                max_eval = eval_score
                best_action = action
            alpha = max(alpha, eval_score)
            if beta <= alpha:
                break  # Beta cutoff
        
        return best_action
    else:
        # Minimizing player
        min_eval = float('inf')
        best_action = None
        
        for action in actions(board):
            eval_score = max_value(result(board, action), alpha, beta)
            if eval_score < min_eval:
                min_eval = eval_score
                best_action = action
            beta = min(beta, eval_score)
            if beta <= alpha:
                break  # Alpha cutoff
        
        return best_action
```

## 🤝 Contributing

This project was completed as part of CS50's Introduction to Artificial Intelligence with Python. While it's primarily for educational purposes, suggestions and improvements are welcome!

## 📜 License

This project is part of CS50 AI coursework. Please respect academic integrity policies if you're currently enrolled in the course.

## 🙏 Acknowledgments

- **CS50 AI Course**: Harvard University's excellent introduction to AI concepts
- **Game Theory**: Classical minimax algorithm foundations
- **PyGame Community**: For the excellent game development framework

## 📈 Future Enhancements

Potential improvements for this project:
- [ ] Add difficulty levels (intentionally suboptimal play)
- [ ] Implement iterative deepening for even better performance
- [ ] Add game statistics and move history
- [ ] Create different board sizes (4x4, 5x5)
- [ ] Add network multiplayer functionality

---

**Challenge**: Try to beat the AI! 🎯 (Hint: The best you can do is a tie if you play perfectly!)

*Made with ❤️ and lots of recursive thinking*