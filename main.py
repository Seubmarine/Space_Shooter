import pyxel as px
from entities import Entities, Spacecraft, Bullet

WIDTH = 150
LENGTH = 200


class App:
    def __init__(self):
        px.init(WIDTH, LENGTH)
        self.player = Spacecraft(WIDTH // 2, LENGTH // 2, 15, 15, 4)
        px.run(self.update, self.draw)

    def update(self):
        self.player.update()

    def draw(self):
        px.cls(0)
        self.player.draw()

        # Test line
        px.line(55, 23, 65, 90, 12)


App()
