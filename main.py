import numpy as np
import functions as f
from newton_cotes import newton_cotes
from hermite import gauss_hermite

if __name__ == '__main__':
    print("Metody numeryczne - zadanie 4. Całkownanie numeryczne\n")
    print("Wariant 2 - wielomiany Hermite'a\n")

    print("Wybierz funkcję:"
          "\n 1. f(x) = 2x - 4"
          "\n 2. f(x) = |2x - 3|"
          "\n 3. f(x) = sin(x)"
          "\n 4. f(x) = cos(2x)"
          "\n 5. f(x) = x^2")
    func = input()
    if func == "1":
        func = f.f0
    elif func == "2":
        func = f.f1
    elif func == "3":
        func = f.f2
    elif func == "4":
        func = f.f3
    elif func == "5":
        func = f.f4

    print("Wybierz metodę:"
          "\n 1 - Newton-Cotes"
          "\n 2 - Hermite")
    choice = input()

    print("Wynik:")
    if choice == "1":
        print("podaj epsilon:")

        print(newton_cotes(func, 0.01))
    elif choice == "2":
        print("podaj liczbę węzłów:")
        print(gauss_hermite(f.f3, 5))

