from random import randint


def miller_rabin(n, k=100):
    """
    n = 2^r * d + 1
    n - 1 = 2^r * d
    d = (n - 1)/2^r
    """
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                continue

        return False

    return True


def gen_prime(n):
    if n % 2 == 0:
        n += 1

    while True:
        while not miller_rabin(n):
            n += 2

        if randint(0, 10) == 0:
            return n

        n += 2


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


assert lcm(60, 52) == 780


def gcd_ext(a, b):
    s = 0
    old_s = 1

    t = 1
    old_t = 0

    r = b
    old_r = a

    while r != 0:
        quotient = old_r // r
        old_r, r = r, old_r - quotient * r
        old_s, s = s, old_s - quotient * s
        old_t, t = t, old_t - quotient * t

    return (old_s, old_t), old_r, (t, s)


assert gcd_ext(240, 46)[1] == 2
assert gcd_ext(240, 46)[0] == (-9, 47)


def egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
    gcd = b
    return gcd, x, y


def mod_inv(a, n):
    return egcd(a, n)[1]


def bit_len(a):
    n = 0
    while a > 0:
        a >>= 1
        n += 1
    return n


def rsa_gen(bits):
    p = gen_prime(randint(2 ** (bits//2 - 1), 2 ** (bits//2 + 1)))
    q = gen_prime(randint(2 ** (bits//2 - 1), 2 ** (bits//2 + 1)))
    n = p * q
    print('bits', bit_len(n))

    carmichael = lcm(p - 1, q - 1)
    print('lambda', carmichael)

    e = carmichael - 2  # why -2?
    while e > 1 and gcd(e, carmichael) != 1:
        e -= 1

    assert 1 < e < carmichael
    assert gcd(e, carmichael) == 1

    print('e', e)

    d = mod_inv(e, carmichael)
    print('d', d)
    assert (e * d) % carmichael == 1

    return (n, e), (n, d)


def rsa_encrypt(m, key):
    return pow(m, key[1], key[0])


def rsa_decrypt(c, key):
    return pow(c, key[1], key[0])


pub, priv = rsa_gen(256)
print(pub, priv)

m = 65
print('m =', m)

c = rsa_encrypt(m, pub)
print('c =', c)

m = rsa_decrypt(c, priv)
print('m =', m)
