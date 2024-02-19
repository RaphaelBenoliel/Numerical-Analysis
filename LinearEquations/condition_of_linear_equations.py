import numpy as np
from inverse_matrix import matrix_inverse
from matrix_utility import print_matrix


def norm(mat):
    size = len(mat)
    max_row = 0
    for row in range(size):
        sum_row = 0
        for col in range(size):
            sum_row += abs(mat[row][col])
        if sum_row > max_row:
            max_row = sum_row
    return max_row


def condition_number(A):
    # Step 1: Calculate the max norm (infinity norm) of A
    norm_A = norm(A)

    # Step 2: Calculate the inverse of A
    A_inv = matrix_inverse(A)

    # Step 3: Calculate the max norm of the inverse of A
    norm_A_inv = norm(A_inv)

    # Step 4: Compute the condition number
    cond = norm_A * norm_A_inv

    print("A:")
    print_matrix(A)

    print("inverse of A:")
    print_matrix(A_inv)

    print("Max Norm of A:", norm_A, "\n")

    print("max norm of the inverse of A:", norm_A_inv)

    return cond

# Date: 19.02.2024
# Groups: Raphael Benoliel 209946854, Daniel Vaknin 314753161, Maor Hadad 312469463, Bar Cohen 316164938
# Git: https://github.com/RaphaelBenoliel/Numerical-Analysis/blob/main/LinearEquations/condition_of_linear_equations.py
# Name: Raphael Benoliel


if __name__ == '__main__':
    A = np.array([[1, 0.5, 0.333333],
                  [0.5, 0.333333, 0.25],
                  [0.333333, 0.25, 0.2]])
    print("Max Norm of A:", norm(A), "\n")
    cond = condition_number(A)

    print("\n condition number: ", cond)

