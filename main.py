import numpy as np
import functions as f
from newton_cotes import newton_cotes
from hermite import hermite

if __name__ == '__main__':
    print("Metody numeryczne - zadanie 4. Całkownanie numeryczne\n")
    print("Wariant 2 - wielomiany Hermite'a\n")

    print(newton_cotes(f.f2, 0.005))


