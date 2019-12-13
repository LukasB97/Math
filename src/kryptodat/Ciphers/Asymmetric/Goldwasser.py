


def ModExp(x, y, n):  # Exponentialfunktion mod n
    # Aufruf: ModExp(x,y,n) mit natuerlichen Zahlen x,y,n und n>=2
    # Ausgabe: (x**y)%n
    z = i = 1
    p = x % n
    while (i <= y):  # Invariante: p = (x^i)%n
        if i & y > 0:
            z = (z * p) % n
        i = i + i
        p = (p * p) % n
    return z


########################################################
########################################################
########################################################

def IsQuadraticResidue(x, p, q):  # testet, ob x quadratischer Rest mod p*q ist
    # Aufruf: IsQuadraticResidue(x,p,q) mit Primzahlen p,q und
    #         x aus {1,...,p*q-1} mit ggT(x,p*q)=1
    # Ausgabe: True, falls es ein a aus {1,...,p*q-1} gibt mit a*a=x (mod p*q)
    #          False, sonst
    ...
    return ...


def GMKeyGen(l=512):  # Schluesselgenerator fuer Goldwasser-Micali-Kryptosystem
    # Aufruf: GMKeyGen(l) mit natuerlicher Zahl l>2
    # Ausgabe: (n,(p,q)) mit n aus [2**(l-1),2**l] und n = p*q fuer
    #          zufaellige, verschiedene Primzahlen p,q aus [2,2**((l+1)//2)] mit p%4=q%4=3
    ...
    return (n, (p, q))


def GMEncryptBit(pk, b):  # Verschluesselung fuer Goldwasser-Micali-Kryptosystem
    # Aufruf: GMEncrypt(pk,b) mit public key pk und Klartextbit b
    # Ausgabe: Chiffretext c = (r*r*((n-1)**b)) % pk
    #          fuer Zufallszahl r aus {1,...,pk-1} mit ggT(r,pk)=1
    ...
    return c


def GMDecryptBit(sk, c):  # Entschluesselung fuer Goldwasser-Micali-Kryptosystem
    # Aufruf: GMDecrypt(sk,c) mit secure key sk und chiffriertes Bit c
    # Ausgabe: dechiffriertes Bit
    #     0 falls c quadratischer Rest mod pk ist
    #     1 falls c kein quadratischer Rest mod pk ist
    ...
    return ...


########################################################
########################################################
########################################################

def GMTest():  # Test fuer Goldwasser-Micali-Kryptosystem
    pt = 1234
    print("Klartext in Dezimaldarstellung: " + str(pt))
    print("Klartext in Binaerdarstellung: " + bin(pt))
    print()
    (pk, sk) = GMKeyGen(256)
    print("Public Key: " + str(pk))
    print("Private Key: " + str(sk))
    print()
    ptl = [int(bin(pt)[i]) for i in range(2, len(bin(pt)))]  # Liste der Klartextbits
    print("Klartextbits | Chiffretexte der Bits")
    print("-------------+----------------------")
    ctl = []
    for i in range(0, len(ptl)):
        ptb = ptl[i]  # Klartextbit
        ctb = GMEncryptBit(pk, ptb)  # Chiffretext des Bits
        ctl += [ctb]
        print("      " + str(ptl[i]) + "      | " + str(ctb))
    print()
    encrypted = ""
    for i in range(0, len(ctl)):
        encrypted += str(GMDecryptBit(sk, ctl[i]))
    print("entschluesselter Chiffretext in Binaerdarstellung: 0b" + encrypted)
    print("entschluesselter Chiffretext in Dezimaldarstellung: " + str(int(encrypted, 2)))
    return
