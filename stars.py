import pyxel
import random


class Stars(object):
    def __init__(self):
        self.stars = [Star() for s in range(100)]

    def draw(self):
        [s.draw() for s in self.stars]


class Star(object):
    def __init__(self):

        self.x = random.randint(0, pyxel.width)
        self.y = random.randint(0, pyxel.height)

    def draw(self):
        pyxel.pset(self.x, self.y, pyxel.COLOR_WHITE)

        self.y -= 1
        # self.x += 1
        if self.y < 0:
            self.x = random.randint(0, pyxel.width)
            self.y = pyxel.height
