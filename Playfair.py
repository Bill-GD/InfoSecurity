def generate_key(key: str):
    if contains(key, 'I') and contains(key, 'J'):
        return 'Invalid key'
    
    key = key.upper()
    k = []
    for i in key:
        k.append(i)
    for i in range(65, 91):
        # handles I & J
        if (chr(i) == 'I' and contains(k, 'J')) or (chr(i) == 'J' and contains(k, 'I')):
            continue
        # adds the rest of the alphabet
        if not contains(k, chr(i)):
            k.append(chr(i))
    # generate table
    table, key_block = [], []
    for i in range(len(k)):
        key_block.append(k[i])
        if len(key_block) == 5:
            table.append(key_block)
            key_block = []
    return table


def text_digraphs(plainText: str):
    pairs, pair = [], []
    p = plainText.upper()
    for i in range(len(p)):
        if i % 2 == 0:
            pair.append(p[i])
        else:
            if p[i] == p[i - 1] and len(pair) == 1:
                pair.append('X')
                pairs.append(pair)
                pair = []
            pair.append(p[i])
        if len(pair) == 2:
            pairs.append(pair)
            pair = []
        if i == len(p) - 1 and len(pair) == 1:
            pair.append('Z')
            pairs.append(pair)
    return pairs


def contains(text: list | str, char: str):
    for i in text:
        if i.upper() == char.upper():
            return True
    return False


def find_coords(mat: list[list], char: str):
    for y in range(len(mat)):
        for x in range(len(mat[y])):
            if mat[y][x].upper() == char.upper():
                return {'x': x, 'y': y}


def encrypt(plainText: str, key: str):
    table, digraphs = generate_key(key), text_digraphs(plainText)
    # substitute using digraphs
    for pair in digraphs:
        coords = {
            'first': find_coords(table, pair[0]),
            'second': find_coords(table, pair[1]),
        }
        # same column
        if coords['first']['x'] == coords['second']['x']:
            pair[0] = table[(coords['first']['y'] + 1) %
                            5][coords['first']['x']]
            pair[1] = table[(coords['second']['y'] + 1) %
                            5][coords['second']['x']]
        # same row
        elif coords['first']['y'] == coords['second']['y']:
            pair[0] = table[coords['first']['y']
                            ][(coords['first']['x'] + 1) % 5]
            pair[1] = table[coords['second']['y']
                            ][(coords['second']['x'] + 1) % 5]
        # rect
        else:
            pair[0] = table[coords['first']['y']][coords['second']['x']]
            pair[1] = table[coords['second']['y']][coords['first']['x']]
    c = ''
    for pair in digraphs:
        c += ''.join(pair)
    return c


def decrypt(cipherText: str, key: str):
    table, digraphs = generate_key(key), text_digraphs(cipherText)
    # substitute using digraphs
    for pair in digraphs:
        coords = {
            'first': find_coords(table, pair[0]),
            'second': find_coords(table, pair[1]),
        }
        # same column
        if coords['first']['x'] == coords['second']['x']:
            pair[0] = table[(coords['first']['y'] + 4) %
                            5][coords['first']['x']]
            pair[1] = table[(coords['second']['y'] + 4) %
                            5][coords['second']['x']]
        # same row
        elif coords['first']['y'] == coords['second']['y']:
            pair[0] = table[coords['first']['y']
                            ][(coords['first']['x'] + 4) % 5]
            pair[1] = table[coords['second']['y']
                            ][(coords['second']['x'] + 4) % 5]
        # rect
        else:
            pair[0] = table[coords['first']['y']][coords['second']['x']]
            pair[1] = table[coords['second']['y']][coords['first']['x']]
    c = ''
    for pair in digraphs:
        c += ''.join(pair)
    return c


if __name__ == '__main__':
    print('Duplicate: uses X')
    print('Fill end of string: uses Z')

    plainText = input('Plain text: ')
    key = input('Key: ')
    print(encrypt(plainText, key))

    cipherText = input('Cipher text: ')
    key = input('Key: ')
    print(decrypt(cipherText, key))
