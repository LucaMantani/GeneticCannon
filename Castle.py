import numpy as np


class Castle(object):

    def __init__(self, width=0.1, height=0.1, pos=np.array([1.9, 0.0])):
        self.width = width
        self.height = height
        self.pos = pos
