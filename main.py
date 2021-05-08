import numpy as np
import functions as f
from simpson import advancedSimpson

if __name__ == '__main__':
    print("Metody numeryczne - zadanie 4. Całkownanie numeryczne\n")
    print("Wariant 2 - wielomiany Hermite'a\n")

    print(advancedSimpson(f.f1, -5, 5, 3, 5))