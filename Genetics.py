import numpy as np
from Cannon import Cannon


def generateInitialPopulation(size):
    return [Cannon(np.random.rand(2)) for _ in range(size)]
