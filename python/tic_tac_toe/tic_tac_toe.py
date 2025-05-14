#!/usr/bin/env python3
# Tic-Tac-Toe Game

class TicTacToe:
    """
    A class representing a Tic-Tac-Toe game.

    This class implements the game logic for a standard 3x3 Tic-Tac-Toe board.
    Players take turns placing 'X' and 'O' markers on the board until one player
    wins or the game ends in a tie.

    Attributes:
        board (list): A 3x3 nested list representing the game board.
                     Empty spaces are represented by ' '.
        current_player (str): Keeps track of whose turn it is ('X' or 'O').
    """    
    def __init__(self):
        # Initialize a 3x3 board as a 2D array for better readability
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.moves_count = 0

    def make_move(self, row, col):
        """
        Attempts to make a move at the specified position.
        
        Args:
            row (int): Row index (0-2)
            col (int): Column index (0-2)
            
        Returns:
            bool: True if the move was successful, False otherwise
        """
        if 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.moves_count += 1
            self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False

    def check_winner(self):
        """
        Checks if there is a winner or if the game is a tie.
        
        Returns:
            str or None: 'X' or 'O' if there's a winner, 'Tie' if the game is a tie,
                        None if the game is still ongoing.
        """
        # Check rows
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != ' ':
                return self.board[row][0]
        
        # Check columns
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return self.board[0][col]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return self.board[0][2]
        
        # Check for tie
        if self.moves_count == 9:
            return 'Tie'
        
        # Game is still ongoing
        return None

    def print_board(self):
        """
        Prints the current state of the board with row and column indices.
        """
        print("\n  1 2 3")
        for i in range(3):
            print(f"{i+1} ", end="")
            for j in range(3):
                print(self.board[i][j], end="")
                if j < 2:
                    print("|", end="")
            print()
            if i < 2:
                print("  -+-+-")

    def get_empty_cells(self):
        """
        Returns a list of empty cells on the board.
        
        Returns:
            list: List of (row, col) tuples representing empty cells
        """
        empty_cells = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    empty_cells.append((row, col))
        return empty_cells

    def is_board_full(self):
        """
        Checks if the board is full.
        
        Returns:
            bool: True if the board is full, False otherwise
        """
        return self.moves_count == 9


def play_game(ai_opponent=False):
    """
    Main game loop function that handles the gameplay of Tic-Tac-Toe.

    Args:
        ai_opponent (bool): If True, player 'O' will be controlled by a simple AI.
                           Default is False (human vs human).

    This function creates a new TicTacToe game instance and manages the game flow by:
    - Displaying the current board state
    - Getting player moves via input
    - Validating moves
    - Making moves and checking for a winner
    - Handling invalid inputs
    - Announcing the game result

    The game continues until there is either a winner or a tie.

    Returns:
        str: The result of the game ('X', 'O', or 'Tie')
    """
    game = TicTacToe()
    winner = None
    
    print("\nWelcome to Tic-Tac-Toe!")
    print("Enter your moves as row and column numbers (1-3).")
    print("For example, '2 3' means row 2, column 3.\n")
    
    if ai_opponent:
        print("You are playing as 'X' against the computer ('O').")
    else:
        print("Player 'X' goes first, followed by player 'O'.")

    while not winner:
        game.print_board()
        
        # Human player's turn
        if not ai_opponent or game.current_player == 'X':
            try:
                move = input(f"\nPlayer {game.current_player}, enter your move (row column): ")
                row, col = map(int, move.split())
                
                # Convert from 1-indexed (user input) to 0-indexed (internal representation)
                row -= 1
                col -= 1
                
                if 0 <= row < 3 and 0 <= col < 3:
                    if game.make_move(row, col):
                        winner = game.check_winner()
                    else:
                        print("That position is already taken. Try again.")
                else:
                    print("Invalid move. Please enter row and column numbers between 1 and 3.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        
        # AI player's turn
        else:
            print("\nComputer (O) is making a move...")
            ai_move = make_ai_move(game)
            row, col = ai_move
            game.make_move(row, col)
            winner = game.check_winner()

    # Game over
    game.print_board()
    if winner == 'Tie':
        print("\nIt's a tie!")
    else:
        if ai_opponent and winner == 'O':
            print("\nComputer (O) wins!")
        else:
            print(f"\nPlayer {winner} wins!")
    
    return winner


def make_ai_move(game):
    """
    Makes a move for the AI player using a simple strategy.
    
    Strategy:
    1. If there's a winning move, take it
    2. If the opponent has a winning move, block it
    3. Take the center if available
    4. Take a corner if available
    5. Take any available edge
    
    Args:
        game (TicTacToe): The current game state
        
    Returns:
        tuple: (row, col) representing the AI's move
    """
    # Get all empty cells
    empty_cells = game.get_empty_cells()
    
    # If this is the first move and center is available, take it
    if game.moves_count == 1 and (1, 1) in empty_cells:
        return (1, 1)
    
    # Check if AI can win in the next move
    for row, col in empty_cells:
        game.board[row][col] = 'O'
        if game.check_winner() == 'O':
            game.board[row][col] = ' '  # Reset the cell
            return (row, col)
        game.board[row][col] = ' '  # Reset the cell
    
    # Check if opponent can win in the next move and block
    for row, col in empty_cells:
        game.board[row][col] = 'X'
        if game.check_winner() == 'X':
            game.board[row][col] = ' '  # Reset the cell
            return (row, col)
        game.board[row][col] = ' '  # Reset the cell
    
    # Take center if available
    if (1, 1) in empty_cells:
        return (1, 1)
    
    # Take corners if available
    corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
    available_corners = [corner for corner in corners if corner in empty_cells]
    if available_corners:
        return available_corners[0]
    
    # Take any available edge
    edges = [(0, 1), (1, 0), (1, 2), (2, 1)]
    available_edges = [edge for edge in edges if edge in empty_cells]
    if available_edges:
        return available_edges[0]
    
    # This should never happen if the function is called correctly
    return empty_cells[0]


def main():
    """
    Main function to start the game and handle replay.
    """
    print("\n===== TIC-TAC-TOE =====")
    print("A classic game of X's and O's")
    
    while True:
        print("\nGame Modes:")
        print("1. Human vs Human")
        print("2. Human vs Computer")
        print("3. Quit")
        
        try:
            choice = int(input("\nSelect a game mode (1-3): "))
            
            if choice == 1:
                play_game(ai_opponent=False)
            elif choice == 2:
                play_game(ai_opponent=True)
            elif choice == 3:
                print("\nThanks for playing! Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                continue
            
            play_again = input("\nPlay again? (y/n): ").lower()
            if play_again != 'y':
                print("\nThanks for playing! Goodbye!")
                break
                
        except ValueError:
            print("Invalid input. Please enter a number.")


if __name__ == "__main__":
    main()