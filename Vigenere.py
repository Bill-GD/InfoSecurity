def encrypt(plainText: str, key: str):
    key, plainText = key.upper(), plainText.upper()
    c, k = '', ''
    for i in range(0, len(plainText)):
        k += key[i % len(key)]
    for i in range(0, len(plainText)):
        c += chr((ord(plainText[i]) + ord(k[i]) - 130) % 26 + 65)
    return c

def decrypt(cipherText: str, key: str):
    key, cipherText = key.upper(), cipherText.upper()
    p, k = '', ''
    for i in range(0, len(cipherText)):
        k += key[i % len(key)]
    for i in range(0, len(cipherText)):
        p += chr((ord(cipherText[i]) - ord(k[i]) - 130) % 26 + 65)
    return p

if __name__ == '__main__':
    key = input('Enter key: ')
    cipher = encrypt(input('Enter plain text: '), key)
    print(cipher)
    print(decrypt(cipher, key))