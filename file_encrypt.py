#!env python3

import cbc
import blowfish
from hashlib import sha384
import sys


def bytes2word(B, n_bytes):
    x = 0
    for i in range(n_bytes):
        x <<= 8
        if i < len(B):
            x += B[i]
    return x


def word2bytes(x, n_bytes):
    B = [0] * n_bytes
    for i in range(n_bytes):
        x, b = divmod(x, 256)
        B[n_bytes - i - 1] = b
    return bytes(B)


def get_key(passphrase):
    h = sha384(bytes(passphrase, 'utf8')).digest()
    key = bytes2word(h, 48)
    return blowfish.key_arr(key)


def encrypt(path, passphrase):
    key = get_key(passphrase)
    P, S = blowfish.generate(key)

    def algo(x):
        return blowfish.encrypt(x, P, S)

    iv = cbc.generate_iv(64)
    encoder = cbc.Encryptor(algo, iv)

    with open(path, 'rb') as ifile:
        with open(path + '.kugelfisch', 'wb') as ofile:
            ofile.write(word2bytes(iv, 8))
            plain_block = ifile.read(8)
            while len(plain_block) > 0:
                cipher_block = encoder.next(bytes2word(plain_block, 8))
                ofile.write(word2bytes(cipher_block, 8))
                plain_block = ifile.read(8)


def decrypt(path, passphrase):
    key = get_key(passphrase)
    P, S = blowfish.generate(key)

    def algo(x):
        return blowfish.decrypt(x, P, S)

    decoder = cbc.Decrypter(algo)

    with open(path, 'rb') as ifile:
        with open(path + '.plain', 'wb') as ofile:
            iv = ifile.read(8)
            decoder.next(bytes2word(iv, 8))
            cipher_block = ifile.read(8)
            while len(cipher_block) > 0:
                plain_block = decoder.next(bytes2word(cipher_block, 8))
                ofile.write(word2bytes(plain_block, 8))
                cipher_block = ifile.read(8)


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Usage:', sys.argv[0], "e|d FILE [PASSPHRASE]")
        exit(1)

    mode = sys.argv[1]
    path = sys.argv[2]
    if len(sys.argv) >= 4:
        passphrase = sys.argv[3]
    else:
        passphrase = input('Enter passphrase: ')

    if mode == 'e':
        encrypt(path, passphrase)
    elif mode == 'd':
        decrypt(path, passphrase)
    else:
        print('Invalid mode "{}"'.format(mode))
        exit(2)
