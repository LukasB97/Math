from abc import abstractmethod

from src.Cryptography.CryptographicScheme import CryptographicScheme


class Cipher(CryptographicScheme):

    @abstractmethod
    def encrypt(self, message):
        pass

    @abstractmethod
    def decrypt(self, chiffretext):
        pass

    def str2int(self, s):  # codiert einen String als Zahl (zum Testen von RSA)
        # Aufruf: str2int('Das ist ein Test.')
        # Ausgabe: 23268733837745479405720608239248647353390
        x = 0
        for i in range(0, len(s)):
            x = (x << 8) + ord(s[i])
        return x

    def int2str(self, x):  # codiert eine Zahl als String (zum Testen von RSA)
        # Aufruf: int2str(23268733837745479405720608239248647353390)
        # Ausgabe: 'Das ist ein Test.'
        s = ''
        while x > 0:
            s = chr(x & 255) + s
            x = x >> 8
        return s
