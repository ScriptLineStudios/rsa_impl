import random

def get_random_number(num_bits):
    return random.randrange(0, 1 << num_bits) | ((1 << num_bits) | 1)

def is_prime(n):
    if n % 2 == 0:
        return False

    a = random.randrange(2, n - 1)
    s = 0
    d = n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    assert(d % 2 != 0 and 2 ** s * d == n - 1)

    alpha = pow(a, d, n)
    if alpha != 1 or alpha == n - 1:
        return False

    for r in range(s):
        beta = pow(alpha, 2, n)
        if beta == n - 1:
            return False
    
    return True

def get_prime(num_bits=256):
    while True:
        num = get_random_number(num_bits)
        if is_prime(num):
            return num

print(get_prime(512))