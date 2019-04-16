import pyxel as px
from entities import Entities, Spacecraft, Bullet, En3
from time import time
import math

WIDTH = 150
LENGTH = 200

WHITE = 7
RED = 8
YELLOW = 10
GREEN = 11
BLUE = 12

FPS = 60


class App:
    def __init__(self):
        px.init(WIDTH, LENGTH, fps=FPS)

        self.player = Spacecraft(WIDTH // 2, LENGTH // 2, 15, 15, 6)
        self.player_bullets = []
        self.ennemy = En3()
        self.stt = time()  # Starting Time

        px.run(self.update, self.draw)

    def update(self):
        self.player.update(self.player_bullets)
        for bullet in self.player_bullets:
            bullet.update()

        self.ennemy.update()

    def draw(self):
        px.cls(0)

        # Test line
        px.line(WIDTH / 2, 0, WIDTH/2, LENGTH, RED)
        px.line(0, LENGTH/2, WIDTH, LENGTH/2, RED)

        self.player.draw()
        for bullet in self.player_bullets:
            bullet.draw()

        self.ennemy.draw()


App()
