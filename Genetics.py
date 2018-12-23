import numpy as np
from Cannon import Cannon


def generateInitialPopulation(size):
    return [Cannon(np.random.rand(2)/10) for _ in range(size)]

def score(cannon, projectile, castle, physics):

    projectile = projectile.copy()

    cannon.shoot(projectile)

    rel_pos = []

    while projectile.pos[1] >= castle.pos[1]:
        physics.timestep(projectile)

        rel_pos.append(physics.distance(projectile, castle))

        if physics.collision(projectile, castle):
            return 0

    return min(rel_pos) if len(rel_pos) > 0 else 10.0

