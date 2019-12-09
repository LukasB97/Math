

def create_type_three(n:int, m:int, row_to_multipy:int, multiply_by:int):
    matrix = list()
    for i in range(m):
        matrix.append(list())
        for j in range(n):
            if j != i:
                matrix[i].append(0)
            elif row_to_multipy == i:
                matrix[i].append(multiply_by)
            else:
                matrix[i].append(1)
    return matrix

def create_type_two(n: int, m: int, swap_first: int, swap_second: int):
    matrix = list()
    for i in range(m):
        matrix.append(list())
        for j in range(n):
            if j != i:
                matrix[i].append(0)
            else:
                matrix[i].append(1)
    matrix[swap_first][swap_second] = 1
    matrix[swap_second][swap_first] = 1
    matrix[swap_second][swap_second] = 0
    matrix[swap_first][swap_first] = 0
    return matrix

def create_type_one(n:int, m:int, row_to_change:int, row_to_add:int, multiply_by: float):
    matrix = list()
    for i in range(m):
        matrix.append(list())
        for j in range(n):
            if j != i:
                matrix[i].append(0)
            else:
                matrix[i].append(1)
    matrix[row_to_change][row_to_add] = multiply_by
    return matrix


def create_frobenius_matrix(A, col: int, pivot_row: int):
    matrix = list()
    for i in range(len(A)):
        matrix.append(list())
        for j in range(len(A[0])):
            if j == col and i != pivot_row:
                matrix[i].append((A[i][col]/A[pivot_row][col])*-1)
            elif j != i:
                matrix[i].append(0)
            else:
                matrix[i].append(1)
    return matrix
    

