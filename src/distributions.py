from random import uniform
from math import log, sqrt, e

def exponential(lambd):
    u = uniform(0, 1)
    return - (1 / lambd) * log(u, e)
    
def normal(mean, var):
    sd = sqrt(var)
    while True:
        y = exponential(1)
        u = uniform(0, 1)
        if u <= e**((-(y-1)**2)/2):
            u = uniform(0, 1)
            z = y if u <= 1/2 else -y
            return mean + sd*z

def bernoulli(p):
    u = uniform(0, 1)
    return True if u < p else False

if __name__ == "__main__":
    for _ in range(100):
        z = normal(0, 1)
        print(z)
