

def gauss_elimination(A, b):
    n = len(b)
    forward_elimination(A, b, n)
    return back_substitution(A, b, n)


def forward_elimination(A, b, n):
    for i in range(n):
        pivot(A, b, i, n)
        for j in range(i + 1, n):
            if A[i][i] == 0:
                raise ValueError("Matrix is singular or nearly singular")
            ratio = A[j][i] / A[i][i]
            eliminate(A, b, i, j, ratio, n)


def pivot(A, b, i, n):
    max_index = i + max(range(n - i), key=lambda k: abs(A[i + k][i]))
    if i != max_index:
        A[i], A[max_index] = A[max_index], A[i]
        b[i], b[max_index] = b[max_index], b[i]


def eliminate(A, b, i, j, ratio, n):
    for k in range(i, n):  # Note: starting from i instead of 0 for efficiency
        A[j][k] -= ratio * A[i][k]
    b[j] -= ratio * b[i]


def back_substitution(A, b, n):
    x = [0 for _ in range(n)]
    x[n - 1] = b[n - 1] / A[n - 1][n - 1]

    for i in range(n - 2, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x


if __name__ == '__main__':
    A = [[1, -1, 2, -1],
         [2, -2, 3, -3],
         [1, 1, 1, 0],
         [1, -1, 4, 3]]

    b = [-8, -20, -2, 4]

    try:
        result = gauss_elimination(A, b)
        print("\nSolution for the system:")
        for x in result:
            print("{:.6f}".format(x))
    except ValueError as e:
        print(e)
