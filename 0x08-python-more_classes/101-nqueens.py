#!/usr/bin/python3
"""defines the N queens program"""

import sys


def is_safe(board, row, col, n):
    """
    checks if it's safe to place a queen on the given row and column

    Args:
        board (list[list[int]]): The chessboard represented as a 2D list
        row (int): The row to check.
        col (int): The column to check.
        n (int): The size of the board

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """

    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(n):
    """
    Solve the N Queens problem and print all possible solutions.

    Args:
        n (int): The size of the chessboard and the number of queens to place

    Prints:
        All possible solutions to the N Queens problem, one solution per line
    """

    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]

    def solve(row):
        if row == n:
            for i in range(n):
                for j in range(n):
                    if board[i][j] == 1:
                        print(f"[{i}, {j}", end=' ')

            print()
            return

        for col in range(n):
            if is_safe(board, row, col, n):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


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
