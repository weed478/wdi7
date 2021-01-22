import blowfish
from blowfish import bit_mask
from random import randint


def cbc_encrypt(prev, x, algo):
    return algo(prev ^ x)


def cbc_decrypt(prev, x, algo):
    return prev ^ algo(x)


def encrypt(blocks, algo):
    for i in range(1, len(blocks)):
        blocks[i] = cbc_encrypt(blocks[i - 1], blocks[i], algo)


def decrypt(blocks, algo):
    for i in range(len(blocks) - 1, 0, -1):
        blocks[i] = cbc_decrypt(blocks[i - 1], blocks[i], algo)


class Encryptor:
    def __init__(self, algo, iv):
        self.algo = algo
        self.prev = iv

    def next(self, block):
        self.prev = cbc_encrypt(self.prev, block, self.algo)
        return self.prev


class Decrypter:
    def __init__(self, algo):
        self.algo = algo
        self.prev = 0

    def next(self, block):
        p = cbc_decrypt(self.prev, block, self.algo)
        self.prev = block
        return p


def generate_iv(bits):
    return randint(0, bit_mask(bits))


def str2blocks(text):
    return list(map(ord, text))


def blocks2str(blocks):
    return str().join(map(chr, blocks))


if __name__ == "__main__":
    P, S = blowfish.generate([randint(0, bit_mask(32)) for _ in range(14)])

    def bf_encrypt(x):
        return blowfish.encrypt(x, P, S)


    def bf_decrypt(x):
        return blowfish.decrypt(x, P, S)

    data = [randint(0, bit_mask(64))] + str2blocks('Odpowiedzi do egzaminu z WDI')
    print('IV:', data[0])
    print(blocks2str(data[1:]))
    encrypt(data, bf_encrypt)
    print(data)
    decrypt(data, bf_decrypt)
    print(blocks2str(data[1:]))
