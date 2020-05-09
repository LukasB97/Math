from abc import abstractmethod, ABC

from src.Cryptography.CryptographicScheme import CryptographicScheme


class Cipher(CryptographicScheme, ABC):

    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, chiffretext) -> str:
        pass

    @staticmethod
    def str2int(s):  # codiert einen String als Zahl (zum Testen von RSA)
        # call: str2int('Das ist ein Test.')
        # return: 23268733837745479405720608239248647353390
        x = 0
        for i in range(0, len(s)):
            x = (x << 8) + ord(s[i])
        return x

    @staticmethod
    def int2str(x):  # codiert eine Zahl als String (zum Testen von RSA)
        # call: int2str(23268733837745479405720608239248647353390)
        # return: 'Das ist ein Test.'
        s = ''
        while x > 0:
            s = chr(x & 255) + s
            x = x >> 8
        return s
