
def egcd(ld, d):  # erweiterter Euklidischer Algorithmus
    # Aufruf: egcd(a,b) mit natuerlichen Zahlen a,b>0
    # Ausgabe: (d,x,y) mit:
    #     d ist groesster gemeinsamer Teiler von a und b
    #     x,y sind ganze Zahlen mit d = x*a + y*b
    (lx, x) = (1, 0)
    (ly, y) = (0, 1)
    while d != 0:
        q = ld // d
        (d, ld) = (ld % d, d)
        (x, lx) = (lx - q * x, x)
        (y, ly) = (ly - q * y, y)
    return ld, lx, ly


def ModInv(e, n):  # Inverses mod n
    # Aufruf: ModInv(e,n) mit natuerlichen Zahlen e,n>0 und ggT(e,n)=1
    # Ausgabe: d aus {1,...,n-1} mit (d*e)%n = 1
    return egcd(e, n)[1]


def ModExp(x, y, n):  # Exponentialfunktion mod n
    # Aufruf: ModExp(x,y,n) mit natuerlichen Zahlen x,y,n und n>=2
    # Ausgabe: z = (x**y)%n
    return (x ** y) % n


def RSAKeyGen(r=1024):
    # Aufruf: RSAKeyGen(r) mit natuerlicher Zahl r>=5
    # Ausgabe: ((n,e),(n,d)) mit
    #     n = p*q fuer zufaellige Primzahlen p,q mit p!=q und
    #         p,q aus [2**l,2**(l+1)), wobei l = (r+2)//2
    #     e = zufaellige Zahl mit 1<e<phi(n) und ggT(e,phi(n))=1
    #     d = Inverses von e modulo phi(n),
    #         d.h. 1<d<phi(n) mit der Eigenschaft (e*d) % phi(n) = 1
    #

    l = (r + 2) // 2
    primes = []
    for i in range(2 ** l, 2 ** (l + 1)):
        if IsPrime(i):
            primes.append(i)
            if len(primes) == 2:
                break
    p = primes[0]
    q = primes[1]
    n = q * p
    phin = (q - 1) * (p - 1)
    while egcd(e := random.randint(2, phin), phin)[0] != 1:
        pass
    return (n, e), (n, ModInv(e, phin))


def power(g_base, a, p_mod):
    x = 1
    bits = "{0:b}".format(a)
    for i, bit in enumerate(bits):
        if bit == '1':
            x = (((x ** 2) * g_base) % p_mod)
        elif bit == '0':
            x = ((x ** 2) % p_mod)
    return x % p_mod


def RSAEncrypt(pk, m):
    # Aufruf: RSAEncrypt(pk,m) mit public key pk und Klartext m
    # Ausgabe: Chiffretext c
    return power(m, pk[1], pk[0])


def RSADecrypt(sk, c):
    # Aufruf: RSADecrypt(sk,c) mit secure key sk und Chiffretext c
    # Ausgabe: dechiffrierte Nachricht m
    return power(c, sk[1], sk[0])


def str2int(s):  # codiert einen String als Zahl (zum Testen von RSA)
    # Aufruf: str2int('Das ist ein Test.')
    # Ausgabe: 23268733837745479405720608239248647353390
    x = 0
    for i in range(0, len(s)):
        x = (x << 8) + ord(s[i])
    return x


def int2str(x):  # codiert eine Zahl als String (zum Testen von RSA)
    # Aufruf: int2str(23268733837745479405720608239248647353390)
    # Ausgabe: 'Das ist ein Test.'
    s = ''
    while x > 0:
        s = chr(x & 255) + s
        x = x >> 8
    return s


def RSATest():
    ms = 'NSA aus USA hasst RSA.'
    m = str2int(ms)
    print("Klartext als String:      " + ms)
    print("Klartext als Zahl:        " + str(m))
    r = len(bin(m)) - 2  # Laenge des Klartexts bestimmen
    (pk, sk) = RSAKeyGen(r)
    (n, e) = pk
    (n, d) = sk
    print("n =                       " + str(n))
    print("e =                       " + str(e))
    print("d =                       " + str(d))
    c = RSAEncrypt(pk, m)
    cs = int2str(c)
    print("Chiffretext als Zahl:     " + str(c))
    b = RSADecrypt(sk, c)
    bs = int2str(b)
    print("entschl. Text als String: " + bs)
    print("entschl. Text als Zahl:   " + str(b))
    return


RSATest()
