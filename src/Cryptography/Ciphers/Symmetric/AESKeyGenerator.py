from src.Cryptography.Ciphers.Symmetric.AESResources import sub_byte_table


def key_expansion(base_key):
    r = [0, 0x1000000, 0x2000000, 0x4000000, 0x8000000, 0x10000000, 0x20000000, 0x40000000,
         0x80000000, 0x1b000000, 0x36000000]
    w = [0] * 44
    w[0] = base_key[0][0] * 0x1000000 + base_key[1][0] * 0x10000 + base_key[2][0] * 0x100 + base_key[3][0]
    w[1] = base_key[0][1] * 0x1000000 + base_key[1][1] * 0x10000 + base_key[2][1] * 0x100 + base_key[3][1]
    w[2] = base_key[0][2] * 0x1000000 + base_key[1][2] * 0x10000 + base_key[2][2] * 0x100 + base_key[3][2]
    w[3] = base_key[0][3] * 0x1000000 + base_key[1][3] * 0x10000 + base_key[2][3] * 0x100 + base_key[3][3]
    for i in range(4, 44):
        t = w[i - 1]
        if (i % 4) == 0:
            t = ((sub_byte_table[(t >> 16) & 0xff] << 24) | (sub_byte_table[(t >> 8) & 0xff] << 16) |
                 (sub_byte_table[(t >> 0) & 0xff] << 8) | (sub_byte_table[(t >> 24) & 0xff] << 0)) ^ r[i // 4]
        w[i] = w[i - 4] ^ t
    expanded_key = []
    for r in range(0, 11):
        base_key = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(0, 4):
            for j in range(0, 4):
                base_key[i][j] = (w[4 * r + j] >> (8 * (3 - i))) & 0xff
        expanded_key.append(base_key)
    return expanded_key
