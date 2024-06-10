
def secant_method(f, x0, x1, TOL, N=50):
    print("{:<10} {:<15} {:<15} {:<15}".format("Iteration", "xo", "x1", "p"))
    for i in range(N):
        if f(x1) - f(x0) == 0:
            print( " method cannot continue.")
            return

        p = x0 - f(x0) * ((x1 - x0) / (f(x1) - f(x0)))

        if abs(p - x1) < TOL:
            return p  # Procedure completed successfully
        print("{:<10} {:<15.6f} {:<15.6f} {:<15.6f}".format(i, x0, x1,p))
        x0 = x1
        x1 = p
    return p

# Date: 18.03.2024
# Groups: Raphael Benoliel 209946854, Daniel Vaknin 314753161, Maor Hadad 312469463, Bar Cohen 316164938
# Name: Raphael Benoliel 200946854


if __name__ == '__main__':
    f = lambda x: 6 * x **4 - 7 * x**3 - 2*x + 1
    x0 = 0
    x1 = 5
    TOL = 1e-6
    N = 20
    roots = secant_method(f, x0, x1, TOL, N)
    print(f"\n The equation f(x) has an approximate root at x = {roots}")