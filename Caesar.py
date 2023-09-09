def decrypt(cipherText: str, key: int):
    cipherText = cipherText.upper()
    p = ''
    for i in range(0, len(cipherText)):
        if (ord(cipherText[i]) == 32):
            p += ' '
            continue
        p += chr((ord(cipherText[i]) - 65 - key) % 26 + 65)
    return f'c={cipherText} -> k={key}, p={p}'


def brute_force(cipherText: str):
    if cipherText.__len__() <= 0:
        return
    for key in range(26):
        print(decrypt(cipherText, key))


def encrypt(plainText: str, key: int):
    plainText = plainText.upper()
    c = ''
    for i in range(0, len(plainText)):
        if (ord(plainText[i]) == 32):
            c += ' '
            continue
        c += chr((ord(plainText[i]) - 65 + key) % 26 + 65)
    return f'p={plainText} -> k={key}, c={c}'


if __name__ == '__main__':
    print('Brute force Caesar')
    # encrypt(input('Enter plain text: '), int(input('Enter key: ')))
    brute_force('syfxuh')
    print()
    print(decrypt('syfxuh', 16))
    print(decrypt('TRVJRI TZGYVIJ RIV HLZKV VRJP KF TIRTB', 17))
    print(encrypt('CAESAR CIPHERS ARE QUITE EASY TO CRACK', 17))
    # brute_force('RWJCVIDXAPRWXTCHXRDCVPC')
