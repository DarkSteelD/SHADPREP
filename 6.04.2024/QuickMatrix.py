dict_for_numbers = {
    1: [6, 8], 2: [7, 9], 3: [4, 8],
    4: [3, 0, 9], 5: [], 6: [1, 0, 7],
    7: [2, 6], 8: [1, 3], 9: [4, 2],
    0: [4, 6]
}

def matrix_multiply(A, B):
    size = len(A)
    result = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            for k in range(size):
                result[i][j] += A[i][k] * B[k][j]
    return result

def matrix_power(matrix, step):
    size = len(matrix)
    result = [[int(i == j) for j in range(size)] for i in range(size)]  # identity
    while step:
        if step % 2:
            result = matrix_multiply(result, matrix)
        matrix = matrix_multiply(matrix, matrix)
        step //= 2
    return result

def vector_multiply(matrix, vector):
    size = len(vector)
    result = [0] * size
    for i in range(size):
        for j in range(size):
            result[i] += matrix[i][j] * vector[j]
    return result

def solve(steps):
    if steps == 0:
        return 8

    size = 10
    M = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in dict_for_numbers[i]:
            M[j][i] = 1

    M = matrix_power(M, steps)

    start = [1 if i != 0 and i != 8 else 0 for i in range(10)]
    final = vector_multiply(M, start)
    return sum(final)

steps = int(input()) - 1
print(solve(steps))
