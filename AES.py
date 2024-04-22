from copy import deepcopy

r_con = ['01', '02', '04', '08', '10', '20', '40', '80', '1b', '36']

s_box_table = [
    ['63', '7c', '77', '7b', 'f2', '6b', '6f', 'c5',
        '30', '01', '67', '2b', 'fe', 'd7', 'ab', '76'],
    ['ca', '82', 'c9', '7d', 'fa', '59', '47', 'f0',
        'ad', 'd4', 'a2', 'af', '9c', 'a4', '72', 'c0'],
    ['b7', 'fd', '93', '26', '36', '3f', 'f7', 'cc',
        '34', 'a5', 'e5', 'f1', '71', 'd8', '31', '15'],
    ['04', 'c7', '23', 'c3', '18', '96', '05', '9a',
        '07', '12', '80', 'e2', 'eb', '27', 'b2', '75'],
    ['09', '83', '2c', '1a', '1b', '6e', '5a', 'a0',
        '52', '3b', 'd6', 'b3', '29', 'e3', '2f', '84'],
    ['53', 'd1', '00', 'ed', '20', 'fc', 'b1', '5b',
        '6a', 'cb', 'be', '39', '4a', '4c', '58', 'cf'],
    ['d0', 'ef', 'aa', 'fb', '43', '4d', '33', '85',
        '45', 'f9', '02', '7f', '50', '3c', '9f', 'a8'],
    ['51', 'a3', '40', '8f', '92', '9d', '38', 'f5',
        'bc', 'b6', 'da', '21', '10', 'ff', 'f3', 'd2'],
    ['cd', '0c', '13', 'ec', '5f', '97', '44', '17',
        'c4', 'a7', '7e', '3d', '64', '5d', '19', '73'],
    ['60', '81', '4f', 'dc', '22', '2a', '90', '88',
        '46', 'ee', 'b8', '14', 'de', '5e', '0b', 'db'],
    ['e0', '32', '3a', '0a', '49', '06', '24', '5c',
        'c2', 'd3', 'ac', '62', '91', '95', 'e4', '79'],
    ['e7', 'c8', '37', '6d', '8d', 'd5', '4e', 'a9',
        '6c', '56', 'f4', 'ea', '65', '7a', 'ae', '08'],
    ['ba', '78', '25', '2e', '1c', 'a6', 'b4', 'c6',
        'e8', 'dd', '74', '1f', '4b', 'bd', '8b', '8a'],
    ['70', '3e', 'b5', '66', '48', '03', 'f6', '0e',
        '61', '35', '57', 'b9', '86', 'c1', '1d', '9e'],
    ['e1', 'f8', '98', '11', '69', 'd9', '8e', '94',
        '9b', '1e', '87', 'e9', 'ce', '55', '28', 'df'],
    ['8c', 'a1', '89', '0d', 'bf', 'e6', '42', '68',
        '41', '99', '2d', '0f', 'b0', '54', 'bb', '16']
]
inverse_s_box_table = [
    ['52', '09', '6a', 'd5', '30', '36', 'a5', '38',
        'bf', '40', 'a3', '9e', '81', 'f3', 'd7', 'fb'],
    ['7c', 'e3', '39', '82', '9b', '2f', 'ff', '87',
        '34', '8e', '43', '44', 'c4', 'de', 'e9', 'cb'],
    ['54', '7b', '94', '32', 'a6', 'c2', '23', '3d',
        'ee', '4c', '95', '0b', '42', 'fa', 'c3', '4e'],
    ['08', '2e', 'a1', '66', '28', 'd9', '24', 'b2',
        '76', '5b', 'a2', '49', '6d', '8b', 'd1', '25'],
    ['72', 'f8', 'f6', '64', '86', '68', '98', '16',
        'd4', 'a4', '5c', 'cc', '5d', '65', 'b6', '92'],
    ['6c', '70', '48', '50', 'fd', 'ed', 'b9', 'da',
        '5e', '15', '46', '57', 'a7', '8d', '9d', '84'],
    ['90', 'd8', 'ab', '00', '8c', 'bc', 'd3', '0a',
        'f7', 'e4', '58', '05', 'b8', 'b3', '45', '06'],
    ['d0', '2c', '1e', '8f', 'ca', '3f', '0f', '02',
        'c1', 'af', 'bd', '03', '01', '13', '8a', '6b'],
    ['3a', '91', '11', '41', '4f', '67', 'dc', 'ea',
        '97', 'f2', 'cf', 'ce', 'f0', 'b4', 'e6', '73'],
    ['96', 'ac', '74', '22', 'e7', 'ad', '35', '85',
        'e2', 'f9', '37', 'e8', '1c', '75', 'df', '6e'],
    ['47', 'f1', '1a', '71', '1d', '29', 'c5', '89',
        '6f', 'b7', '62', '0e', 'aa', '18', 'be', '1b'],
    ['fc', '56', '3e', '4b', 'c6', 'd2', '79', '20',
        '9a', 'db', 'c0', 'fe', '78', 'cd', '5a', 'f4'],
    ['1f', 'dd', 'a8', '33', '88', '07', 'c7', '31',
        'b1', '12', '10', '59', '27', '80', 'ec', '5f'],
    ['60', '51', '7f', 'a9', '19', 'b5', '4a', '0d',
        '2d', 'e5', '7a', '9f', '93', 'c9', '9c', 'ef'],
    ['a0', 'e0', '3b', '4d', 'ae', '2a', 'f5', 'b0',
        'c8', 'eb', 'bb', '3c', '83', '53', '99', '61'],
    ['17', '2b', '04', '7e', 'ba', '77', 'd6', '26',
        'e1', '69', '14', '63', '55', '21', '0c', '7d']
]

