from matrix_utility import row_addition_elementary_matrix, scalar_multiplication_elementary_matrix
import numpy as np

"""
Function that find the inverse of non-singular matrix
The function performs elementary row operations to transform it into the identity matrix. 
The resulting identity matrix will be the inverse of the input matrix if it is non-singular.
 If the input matrix is singular (i.e., its diagonal elements become zero during row operations), it raises an error.
"""

"""
Date:
Groups: Raphael Benoliel 209946854
Daniel Vaknin 314753161
Maor Hadad 312469463
Bar Cohen 316164938
Git: https://github.com/RaphaelBenoliel/Numerical-Analysis/tree/main/LinearEquations
"""
def matrix_inverse(matrix):
    print(f"=================== Finding the inverse of a non-singular matrix using elementary row operations ===================\n {matrix}\n")
    if matrix.shape[0] != matrix.shape[1]:
        raise ValueError("Input matrix must be square.")

    n = matrix.shape[0]
    identity = np.identity(n)

    # Perform row operations to transform the input matrix into the identity matrix
    for i in range(n):
        if matrix[i, i] == 0:
            for k in range(i + 1, n):
                if matrix[k, i] != 0 and matrix[i, k] != 0:
                    # Swap rows i and k
                    matrix[[i, k]] = matrix[[k, i]]
                    identity[[i, k]] = identity[[k, i]]
                    # print(f"Swapped rows {i + 1} and {k + 1}:\n", matrix)
                    break
            else:
                raise ValueError("Matrix is singular, cannot find its inverse.")

        if matrix[i, i] != 1:
            # Scale the current row to make the diagonal element 1
            scalar = 1.0 / matrix[i, i]
            elementary_matrix = scalar_multiplication_elementary_matrix(n, i, scalar)
            print(f"elementary matrix to make the diagonal element 1 :\n {elementary_matrix} \n")
            matrix = np.dot(elementary_matrix, matrix)
            print(f"The matrix after elementary operation :\n {matrix}")
            print("------------------------------------------------------------------------------------------------------------------")
            identity = np.dot(elementary_matrix, identity)

        # Zero out the elements above and below the diagonal
        for j in range(n):
            if i != j:
                scalar = -matrix[j, i]
                elementary_matrix = row_addition_elementary_matrix(n, j, i, scalar)
                print(f"elementary matrix for R{j+1} = R{j+1} + ({scalar}R{i+1}):\n {elementary_matrix} \n")
                matrix = np.dot(elementary_matrix, matrix)
                print(f"The matrix after elementary operation :\n {matrix}")
                print("------------------------------------------------------------------------------------------------------------------")
                identity = np.dot(elementary_matrix, identity)

    return identity


if __name__ == '__main__':

    A = np.array([[1, 2, 3],
                  [2, 4, 4],
                  [3, 4, 6]])

    try:
        A_inverse = matrix_inverse(A)
        print("\nInverse of matrix A: \n", A_inverse)
        print("=====================================================================================================================")

    except ValueError as e:
        print(str(e))


