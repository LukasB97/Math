from src.Cryptography.Ciphers.Asymmetric.RSA import RSA
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm


class RSASignature(SignatureAlgorithm, RSA):

    def __init__(self, secret_key=None, pk=None, *args, **kwargs):
        super().__init__(secret_key, pk, *args, **kwargs)

    def create_signature(self, message):
        message_hash = self.hash(message)
        return self.encrypt(message_hash)

    def verify_signature(self, message, signature):
        message_hash = self.hash(message)
        return self.decrypt(signature) == message_hash
