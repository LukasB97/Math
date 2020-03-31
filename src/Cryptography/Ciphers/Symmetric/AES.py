from typing import List

import numpy

from Cryptography.Ciphers.Symmetric.AESResources import sub_byte_table, mix_col_matrix
from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Cryptography.Ciphers.Cipher import Cipher
from src.Cryptography.FinitePolynomialFieldFactory import FinitePolynomialFieldFactory


class AES(Cipher):
    polynomial_factory: FinitePolynomialFieldFactory(8, numpy.array([1, 1, 0, 1, 1, 0, 0, 0, 1]))

    def encrypt(self, message):
        blocks: List[Matrix] = self.blocks_from_string(message)
        encrypted_blocks = [self._encrypt_matrix(blocks[0])]
        for i in range(1, len(blocks)):
            encrypted_blocks.append(
                self._encrypt_matrix(blocks[i], encrypted_blocks[i-1])
            )
        return self.string_from_blocks(encrypted_blocks)

    def _encrypt_matrix(self, matrix, previous=None):
        if previous is not None:
            matrix = matrix | previous
        for i in range(10):
            matrix = self.aes_round(matrix)
        matrix = self.sub_bytes(matrix)
        return self.shift_row(matrix)

    def decrypt(self, chiffretext):
        blocks: List[Matrix] = self.blocks_from_string(chiffretext)
        encrypted_blocks = [self._encrypt_matrix(blocks[0])]
        for i in range(1, len(blocks)):
            encrypted_blocks.append(
                self._encrypt_matrix(blocks[i], encrypted_blocks[i - 1])
            )
        return self.string_from_blocks(encrypted_blocks)

    def create_key(self, *args, **kwargs):
        pass

    # eine AES-Runde bestehend aus SubByte, ShiftRow, MixCol und AddKey
    def aes_round(self, data_to_encrypt):
        data_to_encrypt = self.sub_bytes(data_to_encrypt)
        data_to_encrypt = self.shift_row(data_to_encrypt)
        return self.mix_col(data_to_encrypt)

    def sub_bytes(self, matrix):
        result = numpy.zeros((4, 4))
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = sub_byte_table[matrix[i, j]]
        return Matrix(result, self.polynomial_factory.create)

    def shift_row(self, to_shift):
        return Matrix([
            to_shift.matrix_vectors[0],
            [to_shift[1, 1], to_shift[1, 2], to_shift[1, 3], to_shift[1, 0]],
            [to_shift[2, 2], to_shift[2, 3], to_shift[2, 0], to_shift[2, 1]],
            [to_shift[3, 3], to_shift[3, 0], to_shift[3, 1], to_shift[3, 2]]
        ], self.polynomial_factory.create
        )

    def mix_col(self, matrix_to_mix):
        return mix_col_matrix * matrix_to_mix

    def blocks_from_string(self, chriffretext):
        text_bytes = bytearray(chriffretext, "utf-8")
        blocks = []
        next_matrix = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
        i = 0
        for b in text_bytes:
            next_matrix[i // 4][i % 4] = b
            i += 1
            if i == 16:
                blocks.append(Matrix(next_matrix))
                next_matrix = [[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0],[0, 0, 0, 0]]
                i = 0
        if i != 0:
            blocks.append(Matrix(next_matrix))
        return blocks





    def string_from_blocks(self, blocks: List[Matrix]):
        result = []
        for block in blocks:
            for i in range(4):
                for j in range(4):
                    result.append(block[i, j])
        return bytearray(result).decode("utf-8")



