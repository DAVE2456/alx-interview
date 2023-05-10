#!/usr/bin/python3

def rotate_2d_matrix(matrix):
    n = len(matrix)
    # Step 1: Transpose the matrix
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    # Step 2: Reverse each row of the transposed matrix
    for i in range(n):
        matrix[i] = matrix[i][::-1]
