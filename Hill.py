from copy import deepcopy
from decimal import Decimal


def text_matrix(text: str, size: int):
    text = ''.join([x if x != ' ' else '' for x in text]).upper()
    if len(text) % size != 0:
        for _ in range(3 - len(text) % size):
            text += 'X'

    mat, row = [], []
    for i in range(len(text)):
        row.append(ord(text[i]) - 65)
        if len(row) >= size:
            mat.append(row)
            row = []
    print('text', mat)
    return mat


def key_matrix(key: str, size: int):
    required_length = pow(size, 2)
    key = ''.join(
        [x if x != ' ' else '' for x in key]
    ).upper()[0:required_length]

    loop = 0
    while len(key) < required_length:
        key += chr(loop + 65)
        loop += 1

    mat, row = [], []
    for i in range(len(key)):
        row.append(ord(key[i]) - 65)
        if len(row) >= size:
            mat.append(row)
            row = []
    print('key', mat)
    return mat


def matrix_multiply(text: list[list[int]], key: list[list[int]]):
    res_mat = []
    for t_row in text:
        res_row = [sum(t_row[i] * k_row[i] for i in range(len(key[0])))
                   for k_row in key]
        res_mat.append(res_row)
    return [[x % 26 for x in row] for row in res_mat]


def determinant(matrix: list[list[int]]):
    size = len(matrix)
    det = 0
    sign = 1
    # mat = deepcopy(matrix)

    if size == 2:
        return matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]

    for col in range(size):
        det += sign * matrix[0][col] * \
            determinant(matrix_minor(matrix, 0, col))
        sign *= -1

    return det


def matrix_minor(matrix: list[list[int]], row: int, col: int):
    size = len(matrix)
    if row < 0 or row >= size or col < 0 or col >= size:
        raise ValueError(f'Invalid index: row={row}, col={col}')

    minor = [[matrix[i][j] for j in range(size) if j != col]
             for i in range(size) if i != row]
    return minor


def cofactor(matrix: list[list[int]]):
    size = len(matrix)
    cofac = [[pow(-1, row + col + 2) * determinant(matrix_minor(matrix, row, col)) for col in range(size)]
             for row in range(size)]
    return cofac


def transpose(matrix: list[list[int]]):
    mat = deepcopy(matrix)
    size = len(matrix)
    for row in range(size):
        for col in range(row, size):
            mat[col][row], mat[row][col] = mat[row][col], mat[col][row]
    return mat


def invert_matrix(matrix: list[list[int]]):
    if len(matrix) != len(matrix[0]):
        raise Exception(f'Invalid matrix (not square), matrix: {matrix}')

    det = determinant(matrix)
    if det == 0:
        raise Exception(f'Matrix not invertible, det={det}')
    else:
        det %= 26
    inv_det = 0
    # det * inv_det = 27 + 26 * n
    # iterate n -> inv_det is int
    for n in range(100):
        res = (27 + 26 * n) / det
        if res.is_integer():
            inv_det = int(res)
            break
    mat = [[x % 26 * inv_det % 26 for x in row]
           for row in transpose(cofactor(matrix))]
    print('inverse key', mat)
    return mat


def find_coords(mat: list[list[int]], num: str):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x] == num:
                return {'x': x, 'y': y}


def encrypt(plainText: str, key: str, size: int):
    return ''.join([chr(x + 65) for row in matrix_multiply(text_matrix(plainText, size), key_matrix(key, size)) for x in row])


def decrypt(cipherText: str, key: str, size: int):
    return ''.join([chr(x + 65) for row in matrix_multiply(text_matrix(cipherText, size), invert_matrix(key_matrix(key, size))) for x in row])


if __name__ == '__main__':
    # this doesn't seems to work, inverted key is all zeros
    # plainText = 'help'
    # key = 'ddcf'
    # key_size = 2

    plainText = input('Plain text: ')
    key_en = input('Key: ')
    key_en_size = int(input('Size of key matrix: '))
    print(f'Encrypted: {encrypt(plainText, key_en, key_en_size)}')

    cipherText = input('Cipher text: ')
    key_de = input('Key: ')
    key_de_size = int(input('Size of key matrix: '))

    print(f'Decrypted: {decrypt(cipherText, key_de, key_de_size)}')
