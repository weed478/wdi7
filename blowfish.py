from blowfish_box import PARRAY, SBOX


def bit_mask(n):
    return (1 << n) - 1


def split64(x):
    return x >> 32, x & bit_mask(32)


def merge64(xL, xR):
    return (xL << 32) | xR


def F(xL, S):
    """
    Blowfish F function

    :param xL: 32 bit word
    :param S: S box
    :return: 32 bit word
    """
    d = xL & 0xff
    xL >>= 8

    c = xL & 0xff
    xL >>= 8

    b = xL & 0xff
    xL >>= 8

    a = xL & 0xff

    return ((((S[0][a] + S[1][b]) & bit_mask(32)) ^ S[2][c]) + S[3][d]) & bit_mask(32)


def feistel(xL, xR, P, S):
    """
    Blowfish Feistel network

    :type xL: int
    :type xR: int
    :param xL: left 32 bit half
    :param xR: right 32 bit half
    :param P: P array
    :param S: S box
    :return: xL, xR
    """
    for i in range(16):
        xL ^= P[i]
        xR ^= F(xL, S)
        xL, xR = xR, xL

    xL, xR = xR, xL
    xR ^= P[16]
    xL ^= P[17]

    return xL, xR


def generate(key):
    """
    Generate subkeys

    :param key: 32 bit word array
    :return: P, S
    """
    P = list(PARRAY)
    S = [list(box) for box in SBOX]

    for i in range(18):
        P[i] ^= key[i % len(key)]

    xL, xR = 0, 0
    for i in range(0, 18, 2):
        xL, xR = feistel(xL, xR, P, S)
        P[i] = xL
        P[i + 1] = xR

    for i in range(4):
        for j in range(0, 256, 2):
            xL, xR = feistel(xL, xR, P, S)
            S[i][j] = xL
            S[i][j + 1] = xR

    return tuple(P), tuple(S)


def encrypt(x, P, S):
    """
    Encrypt 64 bit word

    :type x: int
    """
    xL, xR = split64(x)
    xL, xR = feistel(xL, xR, P, S)
    return merge64(xL, xR)


def decrypt(x, P, S):
    """
    Decrypt 64 bit ciphertext

    :type x: int
    """
    xL, xR = split64(x)
    xL, xR = feistel(xL, xR, tuple(reversed(P)), S)
    return merge64(xL, xR)


def key_arr(x):
    """
    Convert integer key to 32 bit word array

    :type x: int
    :return: tuple
    """
    b = [x & bit_mask(32)]
    x >>= 32
    while x > 0:
        b.insert(0, x & bit_mask(32))
        x >>= 32
    return tuple(b)


def test(k, p, c):
    """
    Verify encryption and decryption

    :type k: int
    :type p: int
    :type c: int
    :param k: key
    :param p: plaintext
    :param c: expected ciphertext
    :return: False if test failed
    """
    P, S = generate(key_arr(k))
    crypt = encrypt(p, P, S)
    plain = decrypt(crypt, P, S)

    res = True

    if crypt != c:
        print('Crypt:', hex(crypt), '!=', hex(c))
        res = False

    if plain != p:
        print('Decrypt:', hex(plain), '!=', hex(p))
        res = False

    return res


test(0x0000000000000000, 0x0000000000000000, 0x4EF997456198DD78)
test(0xFFFFFFFFFFFFFFFF, 0xFFFFFFFFFFFFFFFF, 0x51866FD5B85ECB8A)
test(0x3000000000000000, 0x1000000000000001, 0x7D856F9A613063F2)
test(0x1111111111111111, 0x1111111111111111, 0x2466DD878B963C9D)
test(0x0123456789ABCDEF, 0x1111111111111111, 0x61F9C3802281B096)
test(0x1111111111111111, 0x0123456789ABCDEF, 0x7D0CC630AFDA1EC7)
test(0x0000000000000000, 0x0000000000000000, 0x4EF997456198DD78)
test(0xFEDCBA9876543210, 0x0123456789ABCDEF, 0x0ACEAB0FC6A0A28D)
test(0x7CA110454A1A6E57, 0x01A1D6D039776742, 0x59C68245EB05282B)
test(0x0131D9619DC1376E, 0x5CD54CA83DEF57DA, 0xB1B8CC0B250F09A0)
test(0x07A1133E4A0B2686, 0x0248D43806F67172, 0x1730E5778BEA1DA4)
test(0x3849674C2602319E, 0x51454B582DDF440A, 0xA25E7856CF2651EB)
test(0x04B915BA43FEB5B6, 0x42FD443059577FA2, 0x353882B109CE8F1A)
test(0x0113B970FD34F2CE, 0x059B5E0851CF143A, 0x48F4D0884C379918)
test(0x0170F175468FB5E6, 0x0756D8E0774761D2, 0x432193B78951FC98)
test(0x43297FAD38E373FE, 0x762514B829BF486A, 0x13F04154D69D1AE5)
test(0x07A7137045DA2A16, 0x3BDD119049372802, 0x2EEDDA93FFD39C79)
test(0x04689104C2FD3B2F, 0x26955F6835AF609A, 0xD887E0393C2DA6E3)
test(0x37D06BB516CB7546, 0x164D5E404F275232, 0x5F99D04F5B163969)
test(0x1F08260D1AC2465E, 0x6B056E18759F5CCA, 0x4A057A3B24D3977B)
test(0x584023641ABA6176, 0x004BD6EF09176062, 0x452031C1E4FADA8E)
test(0x025816164629B007, 0x480D39006EE762F2, 0x7555AE39F59B87BD)
test(0x49793EBC79B3258F, 0x437540C8698F3CFA, 0x53C55F9CB49FC019)
test(0x4FB05E1515AB73A7, 0x072D43A077075292, 0x7A8E7BFA937E89A3)
test(0x49E95D6D4CA229BF, 0x02FE55778117F12A, 0xCF9C5D7A4986ADB5)
test(0x018310DC409B26D6, 0x1D9D5C5018F728C2, 0xD1ABB290658BC778)
test(0x1C587F1C13924FEF, 0x305532286D6F295A, 0x55CB3774D13EF201)
test(0x0101010101010101, 0x0123456789ABCDEF, 0xFA34EC4847B268B2)
test(0x1F1F1F1F0E0E0E0E, 0x0123456789ABCDEF, 0xA790795108EA3CAE)
test(0xE0FEE0FEF1FEF1FE, 0x0123456789ABCDEF, 0xC39E072D9FAC631D)
test(0x0000000000000000, 0xFFFFFFFFFFFFFFFF, 0x014933E0CDAFF6E4)
test(0xFFFFFFFFFFFFFFFF, 0x0000000000000000, 0xF21E9A77B71C49BC)
test(0x0123456789ABCDEF, 0x0000000000000000, 0x245946885754369A)
test(0xFEDCBA9876543210, 0xFFFFFFFFFFFFFFFF, 0x6B5C5A9C5D9E0A5A)
