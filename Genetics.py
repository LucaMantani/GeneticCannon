import numpy as np
from Cannon import Cannon


def generateInitialPopulation(size):
    return [Cannon(np.random.rand(2)/10) for _ in range(size)]


def generateSon(parents):
    '''
    It takes the parents impulse and produce a cannon son whose impulse
    is the average of the parents impulses
    '''
    parent1, parent2 = parents
    newImpulse = (parent1.impulse + parent2.impulse) / 2

    # mutation
    newImpulse += (np.random.rand(2)-0.5)/300
    return Cannon(newImpulse)


def evolve(population, fitnessFunc):
    scores = [fitnessFunc(cannon) for cannon in population]
    totalScore = sum(scores)
    probs = [score / totalScore for score in scores]

    children = [generateSon(np.random.choice(population, 2, p=probs))
                for _ in population]

    return children