mix_column_mat = [
    ['02', '03', '01', '01'],
    ['01', '02', '03', '01'],
    ['01', '01', '02', '03'],
    ['03', '01', '01', '02']
]
inverse_mix_column_mat = [
    ['0e', '0b', '0d', '09'],
    ['09', '0e', '0b', '0d'],
    ['0d', '09', '0e', '0b'],
    ['0b', '0d', '09', '0e']
]
# '       01010111'
# '       10000011'

# '       01010111'
# '      010101110'
# '010101110000000'

# '010101101111001'
# '000000100011011'

# '000000011000001'
[]

# 13 11 9 8 6 5 4 3 0  |  8 4 3 1 0
# 13    9 8 6 5        |  5 3
#    11         4 3 0
#    11   7 6   4 3
#         7 6       0


def multiply_binary_poly(bin1: str, bin2: str):
    bin1_list, bin2_list = list(bin1)[::-1], list(bin2)[::-1]
    result = ['0']*16

    for bit1 in range(len(bin1)):
        if bin1_list[bit1] == '0':
            continue
        for bit2 in range(len(bin2)):
            if bin2_list[bit2] == '0':
                continue
            result[bit1 + bit2] = '1' if bin1_list[bit1] == '1' and bin2_list[bit2] == '1' and result[bit1 + bit2] == '0' else '0'
    return ''.join(result[::-1])


def divide_binary_poly(bin1: str, bin2: str):
    bin1_list, bin2_list = list(bin1)[::-1], list(bin2)[::-1]
    result = ['0']*len(bin2)
    max_expo_2 = ''.join(bin2_list).rfind('1')
    # while max expo of 1st is not smaller than max expo of 2nd
    while ''.join(bin1_list).rfind('1') >= max_expo_2:
        max_expo_1 = ''.join(bin1_list).rfind('1')
        res_expo = max_expo_1 - max_expo_2
        result[res_expo] = '1'
        for bit2 in range(len(bin2)):
            if bin2_list[bit2] == '0':
                continue
            bin1_list[bit2 + res_expo] = '0' if bin1_list[bit2 +
                                                          res_expo] == '1' else '1'
    return ''.join(bin1_list[0:len(bin2)][::-1])


def galois(hex_list1: list[str], hex_list2: list[str]):
    result = ''
    for i in range(len(hex_list1)):
        mult = multiply_binary_poly(
            bin(int(hex_list1[i], 16))[2:].zfill(8), bin(int(hex_list2[i], 16))[2:].zfill(8))
        div = divide_binary_poly(mult, '100011011')
        result = div if result == '' else bin(int(result, 2) ^ int(div, 2))
    return hex(int(result, 2))[2:].zfill(2)


def mix_column(shifted_row: list[list[str]], mix_mat: list[list[str]]):
    shifted_row = transpose(shifted_row)
    result_mat = []
    for row1 in mix_mat:
        result_row = []
        for row2 in shifted_row:
            result_row.append(galois(row1, row2))
        result_mat.append(result_row)
    return result_mat


def plain_matrix(plain_hex: str):
    length_factor = int(len(plain_hex) / 16)
    return transpose([[plain_hex[i:i+length_factor] for i in range(row, row + 8, length_factor)] for row in range(0, len(plain_hex), 8)])


def round_zero_key(key_hex: str):
    length_factor = int(len(plain_hex) / 16)
    return [[key_hex[i:i+length_factor] for i in range(row, row + 8, length_factor)] for row in range(0, len(key_hex), 8)]


def xor(key1: list[str], key2: list[str]):
    return [hex(int(key1[i], 16) ^ int(key2[i], 16))[2:].zfill(2) for i in range(len(key1))]


def rotate_key(key: list[str], round: int = 1):
    return key[round:] + key[:round]


def inverse_rotate_key(key: list[str], round: int = 1):
    return key[len(key) - round:] + key[:len(key) - round]


