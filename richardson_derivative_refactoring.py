def forward_difference(f, x, h):
    """Compute the forward difference approximation of the derivative."""
    return (f(x + h) - f(x)) / h


def richardson_extrapolation(D_h, D_2h):
    """Apply Richardson extrapolation to improve the derivative approximation."""
    return (4 * D_h - D_2h) / 3


def richardson_derivative(f, x, h):
    """Compute the derivative using Richardson extrapolation."""
    if h == 0:
        raise ValueError("Step size h cannot be zero.")

    D_h = forward_difference(f, x, h)
    D_2h = forward_difference(f, x, 2 * h)
    return richardson_extrapolation(D_h, D_2h)


if __name__ == '__main__':
    import math


    def f(x):
        return math.sin(x)


    x = math.pi / 4  # Example value of x
    h = 0.01  # Example step size

    try:
        derivative = richardson_derivative(f, x, h)
        print("The derivative of f at x =", x, "is approximately", derivative)
    except ValueError as e:
        print("Error:", e)
