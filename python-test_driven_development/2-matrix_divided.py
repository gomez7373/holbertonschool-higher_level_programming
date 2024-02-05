#!/usr/bin/python3i


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Prototype: def matrix_divided(matrix, div)
    matrix must be a list of lists of integers or floats, otherwise raise a
    TypeError exception with the message 'matrix must be a matrix (list of
    lists) of integers/floats'. Each row of the matrix must be of the
    same size, otherwise raise a TypeError exception
    with the message 'Each row of the matrix must have the same size'.
    div must be a number (integer or float), otherwise raise a TypeError
    exception with the message 'div must be a number'.
    div can’t be equal to 0, otherwise raise a ZeroDivisionError exception
    with the message 'division by zero'.
    All elements of the matrix should be divided by div,
    rounded to 2 decimal places.
    Returns a new matrix.
    You are not allowed to import any module
    """

    # Check if matrix is a list of lists of integers or floats
    if not all(isinstance(row, list) and all(isinstance(num, (int, float))
        for num in row) for row in matrix):
        raise TypeError('matrix will be matrix (list of lists) of int/flot')

    # Check if each row has the same size
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError('Each row of the matrix must have the same size')

    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError('division by zero')

    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(num / div, 2) for num in row] for row in matrix]

    return result_matrix

# Example usage
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
result = matrix_divided(matrix, 3)
print(result)
print(matrix)  # original matrix remains unchanged
