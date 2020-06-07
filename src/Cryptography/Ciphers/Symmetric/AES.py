from typing import List

import numpy

from src.Algebra.Structures.Matrix.Matrix import Matrix
from src.Cryptography.Ciphers.Cipher import Cipher
from src.Cryptography.Ciphers.Symmetric.AESResources import sub_byte_table, mix_col_matrix, revert_mix_col_matrix
from src.Cryptography.FinitePolynomialField import FinitePolynomialField


class AES(Cipher):


    def create_key(self, *args, **kwargs):
        pass

    def encrypt_bytes(self, bytes_to_encrypt: bytes, *args, **kwargs) -> bytes:
        blocks: List[Matrix] = self.blocks_from_bytes(bytes_to_encrypt)
        encrypted_blocks = [self._encrypt_matrix(blocks[0])]
        for i in range(1, len(blocks)):
            encrypted_blocks.append(
                self._encrypt_matrix(blocks[i], encrypted_blocks[i - 1])
            )
        return self.string_from_blocks(encrypted_blocks)

    def decrypt_bytes(self, bytes_to_decrypt: bytes, *args, **kwargs) -> bytes:
        blocks: List[Matrix] = self.blocks_from_bytes(bytes_to_decrypt)

    def __init__(self, secret_key=None, field_constructor=FinitePolynomialField.constructor(), *args, **kwargs):
        super().__init__(secret_key, *args, **kwargs)
        self.field_constructor = field_constructor

    def _encrypt_matrix(self, matrix, previous=None):
        if previous is not None:
            matrix = matrix ^ previous
        for i in range(10):
            matrix = self.aes_round(matrix)
        matrix = self.sub_bytes(matrix)
        return self.shift_row(matrix)


    # eine AES-Runde bestehend aus SubByte, ShiftRow, MixCol und AddKey
    def aes_round(self, data_to_encrypt):
        data_to_encrypt = self.sub_bytes(data_to_encrypt)
        data_to_encrypt = self.shift_row(data_to_encrypt)
        return self.mix_col(data_to_encrypt)

    def sub_bytes(self, matrix):
        result = numpy.zeros((4, 4), dtype=int)
        for i in range(0, 4):
            for j in range(0, 4):
                result[i][j] = sub_byte_table[matrix[i, j]]
        return Matrix(result, value_factory=self.field_constructor, dtype=FinitePolynomialField, preserve_dt=True)

    def shift_row(self, to_shift):
        return Matrix([
            to_shift.matrix_vectors[0],
            [to_shift[1, 1], to_shift[1, 2], to_shift[1, 3], to_shift[1, 0]],
            [to_shift[2, 2], to_shift[2, 3], to_shift[2, 0], to_shift[2, 1]],
            [to_shift[3, 3], to_shift[3, 0], to_shift[3, 1], to_shift[3, 2]]
        ], value_factory=self.field_constructor, dtype=FinitePolynomialField, preserve_dt=True
        )

    def revert_shift_row(self, to_revert):
        return Matrix([
            to_revert.matrix_vectors[0],
            [to_revert[1, 3], to_revert[1, 0], to_revert[1, 1], to_revert[1, 2]],
            [to_revert[2, 2], to_revert[2, 3], to_revert[2, 0], to_revert[2, 1]],
            [to_revert[3, 1], to_revert[3, 2], to_revert[3, 3], to_revert[3, 0]]
        ], value_factory=self.field_constructor, dtype=FinitePolynomialField, preserve_dt=True
        )

    @staticmethod
    def mix_col(matrix_to_mix):
        return mix_col_matrix * matrix_to_mix

    @staticmethod
    def revert_mix_col(matrix_to_revert):
        return revert_mix_col_matrix * matrix_to_revert

    def blocks_from_bytes(self, data_bytes):
        blocks = []
        next_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
        i = 0
        for b in data_bytes:
            next_matrix[i // 4][i % 4] = b
            i += 1
            if i == 16:
                blocks.append(Matrix(next_matrix, value_factory=self.field_constructor, dtype=FinitePolynomialField,
                                     preserve_dt=True))
                next_matrix = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
                i = 0
        if i != 0:
            blocks.append(Matrix(next_matrix))
        return blocks

    @staticmethod
    def string_from_blocks(blocks: List[Matrix]):
        result = bytearray()
        for block in blocks:
            for i in range(4):
                for j in range(4):
                    result.append(block[i, j])
        return bytes(result)
