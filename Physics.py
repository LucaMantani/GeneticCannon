import numpy as np


class Physics(object):
    """
    It defines the Physics of the problem. In particular
    the user can set the strength of gravity and the viscosity of the air.
    """

    def __init__(self, gravity=0, viscosity=0):
        self._gravity = gravity
        self._viscosity = viscosity

    def timestep(self, projectile):
        """
        Modifies the projectile speed and position according to
        Newton's mechanics laws.
        """
        projectile.speed += -self._gravity * np.array([0, 1])
        - self._viscosity / projectile.mass * projectile.speed

        projectile.pos += projectile.speed

    def collision(self, projectile):
        return (projectile.pos[0] > 1.9 and projectile.pos[0] < 2
                and projectile.pos[1] > 0.0 and projectile.pos[1] < 0.1)
