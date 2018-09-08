import numpy as np


class Cannon(object):

    def __init__(self, impulse):
        self._impulse = impulse

    def shoot(self, projectile):
        projectile.speed = self._impulse / projectile.mass
        return projectile
