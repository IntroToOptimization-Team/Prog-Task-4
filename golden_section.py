# given function
def func(x):
    return (x - 2) ** 2 + 3


def golden_section(f, x_l, x_r, eps):
    # repeat algorithm until interval is too small
    while abs(x_r - x_l) > eps:
        x_1 = x_r - ((5 ** 0.5 - 1) / 2) * (x_r - x_l)
        x_2 = x_l + ((5 ** 0.5 - 1) / 2) * (x_r - x_l)
        f1 = f(x_1)
        f2 = f(x_2)
        # make interval less by going towards of minimum
        if f1 > f2:
            x_l = x_1
        elif f1 < f2:
            x_r = x_2
        else:
            x_l = x_1
            x_r = x_2
    # return midpoint of small interval as point of minimum
    return (x_r + x_l) / 2, f((x_r + x_l) / 2)


with open("tests/task2.txt", "r") as f:
    # data input
    left, right, tolerance = [float(el) for el in f.readline().split()]
    # answer output
    print(*golden_section(func, left, right, tolerance))
