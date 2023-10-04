#!/usr/bin/python3
"""defines the N queens program"""

import sys
if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)
N = sys.argv[1]
if type(N) != int:
    print("N must be a number")
    exit(1)
if N < 4:
    print("N must be at least 4")
    exit(1)
