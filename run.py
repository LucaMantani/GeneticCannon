from Cannon import Cannon
from Projectile import Projectile
from Physics import Physics
import numpy as np
from Visualiser import Visualiser
from Castle import Castle
from Genetics import generateInitialPopulation, evolve

def score(cannon):

    global ball, physics, castle

    projectile = ball.copy()

    cannon.shoot(projectile)

    rel_pos = []

    while projectile.pos[1] >= castle.pos[1]:
        physics.timestep(projectile)

        rel_pos.append(physics.distance(projectile, castle))

    scores = (2 - np.array(rel_pos)) / 2

    return max(scores) if len(rel_pos) > 0 else 0.0


ball = Projectile(2.0)

impulse = np.array([0.08, 0.05])

castle = Castle()

physics = Physics(0.001)


cannons = generateInitialPopulation(100)

for i in range(100):
    scores = []
    for cannon in cannons:
        scores.append(score(cannon))

    if i % 10 == 0:
        a = Visualiser(np.random.choice(cannons), ball.copy(), castle, physics)

        a.run()

    print("Min score for generation %i is %f" % (i, min(scores)))

    cannons = evolve(cannons, score)


