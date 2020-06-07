def extended_euclidean_algorithm(ld, d):  # erweiterter euclidean algorithm
    # call: egcd(a,b) mit natural numbers a,b>0
    # return: (d,x,y) mit:
    #     d ist greatest common Teiler von a und b
    #     x,y sind ganze numbers mit d = x*a + y*b
    (lx, x) = (1, 0)
    (ly, y) = (0, 1)
    while d != 0:
        q = ld // d
        (d, ld) = (ld % d, d)
        (x, lx) = (lx - q * x, x)
        (y, ly) = (ly - q * y, y)
    return ld, lx, ly


def gcd(a, b):  # greatest common Teiler
    # call: gcd(a,b) mit natural numbers a,b>0
    # return: greatest common Teiler von a und b
    return extended_euclidean_algorithm(a, b)[0]
