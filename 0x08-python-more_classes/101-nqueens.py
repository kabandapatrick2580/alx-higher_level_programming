#!/usr/bin/python3
"""Solves the N Queens problem."""


import sys


def solve_nqueens(n):
    """
    Solve the N Queens problem and print every possible solution.

    Args:
        n (int): The number of queens and the size of the chessboard.

    Raises:
        ValueError: If n is not an integer or smaller than 4.
    """
    if not isinstance(n, int) or n < 4:
        raise ValueError("N must be an integer >= 4")

    def is_safe(board, row, col):
        """
        Check if it's safe to place a queen on the chessboard.

        Args:
            board (list): The chessboard configuration.
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if it's safe to place a queen, False otherwise.
        """
        for i in range(col):
            if board[i] == row or \
               board[i] - i == row - col or \
               board[i] + i == row + col:
                return False
        return True

    def solve_util(board, col):
        """
        Recursive utility function to solve the N Queens problem.

        Args:
            board (list): The current chessboard configuration.
            col (int): The current column index to place a queen.

        Prints:
            The solutions to the N Queens problem.
        """
        if col == n:
            print_solution(board)
            return
        for row in range(n):
            if is_safe(board, row, col):
                board[col] = row
                solve_util(board, col + 1)

    def print_solution(board):
        """
        Print the current chessboard configuration.

        Args:
            board (list): The current chessboard configuration.
        """
        for col in board:
            row_str = '.' * col + 'Q' + '.' * (n - col - 1)
            print(row_str)

    board = [-1] * n
    solve_util(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    solve_nqueens(N)
