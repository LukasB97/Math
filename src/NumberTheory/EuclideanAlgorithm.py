def extended_euclidean_algorithm(ld, d):  # erweiterter Euklidischer Algorithmus
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


def greatest_common_divisor(a, b):  # groesster gemeinsamer Teiler
    # Aufruf: gcd(a,b) mit natuerlichen Zahlen a,b>0
    # Ausgabe: groesster gemeinsamer Teiler von a und b
    return extended_euclidean_algorithm(a, b)[0]
