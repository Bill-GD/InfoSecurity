from math import sqrt


def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def generate_keys(p: int, q: int, e: int):
    if not is_prime(p) or not is_prime(q):
        raise Exception(
            f'p and q must be prime, p: {is_prime(p)}, q: {is_prime(q)}')
    n = p * q
    phi = (p - 1) * (q - 1)
    if gcd(phi, e) != 1:
        raise Exception(f'Invalid e value, gcd(phi, e) = {gcd(phi, e)} != 1')
    d = int(phi / e)
    while (d * e) % phi != 1:
        d += 1
    return {'public': {'n': n, 'e': e}, 'private': {'n': n, 'd': d}}


def text_to_decimal(text: str):
    res = []
    for c in text:
        if ord(c.upper()) < 65 or ord(c.upper()) > 90:
            res.append(52)
            continue
        res.append(ord(c.upper()) - 65 if c.islower()
                   else ord(c) - 65 + 26)
    return res


def decimal_to_text(decimals: list[int]):
    res = ''
    for i in decimals:
        if i == 52:
            res += ' '
            continue
        res += chr(i + 97) if i < 26 else chr(i - 26 + 65)
    return res


def encrypt(text: str, e: int, n: int):
    # p^e % n
    return ' '.join([str(pow(char, e) % n) for char in text_to_decimal(text)])


def decrypt(cipher: str, d: int, n: int):
    # c^d % n
    return decimal_to_text([pow(int(c), d) % n for c in cipher.split(' ')])


if __name__ == "__main__":
    keys = generate_keys(73, 157, 7)
    print(keys)
    plain = "How are you"

    encrypted = encrypt(plain, keys['public']['e'], keys['public']['n'])
    print(encrypted)
    print(decrypt(encrypted, keys['private']['d'], keys['private']['n']))
