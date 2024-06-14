import math


def simpsons_rule(f, start, end, intervals):
    step_size = (end - start) / intervals
    sum_result = calculate_odd_sum(f, start, step_size, intervals) + calculate_even_sum(f, start, step_size, intervals)
    return (step_size / 3) * (f(start) + f(end) + sum_result)


def calculate_odd_sum(f, start, step_size, intervals):
    total_sum = 0.0
    x = start + step_size
    for i in range(1, int(intervals / 2) + 1):
        total_sum += 4 * f(x)
        x += 2 * step_size
    return total_sum


def calculate_even_sum(f, start, step_size, intervals):
    total_sum = 0.0
    x = start + 2 * step_size
    for i in range(1, int(intervals / 2)):
        total_sum += 2 * f(x)
        x += 2 * step_size
    return total_sum


if __name__ == '__main__':
    f = lambda x: math.e ** (x ** 2)
    start = 0
    end = 1
    intervals = 10
    result = simpsons_rule(f, start, end, intervals)
    print(f"Integral of x^2 from {start} to {end} using Simpson's rule: {result}")