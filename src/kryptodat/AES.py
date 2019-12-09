import numpy

from src.AlgebraicStructures.Matrix.Matrix import Matrix
from src.kryptodat.FinitePolynomialFieldFactory import FinitePolynomialFieldFactory

global SubByteTable
SubByteTable = [
    0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76,
    0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0,
    0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15,
    0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75,
    0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84,
    0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf,
    0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8,
    0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2,
    0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73,
    0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb,
    0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79,
    0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08,
    0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a,
    0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e,
    0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf,
    0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]

factory = FinitePolynomialFieldFactory(8, numpy.array([1, 1, 0, 1, 1, 0, 0, 0, 1]))


# Eingabe ist der AES-Schluessel K (4x4 Matrix ueber F256)
# Ausgabe ist eine Liste L, die die 11 Schluessel L[0], ..., L[10] enthaelt (4x4 Matrizen ueber F256)
def KeyExpansion(K):
    R = [0, 0x1000000, 0x2000000, 0x4000000, 0x8000000, 0x10000000, 0x20000000, 0x40000000,
         0x80000000, 0x1b000000, 0x36000000]
    w = [0] * 44
    w[0] = K[0][0] * 0x1000000 + K[1][0] * 0x10000 + K[2][0] * 0x100 + K[3][0]
    w[1] = K[0][1] * 0x1000000 + K[1][1] * 0x10000 + K[2][1] * 0x100 + K[3][1]
    w[2] = K[0][2] * 0x1000000 + K[1][2] * 0x10000 + K[2][2] * 0x100 + K[3][2]
    w[3] = K[0][3] * 0x1000000 + K[1][3] * 0x10000 + K[2][3] * 0x100 + K[3][3]
    i = 4
    while i < 44:
        t = w[i - 1]
        if (i % 4) == 0:
            t = ((SubByteTable[(t >> 16) & 0xff] << 24) | (SubByteTable[(t >> 8) & 0xff] << 16) |
                 (SubByteTable[(t >> 0) & 0xff] << 8) | (SubByteTable[(t >> 24) & 0xff] << 0)) ^ R[i // 4]
        w[i] = w[i - 4] ^ t
        i = i + 1
    L = []
    for r in range(0, 11):
        K = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        for i in range(0, 4):
            for j in range(0, 4):
                K[i][j] = (w[4 * r + j] >> (8 * (3 - i))) & 0xff
        L = L + [K]
    return L


# Addition in F256
def F256Add(x, y):
    return x ^ y


# Multiplikation in F256
def F256Mul(x, y):
    p = 0  # zuerst Produkt der Polynome bilden
    while y > 0:
        if y & 1 == 1:
            p = p ^ x
        x = x << 1
        y = y >> 1
    f = 0b100011011  # jetzt modulo f(x)=x^8+x^4+x^3+x+1 rechnen
    while len(bin(p)) >= 11:
        p = p ^ (f << (len(bin(p)) - 11))
    return p


def SubByte(A):
    B = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    for i in range(0, 4):
        for j in range(0, 4):
            print(A[i, j].value)
            B[i][j] = factory.create(SubByteTable[A[i, j].value])
    return Matrix(B)


def ShiftRow(A):
    return Matrix([
    A.matrix_vectors[0],
    [A[1,1], A[1, 2], A[1,3], A[1,0]],
    [A[2,2], A[2, 3], A[2,0], A[2,1]],
    [A[3,3], A[3,0], A[3,1], A[3,2]]
    ]
    )

def MixCol(A):
    one = factory.create(value=1)
    two = factory.create(value=2)
    three = factory.create(value=3)
    matrix = Matrix(
        [
            [two, three, one, one],
            [one, two, three, one],
            [one, one, two, three],
            [three, one, one, two]
        ]
    )
    return matrix * A


# addiert den Schluessel K zu den Daten A
def AddKey(A, K):
    # A = zu verschluesselnde Daten (4x4 Matrix ueber F256)
    # K = Schluessel (4x4 Matrix ueber F256)
    B = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    ...
    return B


# eine AES-Runde bestehend aus SubByte, ShiftRow, MixCol und AddKey
def AESRound(A, K):
    # A = zu verschluesselnde Daten (4x4 Matrix ueber F256)
    # K = Schluessel (4x4 Matrix ueber F256)
    ...
    return ...


# gesamtes AES bestehend aus 11 Runden
def AES(P, K):
    # P = zu verschluesselnde Daten (4x4 Matrix ueber F256)
    # K = Schluessel (4x4 Matrix ueber F256)
    K = KeyExpansion(K)
    # K[0], ..., K[10] sind die Schluessel fuer die Runden 0-10 (4x4 Matrizen ueber F256)
    ...
    return ...


# es folgen einige Tests fuer die obigen Funktionen
def AESTests():
    if F256Add(123, 45) != 86: print("Fehler in F256Add")
    #
    if F256Mul(123, 45) != 128: print("Fehler in F256Mul")
    #
    A = Matrix([[factory.create(0xe1), factory.create(0x19), factory.create(0xb3), factory.create(0xf7)],
                [factory.create(0x6c), factory.create(0x8e), factory.create(0x56), factory.create(0xb2)],
                [factory.create(0x13), factory.create(0x7f), factory.create(0x9a), factory.create(0x1b)],
                [factory.create(0xe3), factory.create(0x41), factory.create(0xe1), factory.create(0xad)]])
    B = Matrix([[factory.create(0x9d), factory.create(0x85), factory.create(0xfc), factory.create(0x8e)],
                [factory.create(0xef), factory.create(0xde), factory.create(0x4b), factory.create(0x08)],
                [factory.create(0x95), factory.create(0xaa), factory.create(0xf2), factory.create(0x9f)],
                [factory.create(0x9a), factory.create(0x58), factory.create(0xdb), factory.create(0xea)]
                ])
    mc = MixCol(A)
    if MixCol(A) != B: print("Fehler in MixCol")
    #
    A = Matrix([
        [factory.create(0x76), factory.create(0xbd), factory.create(0xec), factory.create(0xed)],
        [factory.create(0x27), factory.create(0xe5), factory.create(0xb0), factory.create(0x20)],
        [factory.create(0x20), factory.create(0xa5), factory.create(0xe6), factory.create(0x35)],
        [factory.create(0x87), factory.create(0xb7), factory.create(0xe7), factory.create(0x9e)]
    ])
    B = Matrix([
        [factory.create(0x38), factory.create(0x7a), factory.create(0xce), factory.create(0x55)],
        [factory.create(0xcc), factory.create(0xd9), factory.create(0xe7), factory.create(0xb7)],
        [factory.create(0xb7), factory.create(0x06), factory.create(0x8e), factory.create(0x96)],
        [factory.create(0x17), factory.create(0xa9), factory.create(0x94), factory.create(0x0b)]
    ])
    if SubByte(A) != B: print("Fehler in SubByte")
    #
    A = Matrix([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], factory)
    B = Matrix([[1, 2, 3, 4], [6, 7, 8, 5], [11, 12, 9, 10], [16, 13, 14, 15]], factory)
    if ShiftRow(A) != B: print("Fehler in ShiftRow")
    #
    A = [[factory.create(0x76), factory.create(0xbd), factory.create(0xec), factory.create(0xed)], [
        factory.create(0x27), factory.create(0xe5), factory.create(0xb0), factory.create(0x20)], [factory.create(0x20),
                                                                                                  factory.create(0xa5),
                                                                                                  factory.create(0xe6),
                                                                                                  factory.create(
                                                                                                      0x35)], [
        factory.create(0x87), factory.create(0xb7), factory.create(0xe7), factory.create(0x9e)]]
    K = [[factory.create(0xe6), factory.create(0x04), factory.create(0x51), factory.create(0x24)], [
        factory.create(0xdc), factory.create(0xfd), factory.create(0x58), factory.create(0xc3)], [factory.create(0x49),
                                                                                                  factory.create(0xe6),
                                                                                                  factory.create(0x59),
                                                                                                  factory.create(
                                                                                                      0x79)], [
        factory.create(0x51), factory.create(0xcd), factory.create(0x99), factory.create(0x2a)]]
    B = [[factory.create(0x63), factory.create(0x43), factory.create(0x0a), factory.create(0x53)], [
        factory.create(0xcf), factory.create(0xe4), factory.create(0x88), factory.create(0x8b)], [factory.create(0xb2),
                                                                                                  factory.create(0x75),
                                                                                                  factory.create(0xb5),
                                                                                                  factory.create(
                                                                                                      0x4b)], [
        factory.create(0x58), factory.create(0x1c), factory.create(0x99), factory.create(0x2c)]]
    if AESRound(A, K) != B: print("Fehler in AESRound")
    #
    P = [[factory.create(0x32), factory.create(0x88), factory.create(0x31), factory.create(0xe0)], [
        factory.create(0x43), factory.create(0x5a), factory.create(0x31), factory.create(0x37)], [factory.create(0xf6),
                                                                                                  factory.create(0x30),
                                                                                                  factory.create(0x98),
                                                                                                  factory.create(
                                                                                                      0x07)], [
        factory.create(0xa8), factory.create(0x8d), factory.create(0xa2), factory.create(0x34)]]
    K = [[factory.create(0x2b), factory.create(0x28), factory.create(0xab), factory.create(0x09)], [
        factory.create(0x7e), factory.create(0xae), factory.create(0xf7), factory.create(0xcf)], [factory.create(0x15),
                                                                                                  factory.create(0xd2),
                                                                                                  factory.create(0x15),
                                                                                                  factory.create(
                                                                                                      0x4f)], [
        factory.create(0x16), factory.create(0xa6), factory.create(0x88), factory.create(0x3c)]]
    C = [[factory.create(0x39), factory.create(0x02), factory.create(0xdc), factory.create(0x19)], [
        factory.create(0x25), factory.create(0xdc), factory.create(0x11), factory.create(0x6a)], [factory.create(0x84),
                                                                                                  factory.create(0x09),
                                                                                                  factory.create(0x85),
                                                                                                  factory.create(
                                                                                                      0x0b)], [
        factory.create(0x1d), factory.create(0xfb), factory.create(0x97), factory.create(0x32)]]
    if AES(P, K) != C: print("Fehler in AES")
    return


AESTests()
