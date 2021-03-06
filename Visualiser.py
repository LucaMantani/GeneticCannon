import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Circle, Rectangle


class Visualiser(object):

    def __init__(self, cannon, projectile, castle, physics):
        self.cannon = cannon
        self.projectile = projectile
        self.castle = castle
        self.physics = physics

    def run(self):

        # Initialize figure
        figure = plt.figure()
        axes = figure.add_subplot('111', aspect='equal')
        axes.set_xlim(0, 2)
        axes.set_ylim(0, 2)

        # Initialize graphics objects
        castle = Rectangle(tuple(self.castle.pos),
                           self.castle.width, self.castle.height, color="red")
        axes.add_patch(castle)
        cannon = Rectangle((0.0, -0.04), 0.15, 0.08, angle=self.cannon.angle())
        axes.add_patch(cannon)
        ball = Circle((self.projectile.pos[0], self.projectile.pos[1]), 0.02)
        ball.set_visible(False)
        axes.add_patch(ball)

        # shoot the ball

        self.cannon.shoot(self.projectile)

        def animate(frameNumber):
            # Without this, a copy of the figure will always be shown at its
            # original position.
            # Probably an easier way to do this, but the workaround is fine
            if frameNumber == 1:
                ball.set_visible(True)

            # Call the user updateFunc
            self.physics.timestep(self.projectile)

            ball.center = (self.projectile.pos[0], self.projectile.pos[1])

            # if self.physics.collision(self.projectile, self.castle):
            #     raise TypeError

            return [ball]

        ani = animation.FuncAnimation(figure,
                                      animate,
                                      frames=100,
                                      interval=25,
                                      repeat=False,
                                      blit=True)

        plt.show()
