import numpy as np

def simpson(f, a, b):
    av = (b - a) / 2
    integral = (np.exp((-a) ** 2) * f(a)
                + 4 * np.exp((- (a + b) / 2)  ** 2) * f((a + b) / 2)
                + (np.exp((-b) ** 2) * f(b))) * av / 3
    return integral

def advancedSimpson(f, a, b, n, epsilon):
    integral = simpson(f, a, b)
    isUnsatisfying = True
    while isUnsatisfying:
        temp = 0
        av = (b - a) / (2 * n)
        left = a
        right = a + 2 * av
        for i in range (n):
            i = simpson(f, left, right)
            temp += i
            left = right
            right += 2 * av
            print(i)
        if abs(temp - integral) < epsilon:
            isUnsatisfying = False
            integral = temp
        else:
            integral = temp
            n += 1
    return integral
