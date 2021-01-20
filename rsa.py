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
    return abs(a) // gcd(a, b) * abs(b)


assert lcm(60, 52) == 780


def mod_inv(a, n):
    t = 0
    new_t = 1
    r = n
    new_r = a

    while new_r != 0:
        q = r // new_r
        t, new_t = new_t, t - q * new_t
        r, new_r = new_r, r - q * new_r

    if r > 1:
        return None
    if t < 0:
        t = t + n

    return t


def bit_len(a):
    n = 0
    while a > 0:
        a >>= 1
        n += 1
    return n


def carmichael(p, q):
    return lcm(p - 1, q - 1)


def phi(p, q):
    return (p - 1) * (q - 1)


def rsa_gen(bits):
    bit_offset = randint(0, bits // 16)
    p = gen_prime(randint(2 ** (bits//2 - bit_offset), 2 ** (bits//2 - bit_offset + 1)))
    q = gen_prime(randint(2 ** (bits//2 + bit_offset), 2 ** (bits//2 + bit_offset + 1)))
    print('p =', p)
    print('q =', q)

    n = p * q
    print(bit_len(n), 'bits')

    totient = carmichael(p, q)
    # totient = phi(p, q)
    print('totient =', totient)

    e = 2
    while gcd(e, totient) != 1:
        e += 1

    assert 1 < e < totient
    assert gcd(e, totient) == 1

    print('e =', e)

    d = mod_inv(e, totient)
    print('d =', d)
    assert (e * d) % totient == 1

    return (n, e), (n, d)


def rsa(m, key):
    return pow(m, key[1], key[0])


def str2int(text):
    m = 0
    for c in reversed(text):
        m <<= 8
        m += ord(c)
    return m


def int2str(m):
    text = ''
    while m > 0:
        m, c = divmod(m, 256)
        text += chr(c)
    return text


pub, priv = rsa_gen(256)
print('pub =', pub)
print('priv =', priv)

m = 'Odpowiedzi do egzaminu'
print('m =', m)

c = rsa(str2int(m), pub)
print('c =', c)

m = int2str(rsa(c, priv))
print('m =', m)
