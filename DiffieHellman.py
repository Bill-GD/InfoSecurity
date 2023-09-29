from math import sqrt
import random


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
    coprimes, num_coprimes = get_coprimes(n), num_of_coprimes(n)
    if p > n or p not in coprimes:
        raise Exception('p is invalid')
    for i in range(1, num_coprimes + 1):
        if (p ** i) % n == 1:
            return i == num_coprimes
    return False


def find_all_primitive_roots(n: int):
    res = []
    for i in get_coprimes(n):
        if is_primitive_root(i, n):
            res.append(i)
    return res


def generate_keys(p: int, xa: int, xb: int):
    if not is_prime(p):
        raise Exception(f'p must be prime, p: {p}')
    if xa > p or xb > p:
        raise Exception(f'xa ({xa}) and xb ({xb}) has to be less than p ({p})')

    primitive_roots = find_all_primitive_roots(p)
    a = primitive_roots[random.randint(0, len(primitive_roots) - 1)]
    
    ya, yb = (a ** xa) % p, (a ** xb) % p
    key_a, key_b = (yb ** xa) % p, (ya ** xb) % p
    if key_a != key_b:
        raise Exception(f'Mismatch key, {key_a} != {key_b}')
    return {'public': {'a': ya, 'b': yb}, 'shared_private': key_a}


if __name__ == "__main__":
    print(generate_keys(353, 97, 233))
