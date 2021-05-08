nodes = ([])
weights = ([])

def hermite(values, numOfNodes, f):
    result = 0
    for i in range(5):
        if(values[numOfNodes - 2][i] != 0):
            multiplier = weights[numOfNodes - 2][i] * f(nodes[numOfNodes - 2][i])
            result += multiplier
    return result

