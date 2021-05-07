import numpy as np

def simpson(f, a, b, eps):
    dx = (b - a) / eps
    x = np.linspace(a, b, eps+1)
    y = f(x)
    result = dx / 3 * np.sum(y[0:-1:2] + 4 * y[1::2] + y[2::2])
    return result