import pyxel as px

class Entities():
    def __init__(self, x, y, h, w):
        self.x = x
        self.y = y
        self.h = h
        self.w = w

    def draw(self):
        px.rect(self.x, self.y, self.h, self.w, 9)

class Bullet(Entities):
    pass