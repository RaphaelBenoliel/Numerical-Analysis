import math


def richardson_derivative(f, x, h):
    D_h = (f(x + h) - f(x)) / h
    D_2h = (f(x + 2*h) - f(x)) / (2*h)
    D_richardson = (4 * D_h - D_2h) / 3
    return D_richardson


if __name__ == '__main__':
    def f(x):
        return math.sin(x)

    x = math.pi / 4
    h = 0.01

    derivative = richardson_derivative(f, x, h)
    print("The derivative of f at x =", x, "is approximately", derivative)
