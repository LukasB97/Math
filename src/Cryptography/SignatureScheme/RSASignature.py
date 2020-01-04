import hashlib

from src.Cryptography.Ciphers.Asymmetric.RSA import RSAKeyGen
from src.Cryptography.SignatureScheme.SignatureAlgorithm import SignatureAlgorithm


class RSASignature(SignatureAlgorithm):


  def create_key(self, *args, **kwargs):
    return RSAKeyGen()

  def create_signature(self, message):
    pass

  def verify_signature(self, message, signature):
    pass


def create_signature(sk, m):  # signiert eine Nachricht m
    # Aufruf: ElgamalSignature(sk,m) mit secure key sk und Nachricht m (String)
    # Ausgabe: signierte Nachricht sig = (m,r,s)
    ...
    return (m, r, s)


def verify_signature(pk, sig):  # ueberprueft Signatur einer Nachricht
    # Aufruf: ElgamalSignatureVerify(pk,sig) mit pk=public key, sig=signierte Nachricht
    # Ausgabe: True, falls Signatur korrekt, False sonst
    ...


def ElgamalSignatureTest():  # Beispiel zur Elgamal-Signatur
    (pk, sk) = ElgamalKeyGen(128)
    m = str(7777 ** 7777)  # Klartext mit 30259 Zeichen
    sig = create_signature(sk, m)
    print("signiertes Dokument: sig = " + str(sig))
    print("Verifikation: " + str(verify_signature(pk, sig)))
    return
