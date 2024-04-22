initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
                60, 52, 44, 36, 28, 20, 12, 4,
                62, 54, 46, 38, 30, 22, 14, 6,
                64, 56, 48, 40, 32, 24, 16, 8,
                57, 49, 41, 33, 25, 17, 9, 1,
                59, 51, 43, 35, 27, 19, 11, 3,
                61, 53, 45, 37, 29, 21, 13, 5,
                63, 55, 47, 39, 31, 23, 15, 7]

final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

compress_perm_56 = [57, 49, 41, 33, 25, 17, 9,
                    1, 58, 50, 42, 34, 26, 18,
                    10, 2, 59, 51, 43, 35, 27,
                    19, 11, 3, 60, 52, 44, 36,
                    63, 55, 47, 39, 31, 23, 15,
                    7, 62, 54, 46, 38, 30, 22,
                    14, 6, 61, 53, 45, 37, 29,
                    21, 13, 5, 28, 20, 12, 4]

compress_perm_48 = [14, 17, 11, 24, 1, 5, 3, 28,
                    15, 6, 21, 10, 23, 19, 12, 4,
                    26, 8, 16, 7, 27, 20, 13, 2,
                    41, 52, 31, 37, 47, 55, 30, 40,
                    51, 45, 33, 48, 44, 49, 39, 56,
                    34, 53, 46, 42, 50, 36, 29, 32]

expand_perm_48 = [32, 1, 2, 3, 4, 4,
                  4, 5, 6, 7, 8, 9,
                  8, 9, 10, 11, 12, 13,
                  12, 13, 14, 15, 16, 17,
                  16, 17, 18, 19, 20, 21,
                  20, 21, 22, 23, 24, 25,
                  24, 25, 26, 27, 28, 29,
                  28, 29, 30, 31, 32, 1]

s_boxes = [
    # S-box 1
    [
        [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
        [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
        [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
        [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
    ],
    # S-box 2
    [
        [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
        [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
        [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
        [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
    ],
    # S-box 3
    [
        [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
        [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
        [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
        [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
    ],
    # S-box 4
    [
        [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
        [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
        [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
        [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
    ],
    # S-box 5
    [
        [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
        [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
        [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
        [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
    ],
    # S-box 6
    [
        [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
        [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
        [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
        [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
    ],
    # S-box 7
    [
        [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
        [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
        [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
        [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
    ],
    # S-box 8
    [
        [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
        [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
        [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
        [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
    ]
]

p_box_perm = [
    16, 7, 20, 21, 29, 12, 28, 17,
    1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9,
    19, 13, 30, 6, 22, 11, 4, 25
]


def hex_key_to_binary(key: str):
    return bin(int(key, 16))[2:].zfill(64)


def permute(binary: str, permutation: list[int], length: int):
    return ''.join([binary[permutation[i] - 1] for i in range(length)])


def rotate_string(str: str, round: int):
    return str[round:] + str[:round]


def round_keys(key_hex: str):
    key_bin = bin(int(key_hex, 16))[2:].zfill(64)
    key = permute(key_bin, compress_perm_56, 56)
    keys = []
    left, right = key[:28], key[28:]
    for i in range(1, 17):
        left = rotate_string(left, 1 if i in [1, 2, 9, 16] else 2)
        right = rotate_string(right, 1 if i in [1, 2, 9, 16] else 2)

        # print(f'left: {left} -> hex: {hex(int(left, 2))[2:]}')
        # print(f'right: {right} -> hex: {hex(int(right, 2))[2:]}')

        key = permute(left + right, compress_perm_48, 48)
        keys.append(key)
    return keys


def process_s_box(text: str):
    s_box_groups = []
    group = ''
    for bit in text:
        group += bit
        if len(group) == 6:
            s_box_groups.append(
                [int(group[0] + group[5], 2), int(group[1:5], 2)])
            group = ''
    # for i in range(0, len(text), 6):
    #     print(text[i:i+6], end=' ')
    # print()
    # print(s_box_groups)
    # print([s_boxes[i][s_box_groups[i][0]][s_box_groups[i][1]]
    #       for i in range(len(s_box_groups))])
    return ''.join([bin(s_boxes[i][s_box_groups[i][0]][s_box_groups[i][1]])[2:].zfill(4) for i in range(len(s_box_groups))])


def xor(a: str, b: str):
    return bin(int(a, 2) ^ int(b, 2))[2:].zfill(len(a))


def process_round(text_bin: str, key_hex: str, round: int):
    round_key = round_keys(key_hex)[round - 1]
    # print('round key hex:', hex(int(round_key, 2))[2:])

    text_left, text_right = text_bin[:32], text_bin[32:]
    # print('left:', text_left)
    # print('right:', text_right)
    # print('left:', hex(int(text_left, 2))[2:])
    # print('right:', hex(int(text_right, 2))[2:])

    expanded_right = permute(text_right, expand_perm_48, 48)
    # print('expanded right:', expanded_right)

    xor_res = xor(expanded_right, round_key)
    # print(expanded_right)
    # print(round_key)
    # print('xor right:', xor_res)
    # print(xor_res)

    s_boxed = process_s_box(xor_res)
    # print('s boxed  :', s_boxed)

    p_boxed = permute(s_boxed, p_box_perm, 32)
    # print('p boxed  :', p_boxed)
    # print('left     :', text_left)

    text_left_new, text_right_new = text_right, xor(text_left, p_boxed)
    # print('left new:', hex(int(text_left_new, 2))[2:])
    # print('right new:', text_right_new)
    # print('right new:', hex(int(text_right_new, 2))[2:])

    return text_left_new, text_right_new


def encrypt(plain_hex: str, key_hex: str):
    text = permute(bin(int(plain_hex, 16))[2:].zfill(64), initial_perm, 64)
    for i in range(16):
        # print('round:', i + 1)
        # print(hex(int(text, 2))[2:])

        round = process_round(text, key_hex, i + 1)
        # print('right    :', round[1])

        text = ''.join(round)
        # print('round res:', hex(int(text, 2))[2:])
        # print()
    print()
    return permute(text, final_perm, 64)


def decrypt(code_hex: str, key_hex: str):
    text = permute(bin(int(code_hex, 16))[2:].zfill(64), initial_perm, 64)
    for i in range(16):
        # print('round:', i + 1)
        # print(hex(int(text, 2))[2:])

        round = process_round(text, key_hex, i + 1)
        # print('right    :', round[1])

        text = ''.join(round)
        # print('round res:', hex(int(text, 2))[2:])
        # print()
    # print()
    return permute(text, final_perm, 64)


if __name__ == '__main__':
    key_hex = '0f1571c947d9e859'

    plain_hex = '02468aceeca86420'
    plain_bin = bin(int(plain_hex, 16))[2:].zfill(64)
    # print(plain_bin)
    # print('->', plain_bin[32:], '->',
    #       permute(plain_bin[32:], expand_perm_48, 48))

    print(hex(int(encrypt(plain_hex, key_hex), 2))[2:])
    print(hex(int(decrypt('95775d82dccdf75', key_hex), 2))[2:])
    # print(hex(int(permute(bin(int('7070e2fda0f7bb0b', 16))[2:].zfill(64), final_perm, 64), 2))[2:])
    # print(hex(int(permute(bin(int('2b2e210b79fd75ad', 16))[2:].zfill(64), final_perm, 64), 2))[2:])
