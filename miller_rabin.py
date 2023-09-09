import random


def miller_rabin(n):
    if n <= 3:
        raise Exception('n should be greater than 3.')
    if n % 2 == 0:
        return False

    # Find u odd such that n-1 = 2^k * u
    u = n - 1
    k = 0
    while (u % 2 == 0):
        u //= 2
        k += 1

    # Let a be randomly chosen from {2,...,n − 2};
    a = random.randint(2, n-2)
    # b = a^u mod n
    b = pow(a, u, n)
    if b == 1 or b == n-1:
        return True

    for _ in range(1, k-1):
        b = (b*b) % n

        if b == n-1:
            return True
        if b == 1:
            return False
    return False


if __name__ == '__main__':
    print(miller_rabin(int(input("A number: "))))
