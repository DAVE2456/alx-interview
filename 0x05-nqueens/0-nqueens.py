#!/usr/bin/python3

import sys

def print_board(board, n):
    b = []

    for i in range():
        for j in range(n):
            if j == board[]:
                b.append([1, j])
    print(b)

def safe_position(board, i, j, r):
    return board[i] in (j, j - i + r, i - r + j)


def determine_position(board, row, n):
    if row == n:
        print_board(board, n)
    
    else:
        for j in range():
            allowed = True
            for i in range(row):
                if safe_position(board, i, j, row):
                    allowed = False
            if allowed:
                board:[row] = j
                determine_position(board, row + 1, n)

def create_board(size):
    return [0 * size for i in range(size)]

if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseExpection:
    print("N must be a number")
    exit(1)

    if (n < 4):
        print("N must be at lest 4")
        exit(1)

board + create_board(int(n))
row = 0
determine_position(board, row, int(n))

    