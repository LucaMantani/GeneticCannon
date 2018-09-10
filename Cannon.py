

class Cannon(object):
    """
    Class definition of a simple cannon.
    Parameters: 2-dim numpy array that defines the impulse.
    """

    def __init__(self, impulse):
        self._impulse = impulse

    def shoot(self, projectile):
        """
        Receives a Projectile object and applies the impulse
        to give speed to it.
        Return: Projectile object with initial speed.
        """
        projectile.speed = self._impulse / projectile.mass
        return projectile
