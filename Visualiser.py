import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle


class Visualiser(object):

    def __init__(self, cannon, projectile, physics):
        self.cannon = cannon
        self.projectile = projectile
        self.physics = physics

    def run(self):

        # Initialize figure
        figure = plt.figure()
        axes = figure.add_subplot('111', aspect='equal')
        axes.set_xlim(0, 2)
        axes.set_ylim(0, 2)

        # Initialize graphics objects
        castle = Rectangle((1.9, 0.0), 0.1, 0.1, color="red")
        axes.add_patch(castle)
        cannon = Rectangle((0.0, 0.0), 0.15, 0.1, angle=self.cannon.angle())
        axes.add_patch(cannon)
        ball = Circle((self.projectile.pos[0], self.projectile.pos[1]), 0.02)
        ball.set_visible(False)
        axes.add_patch(ball)

        def animate(frameNumber):
            # Without this, a copy of the figure will always be shown at its
            # original position.
            # Probably an easier way to do this, but the workaround is fine
            if frameNumber == 1:
                ball.set_visible(True)

            # Call the user updateFunc
            self.physics.timestep(self.projectile)

            ball.center = (self.projectile.pos[0], self.projectile.pos[1])

            return [ball]

        ani = animation.FuncAnimation(figure,
                                      animate,
                                      interval=25,
                                      blit=True)

        plt.show()
