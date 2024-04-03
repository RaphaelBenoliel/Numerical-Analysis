import numpy as np
from numpy.polynomial.polynomial import Polynomial

def newton_raphson(polynomial, test_range, epsilon=0.0001):
    def evaluate(coefficients, x):
        return np.polyval(coefficients, x)

    def derivative(coefficients):
        return np.polyder(coefficients)

    def newton_iteration(coefficients, x, epsilon):
        iterations = 0
        while True:
            fx = evaluate(coefficients, x)
            if abs(fx) < epsilon:
                break
            dfx = evaluate(derivative(coefficients), x)
            if dfx == 0:
                break
            x = x - fx / dfx
            iterations += 1
        return x, iterations

    coefficients = polynomial.coef[::-1]
    a, b = test_range
    initial_guess = (a + b) / 2
    root, iterations = newton_iteration(coefficients, initial_guess, epsilon)
    print(f"Root found at {root} in {iterations} iterations.")

def secant_method(polynomial, test_range, epsilon=0.0001):
    def evaluate(coefficients, x):
        return np.polyval(coefficients, x)

    def secant_iteration(coefficients, x0, x1, epsilon):
        iterations = 0
        while True:
            fx0 = evaluate(coefficients, x0)
            fx1 = evaluate(coefficients, x1)
            if abs(fx1) < epsilon:
                break
            x_next = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
            x0, x1 = x1, x_next
            iterations += 1
        return x1, iterations

    coefficients = polynomial.coef[::-1]
    a, b = test_range
    root, iterations = secant_iteration(coefficients, a, b, epsilon)
    print(f"Root found at {root} in {iterations} iterations.")

if __name__ == "__main__":
    # Example usage
    poly = Polynomial([1, -5, 6])  # Represents x^2 - 5x + 6
    test_range = (1, 4)  # Test range where a root exists
    epsilon = 0.0001

    print("Using Newton-Raphson method:")
    newton_raphson(poly, test_range, epsilon)

    print("\nUsing Secant method:")
    secant_method(poly, test_range, epsilon)
