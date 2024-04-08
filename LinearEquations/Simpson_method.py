import math
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from sympy.utilities.lambdify import lambdify

x = sp.symbols('x')
def simpsons_rule(f, a, b, n):
    """
    Simpson's Rule for Numerical Integration

    Parameters:
    f (function): The function to be integrated.
    a (float): The lower limit of integration.
    b (float): The upper limit of integration.
    n (int): The number of subintervals (must be even).

    Returns:
    float: The approximate definite integral of the function over [a, b].
    """
    if n % 2 != 0:
        raise ValueError("Number of subintervals (n) must be even for Simpson's Rule.")

    # Check if function is defined in the given interval
    try:
        f_values = [f(a), f(b)]
        for i in range(1, n):
            x_i = a + i * (b - a) / n
            f_values.append(f(x_i))
    except (ValueError, TypeError):
        raise ValueError("Function is not defined for some points in the interval.")

    h = (b - a) / n

    integral = f(a) + f(b)  # Initialize with endpoints

    for i in range(1, n):
        x_i = a + i * h
        if i % 2 == 0:
            integral += 2 * f(x_i)
        else:
            integral += 4 * f(x_i)

    integral *= h / 3

    return integral


# Date: 8.04.2024
# Groups: Raphael Benoliel 209946854, Daniel Vaknin 314753161, Maor Hadad 312469463, Bar Cohen 316164938
# Name: Raphael Benoliel 200946854
if __name__ == '__main__':
    f = lambda x: (3*x**2 - math.sin(x**4 - x + 2)) / x**2
    n = 402
    a = -2.3
    b = -0.1

    # Check if the function is defined for some points in the interval
    if any(f(x) == 0 for x in np.linspace(a, b, 1000)):
        raise ValueError("Function is not defined for some points in the interval.")

    print(f" Division into n={n} sections ")
    integral1 = simpsons_rule(f, a, b, n)
    f2 = lambda x: (3 * x ** 2 - math.sin(x ** 4 - x + 2)) / x ** 2
    n2 = 402
    a2 = 0.1
    b2 = 2.1
    integral2 = simpsons_rule(f2, a2, b2, n2)
    print(f"Numerical Integration of definite integral in range [{a2},{b2}] is {integral1+integral2:.5f}")

