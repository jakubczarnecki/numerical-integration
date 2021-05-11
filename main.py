import functions as f
from newton_cotes import newton_cotes
from hermite import gauss_hermite
from plotter import drawGraph
import numpy as np

if __name__ == '__main__':
    funcs = {
        "1": f.f1,
        "2": f.f2,
        "3": f.f3,
        "4": f.f4,
        "5": f.f5
    }

    print("\n\nMetody numeryczne - zadanie 4. Całkownanie numeryczne")
    print("Wariant 2 - wielomiany Hermite'a\n")

    func = input("\n 1. f(x) = |2x - 3|"
                 "\n 2. f(x) = sin(x)"
                 "\n 3. f(x) = cos(2x)"
                 "\n 4. f(x) = x^2"
                 "\n 5. f(x) = cos(sin(x))\n"
                 "\nWybierz funkcję: ")

    epsilon = input("Podaj epsilon [Newton - Simpson]: ")
    nodes = input("Podaj liczbe wezlow (1-5) [Gauss - Hermite]: ")

    print("Wyniki:")
    print("\n--------------------\nNewton - Simpson: ")
    print(newton_cotes(funcs.get(func), f.w, np.double(epsilon)))
    print("\n--------------------\nGauss - Hermite: ")
    print(gauss_hermite(funcs.get(func), int(nodes)))

    drawGraph(funcs.get(func), f.w)
