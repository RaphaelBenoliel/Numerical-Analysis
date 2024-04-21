import numpy as np


def linear_interpolation(points, x):
    (x0, y0), (x1, y1) = points
    y = y0 + (y1 - y0) * (x - x0) / (x1 - x0)
    return y


def polynomial_interpolation(points, x):
    A = np.array([[p[0]**2, p[0], 1] for p in points])
    B = np.array([p[1] for p in points])
    coefficients = np.linalg.solve(A, B)
    y = np.dot(coefficients, [x**2, x, 1])
    return y


def lagrange_interpolation(points, x):
    total = 0
    n = len(points)
    for i in range(n):
        xi, yi = points[i]
        term = yi
        for j in range(n):
            if i != j:
                xj, _ = points[j]
                term *= (x - xj) / (xi - xj)
        total += term
    return total


def main():
    # Define example points and x-value for demonstration
    points = [(2, 0.9093), (3, 0.1411), (4, 1.5)]
    x_value = 2.5

    # Calculate interpolated values
    linear_result = linear_interpolation(points[:2], x_value)
    polynomial_result = polynomial_interpolation(points, x_value)
    lagrange_result = lagrange_interpolation(points, x_value)

    print(f"Linear Interpolation result: {linear_result}")
    print(f"Polynomial Interpolation result: {polynomial_result}")
    print(f"Lagrange Interpolation result: {lagrange_result}")


if __name__ == "__main__":
    main()
