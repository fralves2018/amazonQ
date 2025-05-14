#!/usr/bin/env python3
import unittest
from tic_tac_toe import TicTacToe, make_ai_move

class TestTicTacToe(unittest.TestCase):
    """
    Test cases for the TicTacToe class.
    """
    
    def setUp(self):
        """
        Set up a new game instance before each test.
        """
        self.game = TicTacToe()
    
    def test_initial_board(self):
        """
        Test that the board is initialized correctly.
        """
        for row in range(3):
            for col in range(3):
                self.assertEqual(self.game.board[row][col], ' ')
        self.assertEqual(self.game.current_player, 'X')
        self.assertEqual(self.game.moves_count, 0)
    
    def test_make_move(self):
        """
        Test that making a move works correctly.
        """
        # Valid move
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')
        self.assertEqual(self.game.moves_count, 1)
        
        # Invalid move - already occupied
        self.assertFalse(self.game.make_move(0, 0))
        self.assertEqual(self.game.board[0][0], 'X')
        self.assertEqual(self.game.current_player, 'O')
        self.assertEqual(self.game.moves_count, 1)
        
        # Invalid move - out of bounds
        self.assertFalse(self.game.make_move(3, 3))
        self.assertEqual(self.game.current_player, 'O')
        self.assertEqual(self.game.moves_count, 1)
    
    def test_check_winner_rows(self):
        """
        Test that checking for a winner in rows works correctly.
        """
        # No winner initially
        self.assertIsNone(self.game.check_winner())
        
        # X wins in first row
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'X'
        self.game.board[0][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Reset and test second row
        self.setUp()
        self.game.board[1][0] = 'O'
        self.game.board[1][1] = 'O'
        self.game.board[1][2] = 'O'
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Reset and test third row
        self.setUp()
        self.game.board[2][0] = 'X'
        self.game.board[2][1] = 'X'
        self.game.board[2][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_columns(self):
        """
        Test that checking for a winner in columns works correctly.
        """
        # X wins in first column
        self.game.board[0][0] = 'X'
        self.game.board[1][0] = 'X'
        self.game.board[2][0] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Reset and test second column
        self.setUp()
        self.game.board[0][1] = 'O'
        self.game.board[1][1] = 'O'
        self.game.board[2][1] = 'O'
        self.assertEqual(self.game.check_winner(), 'O')
        
        # Reset and test third column
        self.setUp()
        self.game.board[0][2] = 'X'
        self.game.board[1][2] = 'X'
        self.game.board[2][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
    
    def test_check_winner_diagonals(self):
        """
        Test that checking for a winner in diagonals works correctly.
        """
        # X wins in main diagonal
        self.game.board[0][0] = 'X'
        self.game.board[1][1] = 'X'
        self.game.board[2][2] = 'X'
        self.assertEqual(self.game.check_winner(), 'X')
        
        # Reset and test other diagonal
        self.setUp()
        self.game.board[0][2] = 'O'
        self.game.board[1][1] = 'O'
        self.game.board[2][0] = 'O'
        self.assertEqual(self.game.check_winner(), 'O')
    
    def test_check_tie(self):
        """
        Test that checking for a tie works correctly.
        """
        # Set up a tie scenario
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'O'
        self.game.board[0][2] = 'X'
        self.game.board[1][0] = 'X'
        self.game.board[1][1] = 'O'
        self.game.board[1][2] = 'X'
        self.game.board[2][0] = 'O'
        self.game.board[2][1] = 'X'
        self.game.board[2][2] = 'O'
        self.game.moves_count = 9
        
        self.assertEqual(self.game.check_winner(), 'Tie')
    
    def test_get_empty_cells(self):
        """
        Test that getting empty cells works correctly.
        """
        # All cells are empty initially
        empty_cells = self.game.get_empty_cells()
        self.assertEqual(len(empty_cells), 9)
        
        # Make some moves
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        
        # Check remaining empty cells
        empty_cells = self.game.get_empty_cells()
        self.assertEqual(len(empty_cells), 7)
        self.assertNotIn((0, 0), empty_cells)
        self.assertNotIn((1, 1), empty_cells)
    
    def test_is_board_full(self):
        """
        Test that checking if the board is full works correctly.
        """
        # Board is not full initially
        self.assertFalse(self.game.is_board_full())
        
        # Fill the board
        for row in range(3):
            for col in range(3):
                self.game.board[row][col] = 'X' if (row + col) % 2 == 0 else 'O'
        self.game.moves_count = 9
        
        # Board should be full now
        self.assertTrue(self.game.is_board_full())
    
    def test_ai_move(self):
        """
        Test that the AI makes valid moves.
        """
        # AI should take center on first move
        self.game.current_player = 'O'
        self.game.moves_count = 1
        ai_row, ai_col = make_ai_move(self.game)
        self.assertEqual((ai_row, ai_col), (1, 1))
        
        # AI should block a winning move
        self.setUp()
        self.game.board[0][0] = 'X'
        self.game.board[0][1] = 'X'
        self.game.current_player = 'O'
        ai_row, ai_col = make_ai_move(self.game)
        self.assertEqual((ai_row, ai_col), (0, 2))
        
        # AI should take a winning move
        self.setUp()
        self.game.board[0][0] = 'O'
        self.game.board[0][1] = 'O'
        self.game.current_player = 'O'
        ai_row, ai_col = make_ai_move(self.game)
        self.assertEqual((ai_row, ai_col), (0, 2))


if __name__ == '__main__':
    unittest.main()