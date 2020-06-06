from abc import abstractmethod, ABC

from src.Cryptography.CryptographicScheme import CryptographicScheme


class Cipher(CryptographicScheme, ABC):

    def __init__(self, secret_key, encoding="utf-8", *args, **kwargs):
        self.encoding = encoding
        super().__init__(secret_key, *args, **kwargs)

    @abstractmethod
    def encrypt_bytes(self, bytes_to_encrypt: bytes) -> bytes:
        pass

    @abstractmethod
    def decrypt_bytes(self, bytes_to_decrypt: bytes) -> bytes:
        pass


    def encrypt(self, message: str) -> str:
        bytes_to_encrypt = message.encode(self.encoding)
        encrypted_bytes = self.encrypt_bytes(bytes_to_encrypt)
        return encrypted_bytes.decode(self.encoding)


    def decrypt(self, chiffretext: str) -> str:
        bytes_to_decrypt = chiffretext.encode(self.encoding)
        decrypted_bytes = self.decrypt_bytes(bytes_to_decrypt)
        return decrypted_bytes.decode(self.encoding)

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
