# given function
def func(x):
    return x ** 3 - 6 * x ** 2 + 11 * x - 6


def bisection_method(f, a, b, eps):
    c = (a + b) / 2
    # function of left and right border should have different signs
    if f(a) * f(b) > 0:
        return Exception("Method is not applicable")
    # repeat algorithm until solution is found
    while abs(f(c)) >= eps:
        # make interval under consideration smaller
        if f(a) * f(c) > 0:
            a = c
        else:
            b = c
        c = (a + b) / 2
    return c


with open("tests/task1.txt", "r") as f:
    # data input
    left, right, tolerance = [float(el) for el in f.readline().split()]
    # answer output
    print(bisection_method(func, left, right, tolerance))
