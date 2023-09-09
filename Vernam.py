def get_text_binary(text: str):
    return list(map(get_char_binary, list(text.upper())))


def get_char_binary(char: str):
    binary = bin(ord(char) - ord('A')).split('b')[1]
    while len(binary) < 8:
        binary = '0' + binary
    return binary


def xor(a: str, b: str):
    res = ''
    for i in range(len(a)):
        res += str(int(a[i]) ^ int(b[i]))
    return res


def encrypt(plainText: str, key: str):
    if len(plainText) != len(key):
        raise Exception('Invalid key (length mismatch)')

    res = list(map(lambda x, y: xor(x, y),
                   get_text_binary(plainText), get_text_binary(key)))
    print(res)
    print(list(map(lambda x: int(x, 2), res)))
    return ''.join(list(map(lambda x: chr(int(x, 2) % 26 + ord('A')), res)))


def decrypt(cipherText: str, key: str):
    if len(cipherText) != len(key):
        raise Exception('Invalid key (length mismatch)')

    res = list(map(lambda x, y: xor(x, y),
                   get_text_binary(cipherText), get_text_binary(key)))
    print(res)
    print(list(map(lambda x: int(x, 2), res)))
    return ''.join(list(map(lambda x: chr(int(x, 2) % 26 + ord('A')), res)))


if __name__ == '__main__':
    plainText = 'L'
    key = 'H'
    
    # seems to work most of the time
    # if encoded binary is > 30 -> mod 26 -> original binary is lost -> different decoded message
    # e.g: L --V(encode)--> E --V(decode)--> R (wrong)
    # e.g: L --H(encode)--> M --H(decode)--> L (correct)
    
    # another encryption technique (dcode.fr & some other): zero-index char -> add (p + k) -> mod % 26 -> c (similar to vigenere)

    print(get_text_binary(plainText))
    print(get_text_binary(key))
    cipherText = encrypt(plainText, key)
    print(f'{plainText} --{key}--> {cipherText}')

    print(get_text_binary(cipherText))
    print(get_text_binary(key))
    print(f'{cipherText} --{key}--> {decrypt(cipherText, key)}')

    # print((ord('R') - ord('A')) ^ (ord('R') - ord('A')))
    # print(chr(((ord('R') - ord('A')) ^ (ord('R') - ord('A'))) + ord('A')))