def process_s_box(key: list[str]):
    coords = [[int(char, 16) for char in hex] for hex in key]
    return [s_box_table[row][col] for row, col in coords]


def inverse_s_box(key: list[str]):
    coords = [[int(char, 16) for char in hex] for hex in key]
    return [inverse_s_box_table[row][col] for row, col in coords]


def other_round_keys(zero_round_key: list[list[str]]):
    all_round_keys = []
    for i in range(10):
        w0, w1, w2, w3 = zero_round_key
        x1 = rotate_key(w3)
        y1 = process_s_box(x1)
        z1 = [hex(int(y1[0], 16) ^ int(r_con[i], 16))[2:]] + y1[1:]
        w4 = xor(w0, z1)
        w5 = xor(w4, w1)
        w6 = xor(w5, w2)
        w7 = xor(w6, w3)
        next_round_key = [w4, w5, w6, w7]
        all_round_keys.append(next_round_key)
        zero_round_key = next_round_key
    return [transpose(round_key) for round_key in all_round_keys]


def transpose(matrix: list[list[int]]):
    mat, size = deepcopy(matrix), len(matrix)
    for row in range(size):
        for col in range(row, size):
            mat[col][row], mat[row][col] = mat[row][col], mat[col][row]
    return mat


def add_round_key(plain: list[list[str]], round_key: list[list[str]]):
    return [xor(plain[row], round_key[row]) for row in range(len(plain))]


def encode_round(plain: list[list[str]], key: list[list[str]], round: int):
    if round == 0:
        return add_round_key(plain, key)
    elif round == 10:
        subbytes = [process_s_box(row) for row in plain]
        shiftrow = [rotate_key(subbytes[row], row)
                    for row in range(len(subbytes))]
        add_roundkey = add_round_key(shiftrow, key)
        return add_roundkey
    else:
        subbytes = [process_s_box(row) for row in plain]
        shiftrow = [rotate_key(subbytes[row], row)
                    for row in range(len(subbytes))]
        mixcol = mix_column(shiftrow, mix_column_mat)
        add_roundkey = add_round_key(mixcol, key)
        return add_roundkey


def encrypt(plain_hex: str, key_hex: str):
    plain_mat = plain_matrix(plain_hex)
    round_zero = round_zero_key(key_hex)
    print('round zero:', round_zero)

    round_keys = [transpose(round_zero)] + other_round_keys(round_zero)
    prev = plain_mat
    for i in range(11):
        c = encode_round(prev, round_keys[i], i)
        # print(f'round {i}: {c}')
        # print()
        prev = c
    return ''.join([hex for row in transpose(prev) for hex in row])


def decode_round(cipher: list[list[str]], key: list[list[str]], round: int):
    # print('decode_round:', round)
    # print('cipher:', cipher)
    if round == 0:
        return add_round_key(cipher, key)
    elif round == 10:
        inv_shiftrow = [inverse_rotate_key(cipher[row], row)
                        for row in range(len(cipher))]
        inv_subbytes = [inverse_s_box(row) for row in inv_shiftrow]
        add_roundkey = add_round_key(inv_subbytes, key)
        return add_roundkey
    else:
        inv_shiftrow = [inverse_rotate_key(cipher[row], row)
                        for row in range(len(cipher))]
        inv_subbytes = [inverse_s_box(row) for row in inv_shiftrow]
        add_roundkey = add_round_key(inv_subbytes, key)
        inv_mixcol = mix_column(add_roundkey, inverse_mix_column_mat)
        return inv_mixcol


def decrypt(cipher_hex: str, key_hex: str):
    cipher_mat = plain_matrix(cipher_hex)
    round_zero = round_zero_key(key_hex)
    round_keys = [transpose(round_zero)] + other_round_keys(round_zero)
    round_keys.reverse()

    prev = cipher_mat
    for i in range(11):
        c = decode_round(prev, round_keys[i], i)
        prev = c
    return ''.join([hex for row in transpose(prev) for hex in row])


def check_hex_string(hex: str):
    for digit in hex:
        if digit.isdigit():
            continue
        if ord(str(digit.upper())) < 65 or ord(str(digit.upper())) > 70:
            raise Exception(f'Invalid hex value: {digit}')


if __name__ == "__main__":
    # plain_hex = '0123456789abcdeffedcba9876543210'
    # plain_hex = '54776F204F6E65204E696E652054776F'
    # key_hex = '0f1571c947d9e8590cb7add6af7f6798'
    # key_hex = '5468617473206d79204b756e67204675'

    plain_hex = input('Input plain: ')
    check_hex_string(plain_hex)

    key_hex = input('Key: ')
    check_hex_string(key_hex)

    print('plain:', plain_hex)
    print('key:', key_hex)

    encrypted = encrypt(plain_hex, key_hex)
    print('encrypted:', encrypted)
    print('decrypted:', decrypt(encrypted, key_hex))
