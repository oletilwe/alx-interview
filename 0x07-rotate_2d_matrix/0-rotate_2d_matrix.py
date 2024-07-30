#!/usr/bin/python3
def rotate_2d_matrix(matrix):
    """
    Rotate a given 2D matrix 90 degrees clockwise.

    Parameters:
    matrix: A 2D list representing the matrix to be rotated.

    Returns:
    None: The function modifies the matrix in place.
    """
    n = len(matrix)  # Determine the size of the matrix (assuming it is n x n).

    # Transpose the matrix
    # The transpose of a matrix is obtained by swapping rows with columns.
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row
    # After transposing, reversing each row gives
    for i in range(n):
        matrix[i].reverse()
