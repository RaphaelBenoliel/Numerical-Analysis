import numpy as np


def trapezoidal_rule(f, a, b, n):
    h = (b - a) / n
    x = np.linspace(a, b, n+1)
    y = f(x)
    # Applying the trapezoidal rule
    integral = h * (0.5 * y[0] + 0.5 * y[-1] + sum(y[1:-1]))
    return integral


def main():
    a = 0
    b = np.pi
    n = 4
    f = np.sin
    integral = trapezoidal_rule(f, a, b, n)
    exact_value = 2
    error = abs(exact_value - integral)

    print(f"Calculated integral: {integral}")
    print(f"Exact integral: {exact_value}")
    print(f"Error: {error}")


if __name__ == "__main__":
    main()
