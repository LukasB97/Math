def calc(v, u):
    sum = 0
    for i in range(len(v)):
        sum += v[i] * u[i]
    return sum