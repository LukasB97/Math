def calc(v, u):
    sum_ = 0
    for i in range(len(v)):
        sum_ += v[i] * u[i]
    return sum_
