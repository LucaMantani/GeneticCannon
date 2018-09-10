import numpy as np


class Projectile(object):
    """
    Defines a Projectile with mass m. 
    Speed and position are set by default at zero 2-dim.
    """

    def __init__(self, mass):
        self._mass = mass
        self.pos = np.array([0.0, 0.0])
        self.speed = np.array([0.0, 0.0])

    @property
    def mass(self):
        return self._mass

    def __str__(self):
        return "({}, {})".format(self.pos, self.speed)
