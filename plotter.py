import matplotlib.pyplot as plt
import numpy as np
import time as t

def drawGraph(f, w):
    time = t.strftime("%Y%m%d-%H%M%S")
    x = np.arange(-6, 6, 0.1)
    plt.plot(x, f(x) * w(x))
    plt.savefig(time + ".png")
    print("\nSpojrz na wygenerowany wykres!\n\nPlik: " + time + ".png")