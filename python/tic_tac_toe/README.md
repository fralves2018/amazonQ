# Tic Tac Toe Game

A classic implementation of the Tic Tac Toe game with both human vs. human and human vs. computer modes.

## Features

- Interactive command-line interface
- 3x3 game board with intuitive coordinate system
- Two game modes:
  - Human vs. Human: Two players take turns
  - Human vs. Computer: Play against a simple AI opponent
- Simple AI with basic strategy:
  1. Win if possible
  2. Block opponent's winning move
  3. Take center if available
  4. Take corners if available
  5. Take edges if available
- Comprehensive test suite to ensure game logic works correctly

## How to Play

1. Run the game:
   ```
   python tic_tac_toe.py
   ```

2. Select a game mode:
   - 1: Human vs. Human
   - 2: Human vs. Computer
   - 3: Quit

3. Enter your moves as row and column numbers (1-3), separated by a space.
   For example, `2 3` means row 2, column 3.

4. The game board is displayed as follows:
   ```
     1 2 3
   1  | | 
     -+-+-
   2  | | 
     -+-+-
   3  | | 
   ```

5. The first player uses 'X', and the second player (or computer) uses 'O'.

6. The game ends when a player gets three of their marks in a row (horizontally, vertically, or diagonally) or when the board is full (a tie).

## Running Tests

To run the test suite:
```
python -m unittest tic_tac_toe_test.py
```

## Implementation Details

The game is implemented using object-oriented programming principles:

- `TicTacToe` class: Manages the game state and logic
- `play_game` function: Handles the game flow and user interaction
- `make_ai_move` function: Implements the AI strategy for computer player
- `main` function: Entry point that handles game mode selection and replay

The board is represented as a 3x3 nested list, with empty spaces represented by ' ' (space), 'X' for the first player, and 'O' for the second player.