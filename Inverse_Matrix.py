from copy import deepcopy


def invert_matrix(matrix: list[list[int]]):
    if len(matrix) != len(matrix[0]):
        raise Exception(f'Invalid matrix (not square), matrix: {matrix}')
    size = len(matrix)

    mat = deepcopy(matrix)
    augmented_matrix = [[1 if i == j else 0 for i in range(size)]
                        for j in range(size)]

    for row in range(size):
        # divide the row
        factor_row = mat[row][row]  # divide by the first element
        for col in range(size):
            mat[row][col] /= factor_row
            augmented_matrix[row][col] /= factor_row

        # eliminate current column
        for row_minor in range(size):
            if row_minor == row:
                continue
            factor_col = mat[row_minor][row] / mat[row][row]
            for col_minor in range(size):
                mat[row_minor][col_minor] -= factor_col * mat[row][col_minor]
                augmented_matrix[row_minor][col_minor] -= factor_col * \
                    augmented_matrix[row][col_minor]
    return augmented_matrix


if __name__ == '__main__':
    inverse = invert_matrix([[6, 24, 1], [13, 16, 10], [20, 17, 15]])
    print(inverse)
