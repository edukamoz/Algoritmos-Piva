import math


def calcular_volume(r):
    v = 4/3 * math.pi * math.pow(r, 3)
    return v


print(calcular_volume(5))
