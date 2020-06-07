from src.Cryptography.Ciphers.Asymmetric.RSA import RSA
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm


class RSASignature(SignatureAlgorithm, RSA):

    def __init__(self, secret_key=None, *args, **kwargs):
        super().__init__(secret_key=secret_key, *args, **kwargs)

    def create_signature(self, message: str):
        message_hash = self.hash(message)
        return self.decrypt(message_hash)

    def verify_signature(self, message, signature, signed_by_pk=None, *args, **kwargs):
        if signed_by_pk is None:
            signed_by_pk = self.public_key
        message_hash = self.hash(message)
        return self.encrypt(signature, signed_by_pk) == message_hash
