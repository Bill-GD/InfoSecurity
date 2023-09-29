from math import sqrt


def is_prime(n: int) -> bool:
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def gcd(a, b):
    while (b != 0):
        r = a % b
        a = b
        b = r
    return a


def get_coprimes(a: int):
    res = []
    for i in range(1, a):
        if gcd(a, i) == 1:
            res.append(i)
    return res


def get_prime_factors(n: int):
    if n < 2:
        raise Exception('n must be greater than 2')
    res = []
    for i in range(2, n + 1):
        if is_prime(i):
            if n % i == 0:
                res.append(i)
            while n % i == 0:
                n /= i
    return res


def num_of_coprimes(n: int):
    res = n
    prime_factors = get_prime_factors(n)
    for i in prime_factors:
        res *= (1 - 1 / i)
    return int(res)


def is_primitive_root(p: int, n: int):
    if p > n:
        raise Exception('p has to be less than n')
    prime_factors, num_coprimes = get_prime_factors(n), num_of_coprimes(n)
    for i in prime_factors:
        if (p ** (num_coprimes / i)) % n == 1:
            return False
    return True


def generate_keys(q: int, a: int, xa: int):
    if not is_prime(q):
        raise Exception(f'q must be prime, q: {q}')
    if not is_primitive_root(a, q):
        raise Exception(f'a ({a}) is not primitive root of q ({q})')
    if xa >= q - 1:
        raise Exception(f'xa ({xa}) has to be less than q - 1 ({q - 1})')

    ya = (a ** xa) % q
    return {'public': {'q': q, 'a': a, 'ya': ya}, 'private': xa}


def encrypt(p: int, q: int, a: int, xa: int) -> tuple[int, int]:
    if p >= q:
        raise Exception(f'p ({p}) must be less than q ({q})')
    keys = generate_keys(q, a, xa)
    k = 6
    onetime_k = (keys['public']['ya'] ** k) % q
    c1, c2 = (a ** k) % q, (onetime_k * p) % q
    return c1, c2


def decrypt(c: tuple[int, int], q: int, xa: int):
    c1, c2 = c
    k = (c1 ** xa) % q
    # extended euclidean algorithm (kinda)
    # (a * a^-1) mod b == 1 -> get a^-1 (mod inverse)
    inv_k = 0
    while (k * inv_k) % q != 1:
        inv_k += 1

    return (c2 * inv_k) % q


if __name__ == "__main__":
    q, a = 353, 3
    xa = 10
    print(generate_keys(q, a, xa))
    encrypted = encrypt(352, q, a, xa)
    print('encrypted:', encrypted)
    print('decrypted:', decrypt(encrypted, q, xa))
