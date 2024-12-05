# given function
def func(x):
    return -x ** 2 + 4 * x + 1


# gradient of given function
def gradient_func(x):
    return -2 * x + 4


def gradient_ascent_method(gradient, f, x, alpha, n):
    for i in range(n):
        # making step towards maximum
        x = x + alpha * gradient(x)
    return x, f(x)


with open("tests/task3.txt", "r") as f:
    # data input
    x_0, learning_rate, iterations_number = [float(el) for el in f.readline().split()]
    # answer output
    print(*gradient_ascent_method(gradient_func, func, x_0, learning_rate, int(iterations_number)))
