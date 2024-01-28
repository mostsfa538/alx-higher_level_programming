#!/usr/bin/python3

def matrix_divided(matrix, div):
    """matrix division"""

    if div == 0:
        raise ZeroDivisionError('division by zero')

    if type(div) is not int:
        raise TypeError('div must be a number')
    
    first_row_length = len(matrix[0])
    for row in matrix[1:]:
        if len(row) != first_row_length:
            raise TypeError('Each row of the matrix must have the same size')

    for row in matrix:
        new_row = []
        for element in row:
            if type(element) is not int:
                raise TypeError('div must be a number')

            new_row.append(element / div)
        new_matrix.append(new_row)

    return new_matrix
